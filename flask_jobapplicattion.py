# content="width=device-width, initial-scale=1, shrink-to-fit=no":

# `width=device-width`: This sets the width of the webpage to match the width of the device's screen. This ensures that
# the page is laid out correctly on devices with different screen sizes.

# `shrink-to-fit=no`: This is an optional setting that tells the browser not to shrink the page to fit the screen size
# if the device has a high-resolution display. This is useful for newer devices with high pixel density, where you want
# the page to be displayed at its normal size rather than being zoomed out.
from flask import Flask, render_template, request, flash, redirect, url_for
# pip install flask-sqlalchemy or here
from flask_sqlalchemy import SQLAlchemy
# pip install flask-mail
from flask_mail import Mail, Message
from datetime import datetime
from os import getenv

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ABCDEFGHIJKLMNOPQRSTUXZ123456789#*'  # Com isto, vai proteger dos hackers, etc.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'portfoliowebsitepython@gmail.com'
app.config['MAIL_PASSWORD'] = getenv('PASSWORD_PORTFOLIO_WEBSITE')

db = SQLAlchemy(app)

mail = Mail(app)


class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        first_name = request.form['first_name'].title().strip()
        last_name = request.form['last_name'].title().strip()
        email = request.form['email']
        date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        occupation = request.form['occupation']

        form = Form(first_name=first_name, last_name=last_name, email=email, date=date, occupation=occupation)
        db.session.add(form)
        db.session.commit()

        message_body = (f'Thank you for your submittion, {first_name} {last_name}.\nHere are your data:\n'
                        f'first_name: {first_name}\nlast_name: {last_name}\nemail: {email}\ndate: {date}\n'
                        f'occupation: {occupation}')
        message = Message(subject='New form submission', sender=app.config['MAIL_USERNAME'], recipients=[email],
                          body=message_body)
        mail.send(message)

        flash(f'{first_name}, your form was submitted successfully!', 'success')
        return redirect(url_for("home"))

    return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # create a database file e cria na pasta instance(foi criada quando executei o código)
        app.run(debug=True, port=5001)  # 5001 só porque sim, mas por default é 5000
