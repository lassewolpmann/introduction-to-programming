meal_price = float(input('How much did the meal cost?: '))
tip = meal_price * 0.15
tax = round((meal_price + tip) * 0.07, 2)

print(f'You paid a tip of {tip}€')
print(f'The tax for the meal is {tax}€')
print(f'Total price: {meal_price + tip + tax}€')
