rate_of_gold = float(input("Rate of gold (toman): "))
mass = float(input("Mass (g): "))
price = rate_of_gold*mass
making_charge = ((float(input("Making charge (%): ")))/100)*price
sales_profit = ((float(input("Sales profit (%): ")))/100)*(making_charge + price)
tax = (float(input("Tax (%) :"))/100)*(making_charge + sales_profit)
final_price = (price + making_charge + sales_profit + tax)

print("=== Gold Price Calculator ===")
print("Final price: ", final_price, "Toman")
if final_price > 100000000:
    print("Expensive purchase")
else:
    print("Affordable purchase")