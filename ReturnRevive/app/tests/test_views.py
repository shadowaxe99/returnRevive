```python
import unittest
from flask import url_for
from ReturnRevive.app import create_app
from ReturnRevive.app.main import views

class TestViews(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def test_home_page(self):
        response = self.client.get(url_for('main.index'))
        self.assertEqual(response.status_code, 200)

    def test_returns_page(self):
        response = self.client.get(url_for('main.returns'))
        self.assertEqual(response.status_code, 200)

    def test_style_swap_page(self):
        response = self.client.get(url_for('main.style_swap'))
        self.assertEqual(response.status_code, 200)

    def test_marketplace_page(self):
        response = self.client.get(url_for('main.marketplace'))
        self.assertEqual(response.status_code, 200)

    def test_challenges_page(self):
        response = self.client.get(url_for('main.challenges'))
        self.assertEqual(response.status_code, 200)

    def test_impact_tracker_page(self):
        response = self.client.get(url_for('main.impact_tracker'))
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
```