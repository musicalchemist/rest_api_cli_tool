import unittest
from unittest.mock import patch
import requests_mock
import api_handler as api

class TestAPIHandler(unittest.TestCase):

    @requests_mock.Mocker()
    def test_get_posts(self, mock):
        mock.get('https://jsonplaceholder.typicode.com/posts', status_code=200, json=[{"id": 1, "title": "Test Post"}])
        response = api.get_posts()
        self.assertEqual(response, [{"id": 1, "title": "Test Post"}])

    @requests_mock.Mocker()
    def test_create_post(self, mock):
        mock.post('https://jsonplaceholder.typicode.com/posts', status_code=201, json={"id": 101, "title": "New Post", "body": "This is a new post", "userId": 1})
        response = api.create_post("New Post", "This is a new post", 1)
        self.assertEqual(response, {"id": 101, "title": "New Post", "body": "This is a new post", "userId": 1})

    @requests_mock.Mocker()
    def test_update_post(self, mock):
        mock.put('https://jsonplaceholder.typicode.com/posts/1', status_code=200, json={"id": 1, "title": "Updated Post", "body": "This is an updated post", "userId": 1})
        response = api.update_post(1, "Updated Post", "This is an updated post", 1)
        self.assertEqual(response, {"id": 1, "title": "Updated Post", "body": "This is an updated post", "userId": 1})

    @requests_mock.Mocker()
    def test_delete_post(self, mock):
        mock.delete('https://jsonplaceholder.typicode.com/posts/1', status_code=200)
        response = api.delete_post(1)
        self.assertEqual(response, 200)

if __name__ == '__main__':
    unittest.main()
