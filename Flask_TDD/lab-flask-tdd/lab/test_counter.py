"""
Test Cases for Counter Web Service

Requirements for the counter service
- The API must be RESTful.
- The endpoint must be called `/counters`.
- When creating a counter, you must specify the name in the path.
- Duplicate names must return a conflict error code.
- The service must be able to update a counter by name.
- The service must be able to get a counter's current value.
- The service must be able to delete a counter.
"""
from unittest import TestCase
from counter import app
import status

class TestCounters(TestCase):
    """Counter Test Suite"""

    def setUp(self):
        self.client = app.test_client()

    def test_create_counter(self):
        """It should create a counter"""
        response = self.client.post("/counters/foo")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = response.get_json()
        self.assertEqual(data["name"], "foo")
        self.assertEqual(data["count"], 0)

    def test_duplicate_counter(self):
        """It should not create a duplicate counter"""
        response = self.client.post("/counters/bar")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post("/counters/bar")
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    
    def test_update_counter(self):
        """The service must be able to update a counter by name."""
        response = self.client.put("/counters/hello")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response = self.client.put("/counters/foo")
        data = response.get_json()
        self.assertEqual(data["name"], "foo")
        self.assertEqual(data["count"], 1)

    def test_read_counter(self):
        """The service must be able to get a counter's current value."""
        response = self.client.get("/counters/hello")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response = self.client.get("/counters/foo")
        data = response.get_json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["count"], 0)

    def test_delete_counter(self):
        """The service must be able to delete a counter"""
        response = self.client.delete("/counters/dummy")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response = self.client.post("/counters/dummy")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.delete("/counters/dummy")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
