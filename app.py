from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from currency import get_spot_rate, convert, available_currencies

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_ENABLED'] = True

@app.route('/', methods=['GET', 'POST'])
def home():
    currencies = available_currencies()

    if request.method == 'POST':
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        amount = float(request.form['amount'])
        
        if from_currency not in currencies or to_currency not in currencies:
            flash("Invalid currency selected. Please choose valid currencies.", 'error')
            return render_template('converter.html', currencies=currencies)

        exchange_rate = get_spot_rate(from_currency, to_currency)
        converted_amount = convert(amount, exchange_rate)

        return render_template('converter.html', currencies=currencies, from_currency=from_currency, to_currency=to_currency, amount=amount, converted_amount=converted_amount)

    return render_template('converter.html', currencies=currencies)
