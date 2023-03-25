from flask import Flask, render_template, redirect
import requests


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    # import requests
    import smtplib

    # Message Sending
    sender = ""
    receiver = ""
    message = ""

    try:
        smtpOb = smtplib.SMTP("localhost")
        smtpOb.sendmail(sender, receiver, message)

    except:
        pass

    # Exchange Rates
    url = 'https://v6.exchangerate-api.com/v6/3ecd59b7db3f7dc7a433a2b7/latest/USD'
    response = requests.get(url)

    result = response.json()
    rates = result["conversion_rates"]

    return render_template("index.html", rates=rates)