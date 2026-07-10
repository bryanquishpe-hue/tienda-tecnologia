def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200

def test_agregar_producto_page(client):
    response = client.get("/agregar")
    assert response.status_code == 200