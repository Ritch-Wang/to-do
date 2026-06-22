from app import app

def test_list_route():
    client = app.test_client()

    response = client.get("/list")

    assert response.status_code == 200
    assert response.get_json() == {"message": "hello_world"}