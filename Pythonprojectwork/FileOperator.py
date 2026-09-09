# File Operator
import os
from datetime import datetime

class JournalManager:
    def __init__(self):
        self.filename = "journal.txt"

    # Add a new journal entry
    def add_entry(self):
        try:
            entry = input("\nEnter your journal entry: ")
            if entry.strip() == "":
                print("Entry cannot be empty.")
                return
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Try to create the file if it does not exist
            try:
                file = open(self.filename, "x")
                file.close()
            except FileExistsError:
                pass

            # Append the new entry
            with open(self.filename, "a") as file:
                file.write(f"[{timestamp}]\n")
                file.write(entry + "\n")
                file.write("-" * 40 + "\n")
            print("\nEntry added successfully!")
        except PermissionError:
            print("Error: You do not have permission to write to the file.")
        except OSError as e:
            print("File error:", e)

    # View all journal entries
    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                data = file.read()
            if data.strip() == "":
                print("\nNo journal entries found.")
                return
            print("\nYour Journal Entries:")
            print("-" * 40)
            print(data)
        except FileNotFoundError:
            print("\nError: The journal file does not exist.")
            print("Please add a new entry first.")
        except PermissionError:
            print("Error: You do not have permission to read the file.")
        except OSError as e:
            print("File error:", e)

    # Search for a keyword or date
    def search_entry(self):
        try:
            keyword = input("\nEnter a keyword or date to search: ").strip()
            if keyword == "":
                print("Please enter something to search.")
                return
            with open(self.filename, "r") as file:
                lines = file.readlines()

            found = False
            i = 0
            print("\nMatching Entries:")
            print("-" * 40)

            while i < len(lines):

                # An entry starts with [
                if lines[i].startswith("["):
                    timestamp = lines[i]
                    text = ""
                    if i + 1 < len(lines):
                        text = lines[i + 1]

                    # Search in timestamp or journal text
                    if keyword.lower() in timestamp.lower() or \
                        keyword.lower() in text.lower():
                        print(timestamp.strip())
                        print(text.strip())
                        print("-" * 40)
                        found = True

                i += 1

            if not found:
                print("No entries were found for the keyword:", keyword)
        except FileNotFoundError:
            print("\nError: The journal file does not exist.")
            print("Please add a new entry first.")
        except PermissionError:
            print("Error: You do not have permission to read the file.")
        except OSError as e:
            print("File error:", e)

    # Delete all journal entries
    def delete_entries(self):
        try:
            if not os.path.exists(self.filename):
                print("\nNo journal entries to delete.")
                return
            choice = input(
                "\nAre you sure you want to delete all entries? (yes/no): "
            ).lower()

            if choice == "yes":

                # Open in write mode to demonstrate 'w' mode
                with open(self.filename, "w") as file:
                    file.write("")

                # Delete the actual file
                os.remove(self.filename)
                print("\nAll journal entries have been deleted.")

            elif choice == "no":
                print("\nDelete operation cancelled.")
            else:
                print("\nPlease enter yes or no.")
        except PermissionError:
            print("Error: You do not have permission to delete the file.")
        except OSError as e:
            print("File error:", e)

# Main program
def main():

    journal = JournalManager()

    while True:
        print("\n========================================")
        print("PERSONAL JOURNAL MANAGER")
        print("========================================")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit") 

        try:
            choice = int(input("Please select an option: "))

            if choice == 1:
                journal.add_entry()
            elif choice == 2:
                journal.view_entries()
            elif choice == 3:
                journal.search_entry()
            elif choice == 4:
                journal.delete_entries()
            elif choice == 5:
                print("\nThank you for using Personal Journal Manager.")
                print("Goodbye!")
                break
            else:
                print("\nInvalid option. Please select a valid option from the menu.")
        except ValueError:
            print("\nInvalid input. Please enter a number from 1 to 5.")
        except KeyboardInterrupt:
            print("\n\nProgram stopped by user.")
            break

if __name__ == "__main__":
    main()
