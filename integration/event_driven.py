from flask import Flask, request
import stripe
from zendesk import Zendesk

app = Flask(__name__)
stripe.api_key = 'stripe_api_key'
zd = Zendesk('https://company.zendesk.com', 'api_user', 'api_token')

@app.route('/stripe-webhook')