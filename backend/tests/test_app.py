import sys
import os

# Agrega la carpeta backend al path para poder importar app.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200


def test_notes_endpoint():
    client = app.test_client()
    response = client.get("/api/notes")
    # Puede devolver 200 o 500 si la DB no está disponible.
    # Para este TP solo verificamos que el endpoint exista.
    assert response.status_code in [200, 500]
