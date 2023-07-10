```python
import unittest
from app.main.models import User, Item, Swap, Challenge, Impact
from app import create_app, db

class TestModels(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_model(self):
        user = User(username='test', email='test@example.com')
        db.session.add(user)
        db.session.commit()
        self.assertEqual(User.query.count(), 1)

    def test_item_model(self):
        item = Item(name='test_item', description='test_description', price=100)
        db.session.add(item)
        db.session.commit()
        self.assertEqual(Item.query.count(), 1)

    def test_swap_model(self):
        swap = Swap(requester_id=1, requested_id=2, item_id=1, status='pending')
        db.session.add(swap)
        db.session.commit()
        self.assertEqual(Swap.query.count(), 1)

    def test_challenge_model(self):
        challenge = Challenge(name='test_challenge', description='test_description')
        db.session.add(challenge)
        db.session.commit()
        self.assertEqual(Challenge.query.count(), 1)

    def test_impact_model(self):
        impact = Impact(user_id=1, carbon_saved=10, waste_reduced=5, swaps_made=2)
        db.session.add(impact)
        db.session.commit()
        self.assertEqual(Impact.query.count(), 1)

if __name__ == '__main__':
    unittest.main()
```