from reportlab.pdfgen import canvas

menu = {
    "Pizza": 40,
    "Pasta": 50,
    "Burger": 60,
    "Salad": 70,
    "Coffee": 80
}

orders = []
order_total = 0

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

# Create PDF
c = canvas.Canvas("Restaurant_Bill.pdf")
c.setFont("Helvetica", 14)

c.drawString(50, 800, "PYTHON RESTAURANT - BILL")
c.drawString(50, 770, f"Items: {', '.join(orders)}")
c.drawString(50, 740, f"Total: Rs {order_total}")
c.drawString(50, 710, f"GST (5%): Rs {gst:.2f}")
c.drawString(50, 680, f"Final Amount: Rs {final_amount:.2f}")

c.save()

print("PDF Generated: Restaurant_Bill.pdf")