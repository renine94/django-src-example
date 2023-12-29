def test_index(client):
    # Given
    ...

    # When
    response = client.get('/boards/')

    # Then
    assert response.json() == "hello world"

