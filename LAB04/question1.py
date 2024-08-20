# QUESTION 01
products = [
    {'name': 'Laptop', 'price': 1000, 'stock': 5, 'categories': ['Electronics', 'Computers']},
    {'name': 'Smartphone', 'price': 800, 'stock': 0, 'categories': ['Electronics', 'Phones']},
    {'name': 'Book', 'price': 15, 'stock': 10, 'categories': ['Books']},
    {'name': 'Headphones', 'price': 100, 'stock': 15, 'categories': ['Electronics', 'Audio']},
]

def main():
    # Check if there are any products that are out of stock
    out_of_stock = any(map(lambda x: x['stock'] == 0, products))
    print(f"Any product out of stock: {out_of_stock}")

    # Verify if all products in a specific category are available and have a price greater than a specified threshold δ, where δ is input by users.
    def check_category_availability_and_price(category, delta):
        return all(map(lambda x: x['price'] > delta and x['stock'] > 0, filter(lambda y: category in y['categories'], products)))

    category = input("Enter category: ")
    delta = float(input("Enter price threshold: "))
    category_check = check_category_availability_and_price(category, delta)
    print(f"All products in category '{category}' have a price greater than {delta} and are in stock: {category_check}")

if __name__ == "__main__":
    main()


