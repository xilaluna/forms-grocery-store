from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, MacAddress, URL
from grocery_app import ItemCategory


class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""
    title = StringField('Store Name', validators=[DataRequired()])
    address = StringField('Address')
    submit = SubmitField('Submit')

    # TODO: Add the following fields to the form class:
    # - title - StringField
    # - address - StringField
    # - submit button


class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    name = StringField('Item Name')
    price = FloatField('Price')
    category = SelectField('Category', choices=ItemCategory.choices())

    # TODO: Add the following fields to the form class:
    # - name - StringField
    # - price - FloatField
    # - category - SelectField (specify the 'choices' param)
    # - photo_url - StringField (use a URL validator)
    # - store - QuerySelectField (specify the `query_factory` param)
    # - submit button
    pass
