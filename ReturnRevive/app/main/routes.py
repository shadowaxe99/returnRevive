```python
from flask import render_template, redirect, url_for, flash, request
from . import main
from .forms import ReturnForm, SwapForm, ItemForm, ChallengeForm
from .models import User, Item, Swap, Challenge, Impact
from .. import db

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/returns', methods=['GET', 'POST'])
def returns():
    form = ReturnForm()
    if form.validate_on_submit():
        # process return and gamification logic here
        flash('Return processed successfully.')
        return redirect(url_for('main.index'))
    return render_template('returns.html', form=form)

@main.route('/style_swap', methods=['GET', 'POST'])
def style_swap():
    form = SwapForm()
    if form.validate_on_submit():
        # process swap logic here
        flash('Swap request sent successfully.')
        return redirect(url_for('main.index'))
    return render_template('style_swap.html', form=form)

@main.route('/marketplace', methods=['GET', 'POST'])
def marketplace():
    form = ItemForm()
    if form.validate_on_submit():
        # process item listing logic here
        flash('Item listed successfully.')
        return redirect(url_for('main.index'))
    return render_template('marketplace.html', form=form)

@main.route('/challenges', methods=['GET', 'POST'])
def challenges():
    form = ChallengeForm()
    if form.validate_on_submit():
        # process challenge participation logic here
        flash('Challenge entry submitted successfully.')
        return redirect(url_for('main.index'))
    return render_template('challenges.html', form=form)

@main.route('/impact_tracker')
def impact_tracker():
    # fetch impact data here
    impact_data = Impact.query.all()
    return render_template('impact_tracker.html', impact_data=impact_data)
```