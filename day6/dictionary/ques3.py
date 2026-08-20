# 9. Create a dictionary of products with their prices. Write a program to calculate the total price of all products.
products = {
  "Apple": 1.5,
  "Banana": 0.5,
  "Orange": 0.8,
  "Grapes": 2.0,
  "Mango": 1.2
} 
total_price = sum(products.values())
print("Total price of all products:", total_price)