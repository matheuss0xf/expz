from fastapi.testclient import TestClient
from app.app import app


def test_root_deve_retornar_200_e_ola_mundo():
    client = TestClient(app) # Organizar (Arrange)
    response = client.get('/') # Agir (Act)

    assert response.status_code == 200 # Afirmar (Assert)
    assert response.json() == {'message': 'Olá Mundo!'} # Afirmar (Assert)
