import stripe


# set api key globally
stripe.api_key = "sk_test_51N3Dp4SIO4953zVXM3CY7RKk9yaZTg9M2dDSXq3eq4JrpH6OVb5a4ht45vib8iy3dn7Xlv1sZDvkS0lFdmNDdm5a00VFqECsyG"

# # create customer no params
# customer = stripe.Customer.create()
# print(customer)


# # retrieve 
# # /v1/customer/:customer_id
# customer = stripe.Customer.retrieve(id="cus_NpEfZQUY3wHXKs")
# print(customer)


# # create customer with kwargs
# customer = stripe.Customer.create(
#     name = "raja",
#     email = 'raja@gmail.com'
# )

# print(customer)


# create payment intent
# payment_intent = stripe.PaymentIntent.create(
#     amount="10000",
#     currency='inr'
# )
# print(payment_intent.id, payment_intent.status)

# confirm a payment intent

payment_intent = stripe.PaymentIntent.confirm(
    'pi_3N3aNRSIO4953zVX0Thqq4B4',
    payment_method='pm_card_visa'
)

print(payment_intent.id, payment_intent.status)