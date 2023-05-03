import stripe


# set api key globally
stripe.api_key = "sk_test_51N3Dp4SIO4953zVXM3CY7RKk9yaZTg9M2dDSXq3eq4JrpH6OVb5a4ht45vib8iy3dn7Xlv1sZDvkS0lFdmNDdm5a00VFqECsyG"

print(stripe.Customer.list())

# set api key per request
customers = stripe.Customer.list(api_key="sk_test_51N3Dp4SIO4953zVXM3CY7RKk9yaZTg9M2dDSXq3eq4JrpH6OVb5a4ht45vib8iy3dn7Xlv1sZDvkS0lFdmNDdm5a00VFqECsyG")

