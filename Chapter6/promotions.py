def fidelity_promo(order):
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

def bulk_item_promo(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

def large_order_promo(order):
    distinct_item = {item.product for item in order.cart}
    if len(distinct_item) >= 10:
        return order.total() * .07
    return 0