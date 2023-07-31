from flask import Flask, render_template, request, redirect, url_for, flash, session
from currency import get_spot_rate, convert, available_currencies

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_ENABLED'] = False

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        amount = float(request.form['amount'])

        exchange_rate = get_spot_rate(from_currency, to_currency)
        converted_amount = convert(amount, exchange_rate)

        return f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}"

    return render_template('converter.html')

@app.route('/currencies')
def currency_list():
    currencies = available_currencies()
    if currencies:
        print(currencies)
