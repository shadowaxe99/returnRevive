```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange

class ReturnForm(FlaskForm):
    reason = TextAreaField('Reason for Return', validators=[DataRequired(), Length(min=10, max=500)])
    submit = SubmitField('Submit Return')

class SwapForm(FlaskForm):
    item_id = IntegerField('Item ID', validators=[DataRequired()])
    swap_with = IntegerField('Swap With Item ID', validators=[DataRequired()])
    submit = SubmitField('Submit Swap Request')

class MarketplaceForm(FlaskForm):
    item_name = StringField('Item Name', validators=[DataRequired(), Length(min=2, max=100)])
    item_description = TextAreaField('Item Description', validators=[DataRequired(), Length(min=10, max=500)])
    item_price = IntegerField('Item Price', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('List Item for Sale')

class ChallengeForm(FlaskForm):
    outfit_description = TextAreaField('Outfit Description', validators=[DataRequired(), Length(min=10, max=500)])
    submit = SubmitField('Submit Outfit')

class ImpactForm(FlaskForm):
    carbon_saved = IntegerField('Carbon Emissions Saved', validators=[DataRequired()])
    waste_reduced = IntegerField('Landfill Waste Reduced', validators=[DataRequired()])
    swaps_made = IntegerField('Number of Sustainable Fashion Swaps Made', validators=[DataRequired()])
    submit = SubmitField('Update Impact')
```