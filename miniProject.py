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

def formatPrinter(product):
    print(f"Category: {product["category"]} \nOriginal Price: $1200.0 \nDiscount: 20% \nFinal Price: ${product["price"]}", end="\n")
    print("===")

# process
for pro in products:
    if pro["category"] == "Electronics":
        if pro["price"] >= 1000:
            pro["price"] = pro["price"] * 0.8
        elif 500 <= pro["price"] < 1000:
            pro["price"] = pro["price"] * 0.85
        elif pro["price"] < 500:
            pro["price"] = pro["price"] * 0.9
    elif pro["category"] == "Clothing":
        if pro["price"] >= 100:
            pro["price"] = pro["price"] * 0.75
        else:
            pro["price"] = pro["price"] * 0.85

    # formatPrinter(pro)







