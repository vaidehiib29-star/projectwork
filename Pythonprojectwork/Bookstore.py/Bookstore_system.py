import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Bookstore:
    def __init__(self):
        self.inv_file = "inventory.csv"
        self.sales_file = "sales.csv"
        f1 = open(self.inv_file, "a+")
        f1.close()
        f2 = open(self.sales_file, "a+")
        f2.close()
        self.inventory = pd.read_csv(self.inv_file)
        if len(self.inventory.columns) == 0:
            self.inventory = pd.DataFrame(columns=["Title", "Author", "Genre", "Price", "Quantity"])
            self.inventory.to_csv(self.inv_file, index=False)
        self.sales = pd.read_csv(self.sales_file)
        if len(self.sales.columns) == 0:
            self.sales = pd.DataFrame(columns=["Date", "Title", "Quantity Sold", "Total Revenue"])
            self.sales.to_csv(self.sales_file, index=False)

    def show_books(self):
        print("ALL BOOKS")
        if len(self.inventory) == 0:
            print("No books found in inventory!")
        else:
            print(self.inventory)

    def add_book(self):
        print("Add New Book")
        title = input("Enter book title: ")
        author = input("Enter author name:")
        genre = input("Enter genre: ")
        price = int(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        new_data = {"Title": title, "Author": author, "Genre": genre, "Price": price, "Quantity": quantity}
        self.inventory = pd.concat([self.inventory, pd.DataFrame([new_data])], ignore_index=True)
        self.inventory.to_csv(self.inv_file,index=False)
        print("Book added sucessfully!")

    def update_stock(self):
        print("Update Stock")
        t_name = input("Enter book title: ")
        new_qty = int(input("Enter new quantity: "))
        for i in range(len(self.inventory)):
            if self.inventory.loc[i, "Title"] == t_name:
                self.inventory.loc[i, "Quantity"] = new_qty
        self.inventory.to_csv(self.inv_file, index=False)
        print("Stock updated successfully.")
    my_store = Bookstore()
    my_store.menu()

    def sell_book(self):
        print("Sell Book")
        t_name = input("Enter book title to sell: ")
        qty_sold = int(input("Enter quantity sold: "))
        s_date = input("Enter date (YYYY-MM-DD): ")
        book_price = 0
        found_idx = -1
        for i in range(len(self.inventory)):
            if self.inventory.loc[i, "Title"] == t_name:
                book_price = self.inventory.loc[i, "Price"]
                current_qty = self.inventory.loc[i, "Quantity"]
                found_idx = i
                break
        if found_idx != -1:
            if current_qty >= qty_sold:
                self.inventory.loc[found_idx, "Quantity"] = current_qty - qty_sold
                total_rev = book_price * qty_sold
                sale_data = {"Date": s_date, "Title": t_name, "Quantity Sold": qty_sold, "Total Revenue": total_rev}
                self.sales = pd.concat([self.sales, pd.DataFrame([sale_data])], ignore_index=True)
                self.inventory.to_csv(self.inv_file, index=False)
                self.sales.to_csv(self.sales_file, index=False)
                print("Sale recorded! Total revenue:", total_rev)
            else:
                print("Not enough stock available!")
        else:
            print("Book not found in inventory.")

    def report(self):
        print("SALES REPORT")
        if len(self.sales) == 0:
            print("No sales recorded yet.")
        else:
            total_qty_sold = np.sum(self.sales["Quantity Sold"].values)
            total_rev_all = np.sum(self.sales["Total Revenue"].values)
            print("Total books sold:", total_qty_sold)
            print("Total revenue earned:", total_rev_all)
            print(self.sales.groupby("Title")["Quantity Sold"].sum())

    def charts(self):
        if len(self.sales) > 0:
            plt.figure(figsize=(8, 5))
            self.sales.groupby("Title")["Quantity Sold"].sum().plot(kind="bar")
            plt.title("Quantity Sold per Book")
            plt.xlabel("Title")
            plt.ylabel("Sold Quantity")
            plt.show()
            plt.figure(figsize=(6, 4))
            sns.heatmap(self.sales[["Quantity Sold", "Total Revenue"]].corr(), anot=True, cmap="coolwarm")
            plt.title("Sales Correlation Heatmap")
            plt.show()
        else:
            print("Not enough data to show charts.")

    def menu(self):
        while True:
            print("BOOKSTORE MANAGEMENT")
            print("1. View Books")
            print("2. Add New Book")
            print("3. Update Stock")
            print("4. Sell Book")
            print("5. View Report")
            print("6. Show Charts")
            print("7. Exit")
            choise = input("Enter your choise (1-7): ")
            if choise == "1":
                self.show_books()
            elif choise == "2":
                self.add_book()
            elif choise == "3":
                self.update_stock()
            elif choise == "4":
                self.sell_book()
            elif choise == "5":
                self.report()
            elif choise == "6":
                self.charts()
            elif choise == "7":
                print("thank you good Bye!")
                break
            else:
                print("Invalid choise!")
