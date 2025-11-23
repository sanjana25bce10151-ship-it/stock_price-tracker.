# stock_price-tracker.

#STOCK DATA VIEWER-

(Tkinter + SQLite)This project is a simple desktop application built with Python, Tkinter, and SQLite to view stored stock price data.
It allows the user to select a stock from a dropdown and display all saved records for that stock in a table-like Treeview widget.FeaturesGUI built using Tkinter.Uses SQLite as a lightweight local database (stock_data.db).Dropdown (combobox) to select any available stock symbol/name from the database.“Load Data” button to fetch and display rows for the selected stock.Tabular display using ttk.Treeview (columns: Stock Name, Price, Timestamp).Automatically loads available stock names into the dropdown at startup.

#HOW IT WORKS-

On startup, the app connects to stock_data.db and runs SELECT DISTINCT stock_name FROM stock_prices to get all unique stock names.
These names are placed in the ttk.Combobox so the user can choose which stock to view.
When the user clicks “Load Data”, the app:
  Clears the existing rows from the Treeview.
  Runs SELECT stock_name, price, timestamp FROM stock_prices WHERE stock_name = ? ORDER BY id DESC.
  Inserts each returned record as a row in the Treeview.
  
#REQUIREMENTS-

  -Standard library modules:
     tkinter
     tkinter.ttk
     sqlite3
     os
  -An existing SQLite database file named stock_data.db in the same directory, containing a stock_prices table with appropriate columns.

#CODE OVERVIEW -

 -display_data()
    Reads the selected stock from the combobox.
    Connects to SQLite, fetches matching rows, clears existing Treeview items, and inserts the new ones.
 -populate_dropdown()
    Connects to SQLite and fetches all distinct stock names.
    Fills the combobox and sets the initial selection.
 -Tkinter setup:
    Creates the root window with title and size.
    Adds a title label, a frame for the dropdown and button, and the Treeview widget.
    Configures Treeview columns and headings.
    Calls populate_dropdown() once at startup.
