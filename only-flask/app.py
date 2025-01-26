from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(f'Name: {request.form["name"]}')
        for number, type_ in zip(
            request.form.getlist('phone_number'),
            request.form.getlist('phone_type')
        ):
            if number:
                print(f'Phone number: {number} ({type_})')
    return render_template('index.html')
