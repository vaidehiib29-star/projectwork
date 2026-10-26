
"""
Project Name: Bookstore Inventory and Data Analytics System

Description:
This project manages bookstore inventory, adds new books, updates stock,
records book sales, generates sales reports, and displays charts.

Required libraries:
    pandas
    numpy
    matplotlib
    seaborn

Required CSV files:
    inventory.csv
    sales.csv

Both CSV files are created automatically if they do not exist.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
                                            

class Bookstore:
    """Manage book inventory, sales, reports, and charts."""

    def __init__(self):
        """Initialize the CSV files and load the data."""

        self.inventory_file = "inventory.csv"
        self.sales_file = "sales.csv"

        self.inventory_columns = [
            "Title", "Author", "Genre", "Price", "Quantity"
        ]

        self.sales_columns = [
            "Date", "Title", "Quantity Sold", "Total Revenue"
        ]

        self.load_data()

    def load_data(self):
        """Create missing CSV files and load existing data."""

        # Create inventory file if it does not exist
        if not os.path.exists(self.inventory_file):
            pd.DataFrame(columns=self.inventory_columns).to_csv(
                self.inventory_file, index=False
            )

        # Create sales file if it does not exist
        if not os.path.exists(self.sales_file):
            pd.DataFrame(columns=self.sales_columns).to_csv(
                self.sales_file, index=False
            )

        # Read the CSV files
        self.inventory = pd.read_csv(self.inventory_file)
        self.sales = pd.read_csv(self.sales_file)

        # Check required columns
        if list(self.inventory.columns) != self.inventory_columns:
            if not all(c in self.inventory.columns
                    for c in self.inventory_columns):
                raise ValueError("Invalid columns in inventory.csv")

        if not all(c in self.sales.columns for c in self.sales_columns):
            raise ValueError("Invalid columns in sales.csv")

        # Convert inventory data types
        self.inventory["Price"] = pd.to_numeric(
            self.inventory["Price"], errors="coerce"
        )
        self.inventory["Quantity"] = pd.to_numeric(
            self.inventory["Quantity"], errors="coerce"
        )

        # Remove invalid inventory records
        self.inventory.dropna(
            subset=self.inventory_columns, inplace=True
        )
        self.inventory = self.inventory[
            (self.inventory["Price"] > 0)
            & (self.inventory["Quantity"] >= 0)
            & (self.inventory["Quantity"] % 1 == 0)
        ].copy()

        self.inventory["Price"] = self.inventory["Price"].astype(float)
        self.inventory["Quantity"] = self.inventory["Quantity"].astype(int)

        # Convert sales data types
        self.sales["Date"] = pd.to_datetime(
            self.sales["Date"], errors="coerce"
        )
        self.sales["Quantity Sold"] = pd.to_numeric(
            self.sales["Quantity Sold"], errors="coerce"
        )
        self.sales["Total Revenue"] = pd.to_numeric(
            self.sales["Total Revenue"], errors="coerce"
        )

        # Remove invalid sales records
        self.sales.dropna(subset=self.sales_columns, inplace=True)
        self.sales = self.sales[
            (self.sales["Quantity Sold"] > 0)
            & (self.sales["Quantity Sold"] % 1 == 0)
            & (self.sales["Total Revenue"] >= 0)
        ].copy()

        self.sales["Quantity Sold"] = (
            self.sales["Quantity Sold"].astype(int)
        )

        # Save the cleaned data
        self.inventory.to_csv(self.inventory_file, index=False)
        self.sales.to_csv(self.sales_file, index=False)

    def show_books(self):
        """Display all books currently available in inventory."""

        print("\n--- Book Inventory ---")

        if self.inventory.empty:
            print("No books available.")
        else:
            print(self.inventory.to_string(index=False))

    def add_book(self):
        """Add a new book with its price and quantity."""

        print("\n--- Add New Book ---")

        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        genre = input("Enter book genre: ").strip()

        if not title or not author or not genre:
            print("Please enter all book details.")
            return

        try:
            price = float(input("Enter book price: "))
            quantity = int(input("Enter quantity: "))

            if not np.isfinite(price) or price <= 0:
                print("Price must be a positive number.")
                return

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                return

        except ValueError:
            print("Please enter a valid price and quantity.")
            return

        # Prevent duplicate book titles
        existing = self.inventory["Title"].str.casefold().eq(
            title.casefold()
        )

        if existing.any():
            print("This book already exists.")
            return

        new_book = {
            "Title": title,
            "Author": author,
            "Genre": genre,
            "Price": price,
            "Quantity": quantity
        }

        self.inventory.loc[len(self.inventory)] = new_book
        self.inventory.to_csv(self.inventory_file, index=False)

        print("Book added successfully!")

    def update_stock(self):
        """Change the available quantity of an existing book."""

        print("\n--- Update Stock ---")
        title = input("Enter book title: ").strip()

        found = self.inventory["Title"].str.casefold().eq(
            title.casefold()
        )

        if not found.any():
            print("Book not found.")
            return

        try:
            quantity = int(input("Enter new quantity: "))

            if quantity < 0:
                print("Quantity cannot be negative.")
                return

        except ValueError:
            print("Please enter a valid whole number.")
            return

        self.inventory.loc[found, "Quantity"] = quantity
        self.inventory.to_csv(self.inventory_file, index=False)

        print("Stock updated successfully!")

    def sell_book(self):
        """Sell books, update stock, and record the sale."""

        print("\n--- Sell Book ---")
        title = input("Enter book title: ").strip()

        found = self.inventory["Title"].str.casefold().eq(
            title.casefold()
        )

        if not found.any():
            print("Book not found.")
            return

        try:
            quantity = int(input("Enter quantity sold: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                return

        except ValueError:
            print("Please enter a valid whole number.")
            return

        index = self.inventory.index[found][0]
        stock = int(self.inventory.loc[index, "Quantity"])
        price = float(self.inventory.loc[index, "Price"])

        if quantity > stock:
            print("Not enough books in stock.")
            return

        # Enter a date or press Enter to use today's date
        date_text = input(
            "Enter sale date (YYYY-MM-DD) or press Enter for today: "
        ).strip()

        if date_text == "":
            sale_date = pd.Timestamp.today().normalize()
        else:
            try:
                sale_date = pd.to_datetime(
                    date_text, format="%Y-%m-%d", errors="raise"
                )
            except ValueError:
                print("Invalid date. Use YYYY-MM-DD.")
                return

        revenue = price * quantity

        sale = {
            "Date": sale_date,
            "Title": self.inventory.loc[index, "Title"],
            "Quantity Sold": quantity,
            "Total Revenue": revenue
        }

        # Update stock and save both files
        self.inventory.loc[index, "Quantity"] = stock - quantity
        self.sales.loc[len(self.sales)] = sale

        try:
            self.inventory.to_csv(self.inventory_file, index=False)
            self.sales.to_csv(self.sales_file, index=False)

        except OSError as error:
            # Restore the original in-memory data if saving fails
            self.inventory.loc[index, "Quantity"] = stock
            self.sales.drop(self.sales.index[-1], inplace=True)
            print("Could not save the sale:", error)
            return

        print("Sale recorded successfully!")
        print(f"Book: {sale['Title']}")
        print(f"Quantity sold: {quantity}")
        print(f"Total revenue: Rs. {revenue:.2f}")

    def report(self):
        """Display total sales, revenue, and best-selling books."""

        print("\n--- Sales Report ---")

        if self.sales.empty:
            print("No sales data available.")
            return

        quantities = self.sales["Quantity Sold"].to_numpy()
        revenues = self.sales["Total Revenue"].to_numpy()

        print(f"Total books sold: {np.sum(quantities)}")
        print(f"Total revenue: Rs. {np.sum(revenues):.2f}")
        print(f"Average sale revenue: Rs. {np.mean(revenues):.2f}")

        best = self.sales.groupby("Title")["Quantity Sold"].sum()
        highest = best.max()

        print("Best-selling book(s):")
        print(best[best == highest].to_string())

        print("\nRevenue by book:")
        print(
            self.sales.groupby("Title")["Total Revenue"]
            .sum().sort_values(ascending=False).to_string()
        )

    def charts(self):
        """Display sales charts using Matplotlib and Seaborn."""

        if self.sales.empty:
            print("No sales data available for charts.")
            return

        data = self.sales.copy()

        # Add genre information to sales
        genre_data = self.inventory[["Title", "Genre"]].drop_duplicates(
            subset=["Title"]
        )
        data = data.merge(genre_data, on="Title", how="left")

        # Chart 1: Books sold
        data.groupby("Title")["Quantity Sold"].sum().plot(
            kind="bar", figsize=(8, 5)
        )
        plt.title("Books Sold")
        plt.xlabel("Book Title")
        plt.ylabel("Quantity Sold")
        plt.tight_layout()
        plt.show()

        # Chart 2: Monthly revenue
        data["Month"] = data["Date"].dt.to_period("M").astype(str)

        data.groupby("Month")["Total Revenue"].sum().plot(
            kind="line", marker="o", figsize=(8, 5)
        )
        plt.title("Monthly Sales Revenue")
        plt.xlabel("Month")
        plt.ylabel("Revenue (Rs.)")
        plt.tight_layout()
        plt.show()

        # Chart 3: Revenue by genre
        genre_revenue = data.groupby("Genre")["Total Revenue"].sum()
        genre_revenue = genre_revenue.dropna()

        if not genre_revenue.empty and genre_revenue.sum() > 0:
            genre_revenue.plot(
                kind="pie", autopct="%1.1f%%", figsize=(7, 7)
            )
            plt.title("Revenue Share by Genre")
            plt.ylabel("")
            plt.tight_layout()
            plt.show()
        else:
            print("Genre revenue chart is not available.")

        # Chart 4: Correlation heatmap
        correlation = data[
            ["Quantity Sold", "Total Revenue"]
        ].corr()

        plt.figure(figsize=(6, 4))
        sns.heatmap(correlation, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
        plt.title("Sales Quantity and Revenue Correlation")
        plt.tight_layout()
        plt.show()

    def menu(self):
        """Display the main menu until the user chooses Exit."""

        while True:
            print("\n====== BOOKSTORE MENU ======")
            print("1. Show Books")
            print("2. Add Book")
            print("3. Update Stock")
            print("4. Sell Book")
            print("5. Sales Report")
            print("6. Show Charts")
            print("7. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.show_books()

            elif choice == "2":
                self.add_book()

            elif choice == "3":
                self.update_stock()

            elif choice == "4":
                self.sell_book()

            elif choice == "5":
                self.report()

            elif choice == "6":
                self.charts()

            elif choice == "7":
                print("Thank you for using Bookstore System!")
                break

            else:
                print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    try:
        bookstore = Bookstore()
        bookstore.menu()

    except (OSError, ValueError, pd.errors.ParserError) as error:
        print("Could not start the bookstore system:", error)
