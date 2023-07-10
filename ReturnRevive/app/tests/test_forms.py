```python
import unittest
from app.main.forms import ReturnForm, SwapForm, MarketplaceForm, ChallengeForm

class TestForms(unittest.TestCase):

    def test_return_form(self):
        form = ReturnForm()
        self.assertFalse(form.validate_on_submit())

    def test_swap_form(self):
        form = SwapForm()
        self.assertFalse(form.validate_on_submit())

    def test_marketplace_form(self):
        form = MarketplaceForm()
        self.assertFalse(form.validate_on_submit())

    def test_challenge_form(self):
        form = ChallengeForm()
        self.assertFalse(form.validate_on_submit())

if __name__ == "__main__":
    unittest.main()
```