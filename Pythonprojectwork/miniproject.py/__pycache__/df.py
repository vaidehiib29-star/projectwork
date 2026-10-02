import numpy as np

class DataAnalytics:

    def __init__(self):
        self.array = None

    def create_array(self):

        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = int(input("Enter your choice: "))

        # 1D Array
        if choice == 1:

            n = int(input("Enter the number of elements: "))

            values = list(map(int, input(f"Enter {n} elements separated by space: ").split()))

            if len(values) != n:
                print("Number of elements does not match!")
                return

            self.array = np.array(values)

        # 2D Array
        elif choice == 2:

            rows = int(input("Enter the number of rows: "))
            columns = int(input("Enter the number of columns: "))

            total = rows * columns

            values = list(map(int, input(f"Enter {total} elements separated by space: ").split()))

            if len(values) != total:
                print("Number of elements does not match!")
                return

            self.array = np.array(values).reshape(rows, columns)

        # 3D Array
        elif choice == 3:

            layers = int(input("Enter the number of layers: "))
            rows = int(input("Enter the number of rows: "))
            columns = int(input("Enter the number of columns: "))

            total = layers * rows * columns

            values = list(map(int, input(f"Enter {total} elements separated by space: ").split()))

            if len(values) != total:
                print("Number of elements does not match!")
                return

            self.array = np.array(values).reshape(layers, rows, columns)

        else:
            print("Invalid choice!")
            return

        print("\nArray created successfully:")
        print(self.array)

    # Indexing and Slicing
    def indexing_slicing(self):
        print("\n------ Indexing and Slicing ------")

        print("Array:")
        print(self.array)
        
        # Indexing
        print("\nIndexing:")
        if self.array.ndim == 1:
            for i in range(self.array.shape[0]):
                print("Index", i, ":", self.array[i])
                
        elif self.array.ndim == 2:
            for row in range(self.array.shape[0]):
                for column in range(self.array.shape[1]):
                    print("Element:", self.array[row, column])

        elif self.array.ndim == 3:

            for layer in range(self.array.shape[0]):
                for row in range(self.array.shape[1]):
                    for column in range(self.array.shape[2]):
                        print("Element:", self.array[layer, row, column])

        # Slicing
        print("\nSlicing:")

        if self.array.ndim == 1:

            print("First two elements:")
            print(self.array[0:2])

        elif self.array.ndim == 2:

            print("Rows:")
            print(self.array[0:2])

            print("Columns:")
            print(self.array[:, 0:2])

        elif self.array.ndim == 3:

            print("First two layers:")
            print(self.array[0:2])
            
    # Mathematical Operations
    def mathematical_operations(self):

        if self.array is None:
            print("\nPlease create an array first!")
            return

        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product")
        print("6. Matrix Multiplication")
        print("7. Go Back")

        choice = int(input("Enter your choice: "))

        # Go Back
        if choice == 7:
            return

        # Matrix Multiplication
        if choice == 6:

            if self.array.ndim != 2:
                print("Matrix multiplication is only available for 2D arrays.")
                return

            rows = int(input("Enter rows of second matrix: "))

            columns = int(input("Enter columns of second matrix: "))

            if rows != self.array.shape[1]:
                print("Rows of second matrix must be equal to columns of first matrix.")
                return

            total = rows * columns

            values = list(map(int,input(f"Enter {total} elements: ").split()))

            if len(values) != total:
                print("Number of elements does not match!")
                return

            second_matrix = np.array(values).reshape(rows, columns)

            print("\nFirst Matrix:")
            print(self.array)

            print("\nSecond Matrix:")
            print(second_matrix)

            result = np.matmul(self.array,second_matrix)

            print("\nMatrix Multiplication Result:")
            print(result)

            return

        # Other operations
        values = list(
            map(int,input(f"Enter {self.array.size} elements for second array: ").split()))

        if len(values) != self.array.size:
            print("Number of elements does not match!")
            return

        second_array = np.array(values).reshape(self.array.shape)

        print("\nFirst Array:")
        print(self.array)

        print("\nSecond Array:")
        print(second_array)

        # Addition
        if choice == 1:

            result = self.array + second_array

            print("\nResult of Addition:")
            print(result)

        # Subtraction
        elif choice == 2:

            result = self.array - second_array

            print("\nResult of Subtraction:")
            print(result)

        # Multiplication
        elif choice == 3:

            result = self.array * second_array

            print("\nResult of Multiplication:")
            print(result)

        # Division
        elif choice == 4:

            if np.any(second_array == 0):

                print("Division by zero is not allowed!")

            else:

                result = self.array / second_array

                print("\nResult of Division:")
                print(result)

        # Dot Product
        elif choice == 5:

            result = np.dot(
                self.array.flatten(),
                second_array.flatten()
            )

            print("\nDot Product:")
            print(result)

        else:
            print("Invalid choice!")


    # Combine and Split
    def combine_split(self):

        if self.array is None:
            print("\nPlease create an array first!")
            return

        while True:

            print("\nChoose an option:")
            print("1. Combine Arrays")
            print("2. Split Array")
            print("3. Go Back")

            choice = int(input("Enter your choice: "))

            # Combine
            if choice == 1:

                values = list(map(int,input(f"Enter {self.array.size} elements for another array: ").split()))

                if len(values) != self.array.size:
                    print("Number of elements does not match!")
                    continue

                second_array = np.array(values).reshape(self.array.shape)

                print("\nOriginal Array:")
                print(self.array)

                print("\nSecond Array:")
                print(second_array)

                if self.array.ndim == 1:

                    result = np.concatenate((self.array, second_array))

                else:

                    result = np.concatenate((self.array, second_array),axis=0)

                print("\nCombined Array:")
                print(result)

            # Split
            elif choice == 2:

                parts = int(input("Enter number of parts: "))

                try:

                    result = np.array_split(self.array,parts,axis=0)

                    print("\nSplit Arrays:")

                    for i in range(len(result)):

                        print(f"\nPart {i + 1}:")
                        print(result[i])

                except ValueError:

                    print("Invalid number of parts!")

            # Go Back
            elif choice == 3:
                break

            else:
                print("Invalid choice!")


    # Search, Sort and Filter
    def search_sort_filter(self):

        if self.array is None:
            print("\nPlease create an array first!")
            return

        while True:

            print("\nChoose an option:")
            print("1. Search a value")
            print("2. Sort the array")
            print("3. Filter values")
            print("4. Go Back")

            choice = int(input("Enter your choice: "))

            # Search
            if choice == 1:

                value = int(input("Enter value to search: "))

                result = np.where(self.array == value)

                if len(result[0]) == 0:

                    print("Value not found!")

                else:

                    print(f"Value {value} found at:")
                    print(result)

            # Sort
            elif choice == 2:

                print("\nOriginal Array:")
                print(self.array)

                order = input("Enter A for Ascending or D for Descending: ").upper()

                if order == "A":

                    result = np.sort(self.array)

                elif order == "D":

                    result = np.sort(self.array)[::-1]

                else:

                    print("Invalid order!")
                    continue

                print("\nSorted Array:")
                print(result)

            # Filter
            elif choice == 3:

                print("\nChoose filter condition:")
                print("1. Greater than")
                print("2. Less than")
                print("3. Equal to")
                print("4. Greater than or equal")
                print("5. Less than or equal")

                condition = int(input("Enter your choice: "))

                value = int(input("Enter value: "))

                if condition == 1:

                    result = self.array[self.array > value]

                elif condition == 2:

                    result = self.array[self.array < value]

                elif condition == 3:

                    result = self.array[self.array == value]

                elif condition == 4:

                    result = self.array[self.array >= value]

                elif condition == 5:

                    result = self.array[self.array <= value]

                else:

                    print("Invalid condition!")
                    continue

                print("\nFiltered values:")
                print(result)

            # Go Back
            elif choice == 4:
                break

            else:
                print("Invalid choice!")


    # Aggregates and Statistics
    def aggregates_statistics(self):

        if self.array is None:
            print("\nPlease create an array first!")
            return

        while True:

            print("\nChoose an operation:")
            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Standard Deviation")
            print("5. Variance")
            print("6. Minimum")
            print("7. Maximum")
            print("8. Percentile")
            print("9. Correlation")
            print("10. Go Back")

            choice = int(input("Enter your choice: "))

            # Sum
            if choice == 1:

                print("\nSum:", np.sum(self.array))

            # Mean
            elif choice == 2:

                print("\nMean:", np.mean(self.array))

            # Median
            elif choice == 3:

                print("\nMedian:",np.median(self.array))

            # Standard Deviation
            elif choice == 4:

                print("\nStandard Deviation:",np.std(self.array))

            # Variance
            elif choice == 5:

                print("\nVariance:",np.var(self.array))

            # Minimum
            elif choice == 6:

                print("\nMinimum:",np.min(self.array))

            # Maximum
            elif choice == 7:

                print("\nMaximum:",np.max(self.array))

            # Percentile
            elif choice == 8:

                percentage = float(input("Enter percentile (0-100): "))

                if percentage < 0 or percentage > 100:

                    print("Percentile must be between 0 and 100!")

                else:

                    result = np.percentile(self.array,percentage)

                    print(f"\n{percentage}th Percentile:",result)

            # Correlation
            elif choice == 9:

                values = list(map(int,input(f"Enter {self.array.size} elements for second array: ").split()))

                if len(values) != self.array.size:

                    print("Number of elements does not match!")
                    continue

                first_array = self.array.flatten()
                second_array = np.array(values)

                result = np.corrcoef(first_array, second_array)

                print("\nCorrelation:")
                print(result)

            # Go Back
            elif choice == 10:

                break

            else:

                print("Invalid choice!")

# Main Program
obj = DataAnalytics()

while True:

    print("\n------------------------------")
    print("       Data Analytics Menu")
    print("------------------------------")
    print("1. Create Array")
    print("2. Indexing and Slicing")
    print("3. Mathematical Operations")
    print("4. Combine and Split")
    print("5. Search, Sort and Filter")
    print("6. Aggregates and Statistics")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        obj.create_array()

    elif choice == 2:
        obj.indexing_slicing()

    elif choice == 3:
        obj.mathematical_operations()

    elif choice == 4:
        obj.combine_split()

    elif choice == 5:
        obj.search_sort_filter()

    elif choice == 6:
        obj.aggregates_statistics()

    elif choice == 7:
        print("\nThank you for using Data Analytics")
        print("Goodbye!")
        break

    else:
        print("\nInvalid choice!")