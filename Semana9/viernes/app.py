
import base64
import binascii
import io
import os
import re
import uuid
from pathlib import Path

from flask import Flask, jsonify, render_template, request, session
from PIL import Image, UnidentifiedImageError

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get(
    "FLASK_SECRET_KEY", "clave-solo-desarrollo"
)
app.config["MAX_CONTENT_LENGTH"] = 7 * 1024 * 1024
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"

UPLOAD_FOLDER = Path(app.root_path) / "static" / "uploads"
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

MAX_IMAGE_SIZE = 5 * 1024 * 1024
ALLOWED_FORMATS = {
    "image/jpeg": "JPEG",
    "image/png": "PNG",
    "image/webp": "WEBP",
}


class Stack:
    """Pila LIFO con capacidad limitada."""

    def __init__(self, items=None, capacity=5):
        if (
            not isinstance(capacity, int)
            or isinstance(capacity, bool)
            or capacity < 1
        ):
            raise ValueError("Capacidad inválida.")

        self.capacity = capacity
        self.items = list(items) if items is not None else []

        if len(self.items) > capacity:
            raise ValueError("La pila supera su capacidad.")

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) >= self.capacity

    def push(self, item):
        if self.is_full():
            return False, "La pila está llena."

        self.items.append(item)
        return True, "Elemento apilado correctamente."

    def pop(self):
        if self.is_empty():
            return False, "La pila está vacía."

        return True, self.items.pop()

    def peek(self):
        if self.is_empty():
            return False, "La pila está vacía."

        return True, self.items[-1]

    def show(self):
        return list(reversed(self.items))


def get_stack():
    return Stack(
        items=session.get("items", []),
        capacity=session.get("capacity", 5),
    )


def save_stack(stack):
    session["items"] = stack.items
    session["capacity"] = stack.capacity


def respond(success, message, stack, status=200, **extra):
    items = stack.show()
    top = items[0] if items else None

    return jsonify({
        "success": success,
        "message": message,
        "items": items,
        "size": len(stack.items),
        "capacity": stack.capacity,
        "is_empty": stack.is_empty(),
        "is_full": stack.is_full(),
        "top": top,
        **extra,
    }), status


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/api/state")
def state():
    stack = get_stack()
    return respond(True, "Estado de la pila.", stack)


@app.post("/api/capacity")
def set_capacity():
    data = request.get_json(silent=True) or {}
    capacity = data.get("capacity")
    stack = get_stack()

    if (
        not isinstance(capacity, int)
        or isinstance(capacity, bool)
        or not 1 <= capacity <= 100
    ):
        return respond(
            False, "La capacidad debe estar entre 1 y 100.",
            stack, 400
        )

    if capacity < len(stack.items):
        return respond(
            False,
            "La capacidad no puede ser menor que los elementos actuales.",
            stack, 400
        )

    stack.capacity = capacity
    save_stack(stack)

    return respond(True, "Capacidad actualizada.", stack)


@app.post("/api/push")
def push_item():
    data = request.get_json(silent=True) or {}
    item = data.get("item")
    stack = get_stack()

    if not isinstance(item, str) or not item.strip():
        return respond(False, "Introduce un valor válido.", stack, 400)

    item = item.strip()

    if len(item) > 100:
        return respond(
            False, "El valor no puede superar 100 caracteres.",
            stack, 400
        )

    success, message = stack.push(item)

    if success:
        save_stack(stack)

    return respond(
        success, message, stack, 200 if success else 400
    )


@app.post("/api/photo")
def save_photo():
    data = request.get_json(silent=True) or {}
    data_url = data.get("image")
    stack = get_stack()

    if stack.is_full():
        return respond(False, "La pila está llena.", stack, 400)

    if not isinstance(data_url, str):
        return respond(
            False, "No se recibió ninguna fotografía.", stack, 400
        )

    match = re.fullmatch(
        r"data:(image/(?:jpeg|png|webp));base64,"
        r"([A-Za-z0-9+/]*={0,2})",
        data_url,
    )

    if not match:
        return respond(
            False, "El formato de la imagen no es válido.",
            stack, 400
        )

    mime_type, encoded_image = match.groups()

    try:
        image_bytes = base64.b64decode(
            encoded_image, validate=True
        )

        if not image_bytes or len(image_bytes) > MAX_IMAGE_SIZE:
            return respond(
                False, "La imagen está vacía o supera los 5 MB.",
                stack, 400
            )

        with Image.open(io.BytesIO(image_bytes)) as image:
            image.verify()

        with Image.open(io.BytesIO(image_bytes)) as image:
            if image.format != ALLOWED_FORMATS[mime_type]:
                return respond(
                    False, "El formato de imagen no coincide.",
                    stack, 400
                )

            image = image.convert("RGB")
            image.thumbnail((1920, 1920))

            filename = f"{uuid.uuid4().hex}.jpg"
            destination = UPLOAD_FOLDER / filename

            image.save(
                destination,
                format="JPEG",
                quality=85,
                optimize=True,
            )

    except (
        ValueError,
        binascii.Error,
        UnidentifiedImageError,
        OSError,
    ):
        return respond(
            False, "No se pudo procesar la fotografía.", stack, 400
        )

    photo_number = 1 + sum(
        1 for item in stack.items
        if isinstance(item, dict) and item.get("type") == "photo"
    )

    photo_item = {
        "type": "photo",
        "name": f"Fotografía {photo_number}",
        "url": f"/static/uploads/{filename}",
    }

    success, message = stack.push(photo_item)

    if not success:
        destination.unlink(missing_ok=True)
        return respond(False, message, stack, 400)

    save_stack(stack)

    return respond(True, "Fotografía guardada en la pila.", stack)


@app.post("/api/pop")
def pop_item():
    stack = get_stack()
    success, result = stack.pop()

    if success:
        save_stack(stack)

    return respond(
        success,
        "Elemento desapilado." if success else result,
        stack,
        200 if success else 400,
        removed=result if success else None,
    )


@app.get("/api/peek")
def peek_item():
    stack = get_stack()
    success, result = stack.peek()

    return respond(
        success,
        "Tope consultado." if success else result,
        stack,
        200 if success else 400,
        top=result if success else None,
    )


@app.post("/api/clear")
def clear_stack():
    stack = get_stack()
    stack.items.clear()
    save_stack(stack)

    return respond(True, "Pila vaciada correctamente.", stack)


@app.errorhandler(413)
def request_too_large(error):
    stack = get_stack()
    return respond(
        False, "La solicitud supera el tamaño permitido.",
        stack, 413
    )


if __name__ == "__main__":
    app.run(debug=True)
