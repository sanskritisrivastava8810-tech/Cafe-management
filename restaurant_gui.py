import tkinter as tk
from tkinter import messagebox

menu = {
    "Pizza": 40,
    "Pasta": 50,
    "Burger": 60,
    "Salad": 70,
    "Coffee": 80
}

order_total = 0

def add_item():
    global order_total
    item = entry.get()

    if item in menu:
        order_total += menu[item]
        listbox.insert(tk.END, f"{item} - Rs {menu[item]}")
    else:
        messagebox.showerror("Error", "Item not available")

def show_bill():
    gst = order_total * 0.05
    final_amount = order_total + gst
    messagebox.showinfo("Bill",
        f"Total: Rs {order_total}\nGST: Rs {gst:.2f}\nFinal Amount: Rs {final_amount:.2f}")

root = tk.Tk()
root.title("Restaurant Billing System")
root.geometry("400x400")

label = tk.Label(root, text="Enter Item Name:", font=("Arial", 12))
label.pack()

entry = tk.Entry(root, font=("Arial", 12))
entry.pack()

add_btn = tk.Button(root, text="Add Item", command=add_item)
add_btn.pack()

listbox = tk.Listbox(root, width=50)
listbox.pack()

bill_btn = tk.Button(root, text="Generate Bill", command=show_bill)
bill_btn.pack()

root.mainloop()