num_espressos = int(input(""))
num_lattes = int(input(""))
num_muffins = int(input(""))

price_per_espresso = int(input(""))
price_per_latte = int(input(""))
price_per_muffin = int(input(""))

total_cost = (num_espressos * price_per_espresso) + (num_lattes * price_per_latte) + (num_muffins * price_per_muffin)

print(total_cost)
