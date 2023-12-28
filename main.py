import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

from contact_form import ContactForm
from email_handler import EmailHandler

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "mugiwara")
bootstrap = Bootstrap5(app=app)


@app.route("/")
def home_route():
    """Handles the home route"""
    return render_template("index.html", title="Home")


@app.route("/projects")
def projects_route():
    """Handles the projects route"""
    return render_template("projects.html", title="Projects")


@app.route("/contact", methods=["GET", "POST"])
def contact_route():
    """Handles the contact route"""
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        email_handler = EmailHandler(
            email=os.environ.get("EMAIL", ""),
            password=os.environ.get("PASSWORD", ""),
        )
        email_handler.send_email(contact_form)
        return render_template("contact.html", title="Success")
    return render_template("contact.html", title="Contact", form=contact_form)


if __name__ == "__main__":
    app.run(debug=False)
