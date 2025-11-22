import tkinter as tk
from tkinter import ttk
import sqlite3
import os
# Path to the SQLite database (same directory as the script)
db_path = os.path.join(os.path.dirname(__file__), "stock_data.db")

# Function to fetch and display data for the selected stock
def display_data():
    """
    Fetches and displays data for the selected stock from the SQLite database.
    Populates the Treeview with the fetched records.
    """
    # Clear any existing data in the Treeview
    for row in tree.get_children():
        tree.delete(row)

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get the selected stock from the dropdown
    selected_stock = stock_var.get()

    # Fetch data for the selected stock
    cursor.execute("SELECT stock_name, price, timestamp FROM stock_prices WHERE stock_name = ? ORDER BY id DESC", (selected_stock,))
    records = cursor.fetchall()
    conn.close()

    # Populate the Treeview with fetched data
    for record in records:
        tree.insert("", tk.END, values=record)

# Function to populate the dropdown with unique stock names from the database
def populate_dropdown():
    """
    Populates the stock selection dropdown with unique stock names
    from the SQLite database.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch unique stock names from the database
    cursor.execute("SELECT DISTINCT stock_name FROM stock_prices")
    stocks = cursor.fetchall()
    conn.close()

    # Update the dropdown with stock names
    stock_names = [stock[0] for stock in stocks]
    stock_var.set(stock_names[0] if stock_names else "No Data")
    stock_dropdown['values'] = stock_names

# Tkinter window setup
root = tk.Tk()
root.title("plus2net.com View Stored Stock Data")
root.geometry("800x400")

# Title label
title_label = tk.Label(root, text="Stored Stock Data", font=("Arial", 16, "bold"), fg="#007bff")
title_label.pack(pady=10)

# Frame for dropdown and button
selection_frame = tk.Frame(root)
selection_frame.pack(pady=10)

# Dropdown to select stock
stock_var = tk.StringVar()
stock_dropdown = ttk.Combobox(selection_frame, textvariable=stock_var, state="readonly", font=("Arial", 12))
stock_dropdown.pack(side=tk.LEFT, padx=5)

# Button to fetch and display data
fetch_button = tk.Button(selection_frame, text="Load Data", command=display_data, font=("Arial", 12))
fetch_button.pack(side=tk.LEFT, padx=5)

# Treeview widget to display stored data
columns = ("Stock Name", "Price", "Timestamp")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("Stock Name", text="Stock Name")
tree.heading("Price", text="Price")
tree.heading("Timestamp", text="Timestamp")
tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Set column widths
tree.column("Stock Name", width=200)
tree.column("Price", width=100)
tree.column("Timestamp", width=200)

# Populate the dropdown with stock names on startup
populate_dropdown()

# Run the Tkinter event loop
root.mainloop()


