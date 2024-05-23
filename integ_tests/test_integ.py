import pytest
import sys
import os

# Add the app directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_login(client):
    # Test login page loads correctly
    response = client.get('/login')
    assert response.status_code == 200

    # Test login with incorrect credentials
    response = client.post('/login', data={'username': 'wronguser', 'password': 'wrongpass'})
    assert response.status_code == 200
    assert b'Invalid username or password' in response.data

    # Test login with correct credentials (assuming these credentials exist in the DB)
    response = client.post('/login', data={'username': 'testuser', 'password': 'testpass'})
    assert response.status_code == 302  # Redirect to index
    assert response.headers['Location'] == 'http://localhost/'

def test_access_index_without_login(client):
    # Test accessing index without logging in redirects to login
    response = client.get('/')
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/login'

def test_access_index_with_login(client):
    # Log in with correct credentials
    client.post('/login', data={'username': 'testuser', 'password': 'testpass'})

    # Test accessing index after logging in
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome' in response.data  # Adjust based on your index.html content

def test_get_coordinates(client):
    # Log in with correct credentials
    client.post('/login', data={'username': 'testuser', 'password': 'testpass'})

    # Test getting coordinates for a valid address
    response = client.get('/coordinates', query_string={'address': '1600 Amphitheatre Parkway, Mountain View, CA'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'latitude' in data
    assert 'longitude' in data
    assert 'avg_FR' in data

    # Test getting coordinates for an invalid address
    response = client.get('/coordinates', query_string={'address': 'Invalid Address'})
    assert response.status_code == 404
    data = response.get_json()
    assert data['error'] == 'Address not found'
