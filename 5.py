prices = [57.8, 46.51, 97, 41, 13, 55.32, 123.5, 34, 11.4, 123, 44.3]

new_list = []
for price in prices:
    roubles = int(price)
    kop = round((price  - roubles) * 100)
    new_list.append(f"{roubles} руб {kop} коп")
print(", ".join(new_list))
id1 = id(prices)
prices.sort()
print(prices)
print(id(prices) == id1)
my_list = sorted(prices, reverse=True)
print(sorted(my_list[:5]))

