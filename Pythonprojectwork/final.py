
# Project: Titanic Survival Analysis
# Purpose: Analyze passenger survival using Python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class TitanicAnalysis:

    def __init__(self):
        self.data = None

    # Load the dataset
    def load_data(self):
        try:
            self.data = pd.read_csv("train.csv")
            print("\nDataset loaded successfully!")

            print("\nFirst 5 rows:")
            print(self.data.head())

        except FileNotFoundError:
            print("Error: Please keep train.csv in this folder.")

    # Display basic information
    def explore_data(self):
        if self.data is None:
            return

        print("\n--- Dataset Information ---")
        print("Total passengers:", len(self.data))
        print("Total columns:", len(self.data.columns))

        print("\nColumn names:")
        print(self.data.columns.tolist())

        print("\nMissing values:")
        print(self.data.isnull().sum())

        print("\nStatistical summary:")
        print(self.data.describe())

    # Clean the data
    def clean_data(self):
        if self.data is None:
            return

        # Fill missing ages with the average age
        self.data["Age"] = self.data["Age"].fillna(
            self.data["Age"].mean()
        )

        # Fill missing fares with the median fare
        self.data["Fare"] = self.data["Fare"].fillna(
            self.data["Fare"].median()
        )

        # Fill missing port values with the most common port
        self.data["Embarked"] = self.data["Embarked"].fillna(
            self.data["Embarked"].mode()[0]
        )

        print("\nData cleaned successfully!")

    # Calculate survival statistics
    def analyze_survival(self):
        if self.data is None:
            return

        total = len(self.data)
        survived = int(self.data["Survived"].sum())
        not_survived = total - survived
        survival_rate = (survived / total) * 100

        print("\n--- Survival Analysis ---")
        print("Total passengers:", total)
        print("Passengers survived:", survived)
        print("Passengers did not survive:", not_survived)
        print("Survival rate:", round(survival_rate, 2), "%")

        print("\nSurvival by gender:")
        print(
            self.data.groupby("Sex")["Survived"]
            .mean().mul(100).round(2)
        )

        print("\nSurvival by passenger class:")
        print(
            self.data.groupby("Pclass")["Survived"]
            .mean().mul(100).round(2)
        )

        print("\nAverage age of passengers:")
        print(round(self.data["Age"].mean(), 2))

    # Draw charts
    def show_charts(self):
        if self.data is None:
            return

        # Chart 1: Number of survivors
        sns.countplot(data=self.data, x="Survived")
        plt.title("Titanic Survival Count")
        plt.xlabel("Survived (0 = No, 1 = Yes)")
        plt.ylabel("Number of Passengers")
        plt.tight_layout()
        plt.show()

        # Chart 2: Survival by gender
        sns.barplot(
            data=self.data,
            x="Sex",
            y="Survived"
        )
        plt.title("Survival Rate by Gender")
        plt.xlabel("Gender")
        plt.ylabel("Survival Rate")
        plt.tight_layout()
        plt.show()

        # Chart 3: Survival by passenger class
        sns.barplot(
            data=self.data,
            x="Pclass",
            y="Survived"
        )
        plt.title("Survival Rate by Passenger Class")
        plt.xlabel("Passenger Class")
        plt.ylabel("Survival Rate")
        plt.tight_layout()
        plt.show() 

        # Chart 4: Age distribution
        sns.histplot(
            data=self.data,
            x="Age",
            bins=20,
            kde=True
        )
        plt.title("Age Distribution of Passengers")
        plt.xlabel("Age")
        plt.ylabel("Number of Passengers")
        plt.tight_layout()
        plt.show()

        # Chart 5: Survival by gender and class
        sns.barplot(
            data=self.data,
            x="Pclass",
            y="Survived",
            hue="Sex"
        )
        plt.title("Survival by Gender and Class")
        plt.xlabel("Passenger Class")
        plt.ylabel("Survival Rate")
        plt.tight_layout()
        plt.show()

    # Save the cleaned dataset
    def save_data(self):
        if self.data is None:
            return

        self.data.to_csv("cleaned_titanic.csv", index=False)
        print("\nCleaned dataset saved successfully!")


# Main program
def main():
    project = TitanicAnalysis()

    while True:
        print("\n===== TITANIC SURVIVAL ANALYSIS =====")
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
