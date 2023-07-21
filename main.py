def cost_delivery(quantity, *args, discount=0):
    delivery_cost = 5 + max(quantity - 1, 0) * 2
    total_cost_with_discount = delivery_cost * (1 - discount)
    return total_cost_with_discount

print(cost_delivery(2, 1, 2, 3))
print(cost_delivery(3, 3))
print(cost_delivery(1))
print(cost_delivery(2, 1, 2, 3, discount=0.5)) 