import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

FILE_NAME = "expenses.csv"


# Load Data
def load_data():
    if os.path.exists(FILE_NAME):
        return pd.read_csv(FILE_NAME)

    return pd.DataFrame(
        columns=["Date", "Amount", "Category", "Description"]
    )


# Save Data
def save_data(df):
    df.to_csv(FILE_NAME, index=False)


# Add Expense
def add_expense(df):
    try:
        amount = float(input("Enter Amount (₹): "))
        category = input("Enter Category (Food/Travel/Shopping/Bills/Other): ")
        description = input("Enter Description: ")

        new_expense = pd.DataFrame([{
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Amount": amount,
            "Category": category,
            "Description": description
        }])

        df = pd.concat([df, new_expense], ignore_index=True)

        save_data(df)
        print("\n✅ Expense Added Successfully!\n")

        return df

    except ValueError:
        print("❌ Invalid Amount!\n")
        return df


# Show Expenses
def show_expenses(df):
    if df.empty:
        print("\nNo expenses found!\n")
        return

    print("\n========== ALL EXPENSES ==========")
    print(df.to_string(index=False))
    print()


# Total Expense
def total_expense(df):
    total = df["Amount"].sum()
    print(f"\n💰 Total Expense: ₹{total:.2f}\n")


# Category Wise Expense
def category_expense(df):
    if df.empty:
        print("\nNo data available!\n")
        return

    summary = df.groupby("Category")["Amount"].sum()

    print("\n====== CATEGORY SUMMARY ======")
    print(summary)
    print()


# Monthly Report
def monthly_report(df):
    if df.empty:
        print("\nNo data available!\n")
        return

    temp_df = df.copy()
    temp_df["Date"] = pd.to_datetime(temp_df["Date"])

    report = temp_df.groupby(
        temp_df["Date"].dt.strftime("%Y-%m")
    )["Amount"].sum()

    print("\n====== MONTHLY REPORT ======")
    print(report)
    print()


# Expense Chart
def show_chart(df):
    if df.empty:
        print("\nNo data available!\n")
        return

    summary = df.groupby("Category")["Amount"].sum()

    plt.figure(figsize=(8, 6))
    plt.pie(
        summary,
        labels=summary.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Expense Distribution")
    plt.show()


# Export Summary
def export_summary(df):
    if df.empty:
        print("\nNo data available!\n")
        return

    summary = df.groupby("Category")["Amount"].sum()
    summary.to_csv("expense_summary.csv")

    print("✅ Summary exported to expense_summary.csv\n")


# Main Menu
def main():
    df = load_data()

    while True:
        print("================================")
        print("      EXPENSE TRACKER")
        print("================================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category Summary")
        print("5. Monthly Report")
        print("6. Show Chart")
        print("7. Export Summary")
        print("8. Exit")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            df = add_expense(df)

        elif choice == "2":
            show_expenses(df)

        elif choice == "3":
            total_expense(df)

        elif choice == "4":
            category_expense(df)

        elif choice == "5":
            monthly_report(df)

        elif choice == "6":
            show_chart(df)

        elif choice == "7":
            export_summary(df)

        elif choice == "8":
            print("\nThank You for Using Expense Tracker!")
            break

        else:
            print("❌ Invalid Choice!\n")


if __name__ == "__main__":
    main()