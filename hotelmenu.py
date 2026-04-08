print("===== Welcome to PYTHON Restaurant =====")

menu = {
    "Pizza": 40,
    "Pasta": 50,
    "Burger": 60,
    "Salad": 70,
    "Coffee": 80
}

print("\n------ MENU ------")
for item, price in menu.items():
    print(f"{item}: Rs {price}")
print("------------------\n")

order_total = 0
orders = []

while True:
    item = input("Enter the item you want to order: ")

    if item in menu:
        order_total += menu[item]
        orders.append(item)
        print(f"{item} added to your order.")
    else:
        print(f"Sorry! {item} is not available.")

    more = input("Do you want to add another item? (Yes/No): ").lower()
    if more != "yes":
        break

print("\nGenerating your bill...")

gst = order_total * 0.05
final_amount = order_total + gst

print("\n----- BILL -----")
print("Items Ordered:", ", ".join(orders))
print(f"Total Amount: Rs {order_total}")
print(f"GST (5%): Rs {gst:.2f}")
print(f"Final Amount to Pay: Rs {final_amount:.2f}")
print("----------------")
print("Thank you for visiting PYTHON Restaurant 😊")
