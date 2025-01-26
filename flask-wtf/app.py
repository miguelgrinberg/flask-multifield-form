from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField, FormField, FieldList, \
    SubmitField
from wtforms.validators import DataRequired, Regexp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class PhoneForm(FlaskForm):
    class Meta:
        csrf = False  # no need to use CSRF here, since this is a sub-form
    number = StringField('Phone number', validators=[
        DataRequired(),
        Regexp(r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$',
               message='Enter a valid phone number.')
    ])
    type_ = SelectField('Phone type', choices=[
        ('home', 'Home'),
        ('work', 'Work'),
        ('mobile', 'Mobile'),
        ('other', 'Other')
    ])


class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone_numbers = FieldList(FormField(PhoneForm), min_entries=1)
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        print(f'Name: {form.name.data}')
        for phone in form.phone_numbers.data:
            print(f'Phone: {phone["number"]} ({phone["type_"]})')
    return render_template('index.html', form=form)
