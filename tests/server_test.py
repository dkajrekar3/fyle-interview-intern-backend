def test_server(client):
    response = client.get(
        '/'
    )

    assert response.status_code == 200