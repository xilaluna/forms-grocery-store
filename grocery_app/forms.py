from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, MacAddress, URL
from grocery_app import ItemCategory, GroceryStore


class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""
    title = StringField('Store Name', validators=[DataRequired()])
    address = StringField('Address')
    submit = SubmitField('Submit')


class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    name = StringField('Item Name')
    price = FloatField('Price')
    category = SelectField('Category', choices=ItemCategory.choices())
    photo_url = StringField('Photo', validators=[URL()])
    store = QuerySelectField(
        'Store Name', query_factory=lambda: GroceryStore.query)
    submit = SubmitField('Submit')
