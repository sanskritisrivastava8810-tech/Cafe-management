import datetime

menu = {
    "Pizza": 40,
    "Pasta": 50,
    "Burger": 60,
    "Salad": 70,
    "Coffee": 80
}

orders = []
order_total = 0

print("Welcome to PYTHON Restaurant\n")

while True:
    item = input("Enter item: ")

    if item in menu:
        orders.append(item)
        order_total += menu[item]
    else:
        print("Not available")

    more = input("Add more? Yes/No: ").lower()
    if more != "yes":
        break

gst = order_total * 0.05
final_amount = order_total + gst

bill = f"""
===== PYTHON RESTAURANT BILL =====
Items Ordered: {", ".join(orders)}
Total: Rs {order_total}
GST (5%): Rs {gst:.2f}
Final Amount: Rs {final_amount:.2f}
Date: {datetime.datetime.now()}
"""

print(bill)

with open("restaurant_bill.txt", "w") as f:
    f.write(bill)

print("Bill saved as restaurant_bill.txt")