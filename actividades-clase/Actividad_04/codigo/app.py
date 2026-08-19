from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os

app = Flask(__name__)
limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["60 per minute"],
    storage_uri="memory://",
)

API_TOKEN = os.getenv("API_TOKEN")

CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

@app.after_request
def agregar_cabeceras_seguridad(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Content-Security-Policy"] = "default-src 'none'"
    response.headers["Cache-Control"] = "no-store"
    return response

USUARIOS = [
    {"id": 1, "nombre": "Ana", "rol": "analista"},
    {"id": 2, "nombre": "Luis", "rol": "auditor"},
]

ROLES_PERMITIDOS = {"analista", "auditor"}

@app.get("/health")
def health():
    return jsonify({"estado": "ok"}), 200

# Este endpoint comprueba tres situaciones: que el servidor tenga un token configurado,
# que el cliente lo envíe como Bearer y que coincida con el valor esperado.
@app.get("/usuarios")
@limiter.limit("10 per minute")
def obtener_usuarios():
    if not API_TOKEN:
        return jsonify({"error": "Configuracion de seguridad incompleta"}), 500

    autorizacion = request.headers.get("Authorization", "")

    if autorizacion != f"Bearer {API_TOKEN}":
        return jsonify({"error": "No autorizado"}), 401

    rol = request.args.get("rol", "").strip().lower()

    if rol and rol not in ROLES_PERMITIDOS:
        return jsonify({
            "error": "Parametro rol invalido",
            "valores_permitidos": sorted(ROLES_PERMITIDOS),
        }), 400

    usuarios_filtrados = (
        [usuario for usuario in USUARIOS if usuario["rol"] == rol]
        if rol
        else USUARIOS
    )

    return jsonify({"usuarios": usuarios_filtrados}), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
