#Question 1. Calculate the total prive avearge for all products
products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"] 
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35] 
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

total_price = sum(prices) 
average_price = total_price / len(prices)
print("Total Price:", total_price) 
print("Average Price:", average_price)

#Question 2. Create a new price list that reduces the old prices by $5
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35] 
new_prices = [price - 5 for price in prices]

products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

new_prices = [price - 5 for price in prices]
print("Product\t\t\tOld Price\tNew Price")
print("-----------------------------------------------")
for i in range(len(products)):
    print(f"{products[i]}\t${prices[i]}\t\t${new_prices[i]}")

#Question 3. Calculate the total revenue genearted from the products
total_revenue = 0

for i in range(len(products)):
    revenue = prices[i] * last_week[i]
    total_revenue += revenue

print("Total revenue generated: $", total_revenue)

#Question 4. Calculate the avearge revenue genearted from the products
total_revenue = 0
for i in range(len(products)):
    daily_revenue = prices[i] * last_week[i]
    total_revenue += daily_revenue

average_daily_revenue = total_revenue / len(last_week)
print("Average daily revenue:", average_daily_revenue)

#Question 5. based on the new prices, which products are less than $30

# Calculate new prices
new_prices = [price - last_week[i] for i, price in enumerate(prices)]

# Find products with prices less than $30
less_than_30 = [product for product, price in zip(products, new_prices) if price < 30]

print("Products with prices less than $30:")
for product in less_than_30:
    print(product)




