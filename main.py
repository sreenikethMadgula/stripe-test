from fastapi import FastAPI, Request
from pydantic import BaseModel

import stripe
stripe.api_key = "sk_test_51N3Dp4SIO4953zVXM3CY7RKk9yaZTg9M2dDSXq3eq4JrpH6OVb5a4ht45vib8iy3dn7Xlv1sZDvkS0lFdmNDdm5a00VFqECsyG"


class PaymentIntent(BaseModel):
    amount: int
    currency: str

class Product(BaseModel):
    name: str
    default_price_data: dict = None

class PaymentLink(BaseModel):
    line_items: list[dict]
    


app = FastAPI()


endpoint_secret = 'whsec_71LeISgk4Jqge7rfFOASVxIM6bTmqqiz'


@app.get("/")
def home():
    return {
        "Hello": "world"
    }

@app.post('/create-payment-intent')
def create_payment_intent(pi: PaymentIntent):
    payment_intent = stripe.PaymentIntent.create(
        amount = pi.amount,
        currency = pi.  currency,
        payment_method_types = ['card']
    )
    return {
        "client_secret": payment_intent.client_secret
    }


@app.post('/product')
def create_product(prod: Product):
    product = stripe.Product.create(
        name= prod.name,
        default_price_data = prod.default_price_data
    )
    return {
        "data": product
    }

@app.get('/product')
def get_all_products():
    products = stripe.Product.list()
    return {
        "data" : products
    }

@app.get('/product/{id}')
def get_product_by_id(id: str):
    return {
        "data": stripe.Product.retrieve(id)
    }

@app.get('/price')
def get_all_prices():
    prices = stripe.Price.list()
    return {
        "data": prices
    }

@app.get('/price/{id}')
def get_price_by_id(id: str):
    price = stripe.Price.retrieve(id)
    return {
        "data": price
    }

@app.post('/payment-link')
def create_payment_link(pl: PaymentLink):
    payment_link = stripe.PaymentLink.create(
        line_items = pl.line_items
    )
    return {
        "data": payment_link
    }

@app.get('/payment-link')
def get_all_payment_links():
    payment_links = stripe.PaymentLink.list()
    return {
        "data": payment_links
    }



@app.post('/webhook')
async def webhook(request: Request):
    event = None
    payload = await request.body()
    sig_header = request.headers.get('stripe-signature', None)

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        raise e
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        raise e
    
    event_type = event["type"]

    if event_type == "payment_intent.created":
        print("\n\n\nPayemnt Created!!")
        payment_intent = event.data.object
        print("payment_intent",payment_intent)

    if event_type == 'payment_intent.succeeded':
        print("\n\n\nPayment Succeeded!!")
        payment_intent = event.data.object
        print("payment_intent", payment_intent)


    # Handle the event
    else:
        print('Unhandled event type {}'.format(event['type']))

    return {
        "success": True,
        "event": event
    }

