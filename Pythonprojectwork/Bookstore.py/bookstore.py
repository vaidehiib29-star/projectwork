"""
Project Name: Bookstore Inventory and Data Analytics System

Description:
This project manages bookstore inventory and sales records using CSV files.
It allows users to:
1. Add new books
2. Remove books
3. Update stock quantity
4. Display all books
5. Record book sales
6. Generate sales reports
7. Display charts for data analysis

Libraries Used:
- pandas: To manage CSV files and tabular data.
- numpy: To perform mathematical calculations.
- matplotlib: To create charts.
- seaborn: To create a heatmap.
- os: To check whether CSV files exist.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


class Bookstore:
    """
    This class manages bookstore inventory, sales, reports,
    and data visualizations.
    """

    def __init__(self):
        """
        Constructor:
        Initializes the CSV file names and loads the data.
        """
        self.inventory_file = "inventory.csv"
        self.sales_file = "sales.csv"
        self.load_data()

    def load_data(self):
        """
        Loads inventory and sales data from CSV files.

        Converts price, quantity, date, and revenue columns
        into suitable data types and removes invalid records.
        """
        self.inventory = pd.read_csv(self.inventory_file)
        self.sales = pd.read_csv(self.sales_file)

        # Convert inventory columns to numeric values
        self.inventory["Price"] = pd.to_numeric(self.inventory["Price"], errors="coerce")
        self.inventory["Quantity"] = pd.to_numeric(
            self.inventory["Quantity"], errors="coerce"
        )

        # Remove records containing missing required values
        self.inventory.dropna(
            subset=["Title", "Author", "Genre", "Price", "Quantity"],
            inplace=True
        )

        # Set the correct data types
        self.inventory["Price"] = self.inventory["Price"].astype(float)
        self.inventory["Quantity"] = self.inventory["Quantity"].astype(int)

        # Convert sales columns to suitable data types
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
        self.sales.dropna(
            subset=["Date", "Title", "Quantity Sold", "Total Revenue"],
            inplace=True
        )

        self.sales["Quantity Sold"] = (
            self.sales["Quantity Sold"].astype(int)
        )

        # Save cleaned data back to CSV files
        self.inventory.to_csv(self.inventory_file, index=False)
        self.sales.to_csv(self.sales_file, index=False)

    def add_book(self):
        """
        Adds a new book to the inventory.

        Takes the book title, author, genre, price, and quantity
        from the user and saves the new record to inventory.csv.
        """
        title = input("Enter book title: ").strip()
        author = input("Enter author: ").strip()
        genre = input("Enter genre: ").strip()

        try:
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))

            # Check that book details are not empty
            if not title or not author or not genre:
                print("Book details cannot be empty.")
                return

            # Validate price and quantity
            if price <= 0 or quantity <= 0:
                print("Price and quantity must be positive.")
                return

            # Prevent duplicate book titles
            if title in self.inventory["Title"].values:
                print("Book already exists. Use update option.")
                return

            # Create a DataFrame for the new book
            new_book = pd.DataFrame([{
                "Title": title,
                "Author": author,
                "Genre": genre,
                "Price": price,
                "Quantity": quantity
            }])

            # Add the book to the existing inventory
            self.inventory = pd.concat(
                [self.inventory, new_book], ignore_index=True
            )

            # Save changes
            self.inventory.to_csv(self.inventory_file, index=False)
            print("Book added successfully.")

        except ValueError:
            print("Enter a valid price and quantity.")

    def remove_book(self):
        """
        Removes a book from inventory using its title.
        Saves the updated inventory to the CSV file.
        """
        title = input("Enter book title to remove: ").strip()

        if title in self.inventory["Title"].values:
            self.inventory = self.inventory[
                self.inventory["Title"] != title
            ]

            self.inventory.to_csv(self.inventory_file, index=False)
            print("Book removed successfully.")
        else:
            print("Book not found.")

    def update_inventory(self):
        """
        Updates the available stock of an existing book.
        The new quantity cannot be negative.
        """
        title = input("Enter book title: ").strip()

        if title not in self.inventory["Title"].values:
            print("Book not found.")
            return

        try:
            quantity = int(input("Enter new stock quantity: "))

            if quantity < 0:
                print("Quantity cannot be negative.")
                return

            # Update the stock quantity
            self.inventory.loc[
                self.inventory["Title"] == title, "Quantity"
            ] = quantity

            self.inventory.to_csv(self.inventory_file, index=False)
            print("Stock updated successfully.")

        except ValueError:
            print("Enter a valid quantity.")

    def display_inventory(self):
        """
        Displays all books currently available in the inventory.
        """
        print("\n----- BOOK INVENTORY -----")

        if self.inventory.empty:
            print("Inventory is empty.")
        else:
            print(self.inventory.to_string(index=False))

    def record_sale(self):
        """
        Records the sale of a book.

        Checks stock availability, calculates total revenue,
        updates the inventory, and saves the sale details.
        """
        title = input("Enter book title sold: ").strip()

        if title not in self.inventory["Title"].values:
            print("Book not found.")
            return

        try:
            quantity = int(input("Enter quantity sold: "))

            if quantity <= 0:
                print("Quantity must be positive.")
                return

            # Find the selected book
            index = self.inventory.index[
                self.inventory["Title"] == title
            ][0]

            available = int(self.inventory.loc[index, "Quantity"])
            price = float(self.inventory.loc[index, "Price"])

            # Check whether enough stock is available
            if quantity > available:
                print("Not enough stock available.")
                return

            # Calculate revenue and get today's date
            revenue = price * quantity
            date = pd.Timestamp.today().strftime("%Y-%m-%d")

            # Create a new sales record
            new_sale = pd.DataFrame([{
                "Date": date,
                "Title": title,
                "Quantity Sold": quantity,
                "Total Revenue": revenue
            }])

            # Add the sale to the sales DataFrame
            self.sales = pd.concat(
                [self.sales, new_sale], ignore_index=True
            )

            # Reduce the available stock
            self.inventory.loc[index, "Quantity"] -= quantity

            # Save both files
            self.inventory.to_csv(self.inventory_file, index=False)
            self.sales.to_csv(self.sales_file, index=False)

            print("Sale recorded successfully.")
            print("Total revenue: Rs.", revenue)

        except ValueError:
            print("Enter a valid quantity.")

    def generate_report(self):
        """
        Generates a sales report using NumPy and pandas.

        Displays total revenue, average sale revenue,
        total books sold, best-selling books, stock by genre,
        monthly revenue, and revenue by author.
        """
        if self.sales.empty:
            print("No sales data available.")
            return

        # Convert sales columns into NumPy arrays
        revenue = self.sales["Total Revenue"].to_numpy(dtype=float)
        quantities = self.sales["Quantity Sold"].to_numpy(dtype=float)

        print("\n----- SALES REPORT -----")

        # Calculate sales statistics using NumPy
        print("Total revenue: Rs.", np.sum(revenue))
        print("Average sale revenue: Rs.", round(np.mean(revenue), 2))
        print("Total books sold:", int(np.sum(quantities)))

        # Find the best-selling books
        top_books = self.sales.groupby("Title")[
            "Quantity Sold"
        ].sum().sort_values(ascending=False)

        print("\nBest-selling books:")
        print(top_books)

        # Calculate available stock by genre
        print("\nBooks by genre:")
        genre_data = self.inventory.groupby("Genre")["Quantity"].sum()
        print(genre_data)

        # Calculate revenue for each month
        sales_details = self.sales.copy()
        sales_details["Month"] = sales_details["Date"].dt.to_period("M")

        print("\nMonthly revenue:")
        print(sales_details.groupby("Month")["Total Revenue"].sum())

        # Combine sales and inventory information
        details = self.sales.merge(
            self.inventory[["Title", "Author", "Genre", "Price"]],
            on="Title",
            how="left"
        )

        # Calculate revenue by author
        print("\nRevenue by author:")
        print(details.groupby("Author")["Total Revenue"].sum())

    def show_charts(self):
        """
        Creates four visualizations:
        1. Bar chart: Revenue by genre
        2. Line chart: Monthly sales trend
        3. Pie chart: Revenue share by genre
        4. Heatmap: Correlation between price and quantity sold
        """
        if self.sales.empty:
            print("No sales data available for charts.")
            return

        # Combine sales information with book details
        details = self.sales.merge(
            self.inventory[["Title", "Author", "Genre", "Price"]],
            on="Title",
            how="left"
        )

        # 1. Bar chart showing revenue by genre
        genre_revenue = details.groupby("Genre")[
            "Total Revenue"
        ].sum()

        if not genre_revenue.empty:
            genre_revenue.plot(
                kind="bar", title="Revenue by Genre"
            )
            plt.xlabel("Genre")
            plt.ylabel("Total Revenue (Rs.)")
            plt.tight_layout()
            plt.show()

        # 2. Line chart showing monthly revenue
        details["Month"] = (
            details["Date"].dt.to_period("M").astype(str)
        )

        monthly = details.groupby("Month")[
            "Total Revenue"
        ].sum().sort_index()

        if not monthly.empty:
            monthly.plot(
                kind="line",
                marker="o",
                title="Monthly Sales Trend"
            )
            plt.xlabel("Month")
            plt.ylabel("Revenue (Rs.)")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

        # 3. Pie chart showing revenue share by genre
        if not genre_revenue.empty and genre_revenue.sum() > 0:
            genre_revenue.plot(
                kind="pie",
                autopct="%1.1f%%",
                title="Revenue Share by Genre"
            )
            plt.ylabel("")
            plt.tight_layout()
            plt.show()

        # 4. Heatmap showing price and quantity correlation
        heat_data = details[["Price", "Quantity Sold"]].dropna()

        if len(heat_data) >= 2:
            correlation = heat_data.corr()

            sns.heatmap(
                correlation,
                annot=True,
                cmap="coolwarm",
                vmin=-1,
                vmax=1
            )

            plt.title("Price and Sales Correlation")
            plt.tight_layout()
            plt.show()
        else:
            print("More sales records are needed for the heatmap.")

    def menu(self):
        """
        Displays the main menu and calls the selected function.
        The menu continues until the user chooses Exit.
        """
        while True:
            print("\n===== BOOKSTORE SYSTEM =====")
            print("1. Add Book")
            print("2. Remove Book")
            print("3. Update Stock")
            print("4. Display Inventory")
            print("5. Record Sale")
            print("6. Generate Sales Report")
            print("7. Show Charts")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.remove_book()
            elif choice == "3":
                self.update_inventory()
            elif choice == "4":
                self.display_inventory()
            elif choice == "5":
                self.record_sale()
            elif choice == "6":
                self.generate_report()
            elif choice == "7":
                self.show_charts()
            elif choice == "8":
                print("Thank you for using Bookstore System.")
                break
            else:
                print("Invalid choice. Please try again.")


# Program execution starts here
if __name__ == "__main__":

    # Check whether the required CSV files exist
    if (
        not os.path.exists("inventory.csv")
        or not os.path.exists("sales.csv")
    ):
        print("Please keep both CSV files in the project folder.")

    else:
        # Create the Bookstore object and start the menu
        bookstore = Bookstore()
        bookstore.menu()
