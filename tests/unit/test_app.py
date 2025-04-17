import app

def test_home():
    # Create a test client using the Flask app
    test_client = app.app.test_client()

    # Send a GET request to "/"
    response = test_client.get("/")

    # Check if the response data is correct
    assert response.status_code == 200
    assert "<title>Cloud Native App</title>" in response.data.decode("utf-8")
