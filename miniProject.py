products = [
{"name": "Laptop", "price": 1200, "category": "Electronics"},
{"name": "Shirt", "price": 45, "category": "Clothing"},
{"name": "Phone", "price": 800, "category": "Electronics"},
{"name": "Shoes", "price": 120, "category": "Clothing"},
{"name": "Tablet", "price": 350, "category": "Electronics"},
{"name": "Jacket", "price": 95, "category": "Clothing"},
{"name": "Book", "price": 25, "category": "Books"},
{"name": "Headphones", "price": 150, "category": "Electronics"}
]

# display product info
print("=== PRODUCT DISCOUNT CALCULATOR ===")
def printer(product):
    print(
    f"Product: {product['name']}\n"
    f"  Category: {product['category']}\n"
    f"  Original Price: ${product['price']}\n"
    f"  Discount: {product['discountRate']}%\n"
    f"  Final Price: ${product['newPrice']}\n"
    )

# process
totalOriginal = 0
totalDiscount = 0.0
discountRate = 0.0
newPrice = 0.0
countProduct = 0

# bonus
highestDiscount = 0.0
highestDiscountedProduct = products[0]
cheapestPrice = products[0]["price"]
cheapestProduct = products[0]
highestPrice = 0
highestProduct = products[0]

categoryCounter = {}
def countCategories(cate):
    if cate not in categoryCounter:
        categoryCounter[cate] = 1
    else:
        categoryCounter[cate] += 1

for pro in products:
    totalOriginal += pro["price"]
    countCategories(pro["category"]) # bonus
    if pro["category"] == "Electronics":
        if pro["price"] >= 1000:
            discountRate = 0.2
        elif 500 <= pro["price"] < 1000:
            discountRate = 0.15
        else:
            discountRate = 0.1
    elif pro["category"] == "Clothing":
        if pro["price"] >= 100:
            discountRate = 0.25
        else:
            discountRate = 0.15
    elif pro["category"] == "Books":
        discountRate = 0.1

    pro["newPrice"] = pro["price"] * (1-discountRate)
    pro["discountRate"] = int(discountRate * 100)

    discount = pro["price"] * discountRate
    countProduct += 1
    totalDiscount += discount

    # bonus
    if(highestDiscount < discount):
        highestDiscount = discount
        highestDiscountedProduct = pro

    if(cheapestPrice > pro["newPrice"]):
        cheapestPrice = pro["newPrice"]
        cheapestProduct = pro

    if(highestPrice < pro["newPrice"]):
        highestPrice = pro["newPrice"]
        highestProduct = pro

    printer(pro)

# display summary
print("=== SUMMARY ===")
print(
    f"Total products: {countProduct}\n"
    f"Total original price: ${totalOriginal}\n"
    f"Total discount: ${totalDiscount}\n"
    f"Total final price: ${totalOriginal - totalDiscount}"
    )

# bonus
print("=========")
print(f"Average discount: {totalDiscount/countProduct}")
print(f"Product with the highest discount: {highestDiscountedProduct["name"]}, with ${highestDiscount}")
print(f"Product with the highest price after discount: {highestProduct["name"]}, at ${highestProduct["newPrice"]}")
print(f"Product with the lowest price after discount: {cheapestProduct["name"]}, at ${cheapestProduct["newPrice"]}")
print("=========")
for c in categoryCounter:
    print(f"Category: {c}, number of products: {categoryCounter[c]}")



