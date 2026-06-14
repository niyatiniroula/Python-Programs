#Niyati Niroula
from discount import final_price, TAX_RATE

products = [
    ("Laptop", 85000, 10),
    ("Headphones", 4500, 15),
    ("Phone Case", 800, 5),
    ("USB Cable", 600, 0),
]

print(f"TAX_RATE imported: {TAX_RATE}")
print()
print(f"{'Product':<15} {'Original':>10} {'Final Price':>12}")
print("-" * 40)
for name, price, discount in products:
    fp = final_price(price, discount)
    print(f"{name:<15} NPR {price:>6} NPR {fp:>9.2f}")
