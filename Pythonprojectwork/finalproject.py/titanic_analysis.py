#Project Name: Titanic Survival Analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class TitanicAnalysis:

    def __init__(self):
        self.data = None

    def load_data(self):
        try:
            self.data = pd.read_csv("train.csv")
            print("Dataset loaded successfully!")

            print("First 5 rows:")
            print(self.data.head())

        except FileNotFoundError:
            print("Error: PLease keep train.csv in this folder.")


    def explore_data(self):
        if self.data is None:
            return

        print("    Dataset Information   ")
        print("Total passenger:", len(self.data))
        print("Total columns:", len(self.data.columns))

        print("Column names: ")
        print(self.data.column.tolist())

        print("Missing values: ")
        print(self.data.isnull().sum())

        print("Statistical summary: ")
        print(self.data.describe())

    def clean_data(self):
        if self.data is None:
            return

        self.data["Age"] = self.data["Age"].fillna(self.data["Age"].mean())

        self.data["Fare"] = self.data["Fare"].fillna(self.data["Fare"].median())

        self.data["Embarked"] = self.data["Embarked"].fillna(self.data["Embarked"].mode([0]))

        print("Data cleaned successfully!")

    def analyze_survival(self):
        if self.data is None:
            return

        total = len(self.data)
        survival = int(self.data["Survival"].sum())
        not_survived = total - not_survived
        survival_rate = (survived / total) * 100

        print("      Survival Analysis    ")
        print("Total passenger:", total)
        print("passengers survived:", survived)
        print("Passenger did not survive:", not_survived)
        print("Survival rate:", round(survival_rate, 2), "%")

        print("Survival by gender:")
        print(self.data.groupby("Sex")["Survived"].mean().mul(100).round(2))

        print("Survival by passenger class:")
        print(self.data.groupby("class")["Survived"].mean().mul(100).round(2))

        print("Average age of passenger:")
        print(round(self.data["Age"].mean(), 2))

    def show_charts(self):
        if self.data is None:
            return

        #char 1:
        sns.countplot(data = self.data, x="Survived")
        plt.title("Titanic Survival Count")
        plt.xlabel("Survived (0 = No, 1 = Yes)")
        plt.ylabel("Number of Passenger")
        plt.tight_layout()
        plt.show()

        #char 2:
        sns.barplot(data = self.data, x = "Sex", y = "Survived")
        plt.title("Survival Rate by Gender")
        plt.xlabel("Gender")
        plt.ylabel("Survival Rate")
        plt.tight_layout()
        plt.show()

        #chart 3:
        sns.barplot(data = self.data, x = "Pclass", y = "Survived")
        plt.title("Survival Rate by Passenger Class")
        plt.xlabel("Passenger Class")
        plt.ylabel("Survival Rate")
        plt.tight_layout()
        plt.show()

        #chart 4:
        sns.histplot(data = self.data, x = "Age", bins = 20, kde = True)
        plt.title("Age Distribution of Passengers")
        plt.xlabel("Age")
        plt.ylabel("Number of Passengers")
        plt.tight_layout()
        plt.show()

        #chart 5:
        sns.barplot(data = self.data, x = "Pclass", y = "Survived", hue = "Sex")
        plt.title("Survival by Gender and Class")
        plt.xlabel("Passenger Class")
        plt.ylabel("Survival Rate")
        plt.tight_layout()
        plt.show()

    def save_data(self):
        if self.data is None:
            return

        self.data.to_csv("Cleaned_titanic.csv", index = False)
        print("Cleaned dataset saved successfully!")

def main():
    project = TitanicAnalysis()

    while True:
        print("    Titanic Survival Analysis   ")
        print("1. Load Dataset")
        print("2. Explore Dataset")
        print("3. Clean Dataset")
        print("4. Analyze Survival")
        print("5. Show Charts")
        print("6. Save Cleaned Dataset")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            project.load_data()

        elif choice == "2":
            project.explore_data()

        elif choice == "3":
            project.clean_data()

        elif choice == "4":
            project.analyze_survival()

        elif choice == "5":
            project.show_charts()

        elif choice == "6":
            project.save_data()

        elif choice == "7":
            print("Thank you for using the project!")
            break

        else:
            print("Invalid choice! Please enter 1 to 7.")

if __name__ == "__main__":
    main()
                    

