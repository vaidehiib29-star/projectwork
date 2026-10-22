
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class Bookstore:

    def __init__(self):
        self.inventory_file = "inventory.csv"
        self.sales_file = "sales.csv"

        self.load_data()

    # Load CSV files
    def load_data(self):
        try:
            self.inventory = pd.read_csv(self.inventory_file)
            self.sales = pd.read_csv(self.sales_file)

            self.inventory["Price"] = pd.to_numeric(
                self.inventory["Price"], errors="coerce"
            )
            self.inventory["Quantity"] = pd.to_numeric(
                self.inventory["Quantity"], errors="coerce"
            )

            self.inventory.dropna(
                subset=["Title", "Author", "Genre", "Price", "Quantity"],
                inplace=True
            )

            self.inventory = self.inventory[
                (self.inventory["Price"] > 0) &
                (self.inventory["Quantity"] >= 0)
            ]

            self.sales["Quantity Sold"] = pd.to_numeric(
                self.sales["Quantity Sold"], errors="coerce"
            )
            self.sales["Total Revenue"] = pd.to_numeric(
                self.sales["Total Revenue"], errors="coerce"
            )
            self.sales["Date"] = pd.to_datetime(
                self.sales["Date"], errors="coerce"
            )

            self.sales.dropna(
                subset=["Date", "Title", "Quantity Sold", "Total Revenue"],
                inplace=True
            )

            print("Inventory and sales data loaded successfully!")

        except FileNotFoundError:
            print("Error: CSV files not found!")
            raise

    # Save inventory
    def save_inventory(self):
        self.inventory.to_csv(self.inventory_file, index=False)

    # Save sales
    def save_sales(self):
        self.sales["Date"] = pd.to_datetime(
            self.sales["Date"]
        ).dt.strftime("%Y-%m-%d")
        self.sales.to_csv(self.sales_file, index=False)

    # Display all books
    def display_books(self):
        print("\n========== BOOK INVENTORY ==========")

        if self.inventory.empty:
            print("No books available.")
        else:
            print(self.inventory.to_string(index=False))

    # Add a new book
    def add_book(self):
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        genre = input("Enter book genre: ").strip()

        if not title or not author or not genre:
            print("Error: All details are required.")
            return

        try:
            price = float(input("Enter book price: "))
            quantity = int(input("Enter quantity: "))

            if price <= 0 or quantity <= 0:
                print("Price and quantity must be positive.")
                return

        except ValueError:
            print("Please enter valid numbers.")
            return

        existing = self.inventory[
            self.inventory["Title"].str.lower() == title.lower()
        ]

        if not existing.empty:
            print("Book already exists. Use Update Stock.")
            return

        new_book = pd.DataFrame([{
            "Title": title,
            "Author": author,
            "Genre": genre,
            "Price": price,
            "Quantity": quantity
        }])

        self.inventory = pd.concat(
            [self.inventory, new_book], ignore_index=True
        )

        self.save_inventory()
        print("Book added successfully!")

    # Update stock quantity
    def update_inventory(self):
        title = input("Enter book title: ").strip()

        matching = self.inventory[
            self.inventory["Title"].str.lower() == title.lower()
        ]

        if matching.empty:
            print("Book not found.")
            return

        try:
            quantity = int(input("Enter new stock quantity: "))

            if quantity < 0:
                print("Quantity cannot be negative.")
                return

        except ValueError:
            print("Enter a valid whole number.")
            return

        index = matching.index[0]
        self.inventory.loc[index, "Quantity"] = quantity

        self.save_inventory()
        print("Stock updated successfully!")

    # Remove a book
    def remove_book(self):
        title = input("Enter book title to remove: ").strip()

        matching = self.inventory[
            self.inventory["Title"].str.lower() == title.lower()
        ]

        if matching.empty:
            print("Book not found.")
            return

        self.inventory = self.inventory.drop(matching.index)
        self.save_inventory()
        print("Book removed successfully!")

    # Record a book sale
    def record_sale(self):
        title = input("Enter book title sold: ").strip()

        matching = self.inventory[
            self.inventory["Title"].str.lower() == title.lower()
        ]

        if matching.empty:
            print("Book not found.")
            return

        index = matching.index[0]
        available = int(self.inventory.loc[index, "Quantity"])
        price = float(self.inventory.loc[index, "Price"])

        try:
            quantity = int(input("Enter quantity sold: "))

            if quantity <= 0:
                print("Quantity must be positive.")
                return

            if quantity > available:
                print("Not enough stock available.")
                return

        except ValueError:
            print("Enter a valid whole number.")
            return

        revenue = price * quantity
        date = input("Enter sale date (YYYY-MM-DD): ").strip()

        try:
            date = pd.to_datetime(date, format="%Y-%m-%d")
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD.")
            return

        new_sale = pd.DataFrame([{
            "Date": date.strftime("%Y-%m-%d"),
            "Title": self.inventory.loc[index, "Title"],
            "Quantity Sold": quantity,
            "Total Revenue": revenue
        }])

        self.sales = pd.concat(
            [self.sales, new_sale], ignore_index=True
        )

        self.inventory.loc[index, "Quantity"] = available - quantity

        self.save_inventory()
        self.save_sales()

        print(f"Sale recorded successfully!")
        print(f"Quantity sold: {quantity}")
        print(f"Total revenue: Rs. {revenue:.2f}")

    # Sales report using NumPy
    def generate_report(self):
        print("\n========== SALES REPORT ==========")

        if self.sales.empty:
            print("No sales data available.")
            return

        revenue = self.sales["Total Revenue"].to_numpy(dtype=float)
        quantity = self.sales["Quantity Sold"].to_numpy(dtype=float)

        print(f"Total books in inventory: {len(self.inventory)}")
        print(f"Total stock available: {self.inventory['Quantity'].sum()}")
        print(f"Total books sold: {np.sum(quantity):.0f}")
        print(f"Total revenue: Rs. {np.sum(revenue):.2f}")
        print(f"Average sale revenue: Rs. {np.mean(revenue):.2f}")

        best_seller = self.sales.groupby("Title")["Quantity Sold"].sum()

        print("\nBest-selling book:")
        print(best_seller.idxmax())
        print("Copies sold:", int(best_seller.max()))

        print("\nRevenue by book:")
        print(
            self.sales.groupby("Title")["Total Revenue"]
            .sum().sort_values(ascending=False)
        )

    # Charts using Matplotlib and Seaborn
    def show_charts(self):
        if self.sales.empty:
            print("No sales data available for charts.")
            return

        data = self.sales.merge(
            self.inventory[["Title", "Author", "Genre", "Price"]],
            on="Title",
            how="left"
        )

        data["Genre"] = data["Genre"].fillna("Unknown")
        data["Author"] = data["Author"].fillna("Unknown")
        data["Price"] = data["Price"].fillna(0)
        data["Month"] = data["Date"].dt.to_period("M").astype(str)

        # 1. Bar chart: Sales by genre
        genre_sales = data.groupby("Genre")["Quantity Sold"].sum()

        genre_sales.plot(kind="bar", title="Books Sold by Genre")
        plt.xlabel("Genre")
        plt.ylabel("Quantity Sold")
        plt.tight_layout()
        plt.show()

        # 2. Line graph: Monthly sales
        monthly_sales = data.groupby("Month")["Total Revenue"].sum()

        monthly_sales.plot(
            kind="line", marker="o", title="Monthly Sales Revenue"
        )
        plt.xlabel("Month")
        plt.ylabel("Revenue (Rs.)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # 3. Pie chart: Revenue by genre
        genre_revenue = data.groupby("Genre")["Total Revenue"].sum()

        genre_revenue.plot(
            kind="pie", autopct="%1.1f%%",
            title="Revenue Share by Genre"
        )
        plt.ylabel("")
        plt.tight_layout()
        plt.show()

        # 4. Heatmap: Price and sales volume
        heat_data = data[["Price", "Quantity Sold"]].corr()

        sns.heatmap(
            heat_data, annot=True, cmap="coolwarm",
            vmin=-1, vmax=1
        )
        plt.title("Price and Sales Correlation")
        plt.tight_layout()
        plt.show()

        # Additional chart: Sales by author
        author_sales = data.groupby("Author")["Quantity Sold"].sum()

        author_sales.plot(
            kind="bar", title="Books Sold by Author"
        )
        plt.xlabel("Author")
        plt.ylabel("Quantity Sold")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()

    # Main menu
    def menu(self):
        while True:
            print("\n===== BOOKSTORE INVENTORY SYSTEM =====")
            print("1. Display Books")
            print("2. Add Book")
            print("3. Update Stock")
            print("4. Remove Book")
            print("5. Record Sale")
            print("6. Generate Sales Report")
            print("7. Show Charts")
            print("8. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.display_books()

            elif choice == "2":
                self.add_book()

            elif choice == "3":
                self.update_inventory()

            elif choice == "4":
                self.remove_book()

            elif choice == "5":
                self.record_sale()

            elif choice == "6":
                self.generate_report()

            elif choice == "7":
                self.show_charts()

            elif choice == "8":
                print("Thank you for using Bookstore System!")
                break

            else:
                print("Invalid choice. Please select 1 to 8.")


# Run the project
if __name__ == "__main__":
    try:
        bookstore = Bookstore()
        bookstore.menu()
    except FileNotFoundError:
        print("Please place inventory.csv and sales.csv beside the Python file.")






import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class Bookstore:

    def __init__(self):
        self.books = pd.read_csv("inventory.csv")
        self.sales = pd.read_csv("sales.csv")

    # Show all books
    def show_books(self):
        print("\n--- Book Inventory ---")
        print(self.books.to_string(index=False))

    # Add a new book
    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        genre = input("Enter book genre: ")

        try:
            price = float(input("Enter book price: "))
            quantity = int(input("Enter quantity: "))

            if price <= 0 or quantity <= 0:
                print("Price and quantity must be positive.")
                return

        except ValueError:
            print("Please enter valid numbers.")
            return

        if title.strip() == "" or author.strip() == "" or genre.strip() == "":
            print("Please enter all book details.")
            return

        if self.books["Title"].str.lower().eq(title.lower()).any():
            print("This book already exists.")
            return

        new_book = {
            "Title": title,
            "Author": author,
            "Genre": genre,
            "Price": price,
            "Quantity": quantity
        }

        self.books.loc[len(self.books)] = new_book
        self.books.to_csv("inventory.csv", index=False)

        print("Book added successfully!")

    # Update book quantity
    def update_stock(self):
        title = input("Enter book title: ")

        found = self.books["Title"].str.lower() == title.lower()

        if not found.any():
            print("Book not found.")
            return

        try:
            quantity = int(input("Enter new quantity: "))

            if quantity < 0:
                print("Quantity cannot be negative.")
                return

        except ValueError:
            print("Enter a valid quantity.")
            return

        self.books.loc[found, "Quantity"] = quantity
        self.books.to_csv("inventory.csv", index=False)

        print("Stock updated successfully!")

    # Record a sale
    def sell_book(self):
        title = input("Enter book title: ")

        found = self.books["Title"].str.lower() == title.lower()

        if not found.any():
            print("Book not found.")
            return

        try:
            quantity = int(input("Enter quantity sold: "))

            if quantity <= 0:
                print("Quantity must be positive.")
                return

        except ValueError:
            print("Enter a valid quantity.")
            return

        index = self.books.index[found][0]
        stock = int(self.books.loc[index, "Quantity"])
        price = float(self.books.loc[index, "Price"])

        if quantity > stock:
            print("Not enough books in stock.")
            return

        revenue = price * quantity

        self.books.loc[index, "Quantity"] = stock - quantity
        self.books.to_csv("inventory.csv", index=False)

        sale = {
            "Date": input("Enter date (YYYY-MM-DD): "),
            "Title": self.books.loc[index, "Title"],
            "Quantity Sold": quantity,
            "Total Revenue": revenue
        }

        try:
            pd.to_datetime(sale["Date"], format="%Y-%m-%d")
        except ValueError:
            self.books.loc[index, "Quantity"] = stock
            self.books.to_csv("inventory.csv", index=False)
            print("Invalid date. Use YYYY-MM-DD.")
            return

        self.sales.loc[len(self.sales)] = sale
        self.sales.to_csv("sales.csv", index=False)

        print("Sale recorded successfully!")
        print(f"Total revenue: Rs. {revenue:.2f}")

    # Show sales report using NumPy
    def report(self):
        revenue = self.sales["Total Revenue"].to_numpy()
        quantity = self.sales["Quantity Sold"].to_numpy()

        print("\n--- Sales Report ---")
        print(f"Total books sold: {np.sum(quantity)}")
        print(f"Total revenue: Rs. {np.sum(revenue):.2f}")
        print(f"Average sale revenue: Rs. {np.mean(revenue):.2f}")

        best = self.sales.groupby("Title")["Quantity Sold"].sum()

        print("Best-selling book:", best.idxmax())

    # Show charts
    def charts(self):
        if self.sales.empty:
            print("No sales data available.")
            return

        data = self.sales.copy()
        data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
        data["Quantity Sold"] = pd.to_numeric(
            data["Quantity Sold"], errors="coerce"
        )
        data["Total Revenue"] = pd.to_numeric(
            data["Total Revenue"], errors="coerce"
        )
        data.dropna(inplace=True)

        if data.empty:
            print("No valid sales data available.")
            return

        # Bar chart
        data.groupby("Title")["Quantity Sold"].sum().plot(kind="bar")
        plt.title("Books Sold")
        plt.xlabel("Book Title")
        plt.ylabel("Quantity Sold")
        plt.tight_layout()
        plt.show()

        # Line graph
        data["Month"] = data["Date"].dt.to_period("M").astype(str)
        data.groupby("Month")["Total Revenue"].sum().plot(
            kind="line", marker="o"
        )
        plt.title("Monthly Sales")
        plt.xlabel("Month")
        plt.ylabel("Revenue")
        plt.tight_layout()
        plt.show()

        # Pie chart
        books = self.books[["Title", "Genre"]]
        data = data.merge(books, on="Title", how="left")

        data.groupby("Genre")["Total Revenue"].sum().plot(
            kind="pie", autopct="%1.1f%%"
        )
        plt.title("Revenue by Genre")
        plt.ylabel("")
        plt.tight_layout()
        plt.show()

        # Heatmap
        sns.heatmap(
            data[["Quantity Sold", "Total Revenue"]].corr(),
            annot=True
        )
        plt.title("Sales Correlation")
        plt.tight_layout()
        plt.show()


# Main program
store = Bookstore()

while True:
    print("\n===== BOOKSTORE MENU =====")
    print("1. Show Books")
    print("2. Add Book")
    print("3. Update Stock")
    print("4. Sell Book")
    print("5. Sales Report")
    print("6. Show Charts")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        store.show_books()

    elif choice == "2":
        store.add_book()

    elif choice == "3":
        store.update_stock()

    elif choice == "4":
        store.sell_book()

    elif choice == "5":
        store.report()

    elif choice == "6":
        store.charts()

    elif choice == "7":
        print("Thank you for using Bookstore System!")
        break

    else:
        print("Invalid choice. Please try again.")
