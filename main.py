
"""Personal Finance Calculator CLI

A command-line tool for tracking income, expenses, and analyzing savings habits.
"""

def get_valid_amount(prompt_message):
    """Prompting the user for a numeric value and validating it using Phase 1 string methods

    and guard clauses. Ensureing input is positive and numeric.
    """
    while True:
        raw_input = input(prompt_message).strip()

        # Guard clause 1: empty input check (falsy string)
        if not raw_input:
            print("❌ Input cannot be empty. Please try again.")
            continue

        # clean common user inputs
        cleaned_input = raw_input.replace("$", "").replace(",", "")

        # guard clause 2: checking if numeric (allowing decimal point)
        # replacing the first decimal point to validate floats via isnumeric/isdigit equivalent logic
        test_str = cleaned_input.replace(".", "", 1)
        if not test_str.isdigit():
            print("❌ Invalid entry. Please enter a valid positive number.")
            continue

        # safe conversion to float
        amount = float(cleaned_input)

        # guard clause 3
        if amount <= 0:
            print("❌ Amount must be greater than 0.")
            continue

        return amount


def handle_income(current_income):
    """Displaying current income and updating it using get_valid_amount()."""
    print(f"\n--- INCOME MANAGEMENT ---")
    if current_income > 0:
        print(f"Currently Monthly Income: {current_income:,.2f}")

    new_income = get_valid_amount("Enter your total monthly income: $")
    print(f"✅ Total income updated to: ${new_income:,.2f}")
    return new_income


def get_expense_category():
    """Displays a category menu and returns a clean category name."""
    categories = {
        "1": "Housing & Rent",
        "2": "Food & Groceries",
        "3": "Utilities & Bills",
        "4": "Transportation",
        "5": "Entertainment",
    }

    print("\n--- SELECT EXPENSE CATEGORY ---")
    for key, name in categories.items():
        print(f"{key}. {name}")
    print("6. Other / Custom Category")

    while True:
        choice = input("\nSelect a category (1-6): ").strip()

        # Guard clause for valid option selection
        if choice in categories:
            return categories[choice]
        elif choice == "6":
            custom_cat = input("Enter custom category name: ").strip().title()
            if not custom_cat:
                print("❌ Category name cannot be blank.")
                continue
            return custom_cat
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 6")    


def handle_expense(expenses):
    """Prompts for expense category and amount, then updates the expenses dictionary."""
    category = get_expense_category()
    amount = get_valid_amount(f"Enter amount spent on '{category}': $")

    # Accumulator pattern for dictionary values
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

    print(f"✅ Logged ${amount:,.2f} under '{category}' .")
    print(f" Total for '{category}': ${expenses[category]:,.2f}")

def main():
    # Application state (Data Store)
    total_income = 0.0
    expenses = {}  # will populate this with category: amount pairs

    print("========================================")
    print("   WELCOME TO PERSONAL FINANCE CLI   ")
    print("========================================\n")

    while True:
        # 1. Display Menu
        print("\n--- MAIN MENU ---")
        print("1. Set / Update Total Monthly Income")
        print("2. Add an Expense")
        print("3. View Financial Summary & Advice")
        print("4. Exit")

        # 2. Getting User Choice
        choice = input("\nSelect an option (1-4): ").strip()

        # 3. Guard Clause: Empty or Invalid choice
        if not choice or choice not in ("1", "2", "3", "4"):
            print("❌ Invalid selection. Please enter a number between 1 and 4.")
            continue

        # Command Routing 
        if choice == "1":
            total_income = handle_income(total_income)
            # Will implement handle_income() here next

        elif choice == "2":
            handle_expense(expenses)

        elif choice == "3":
            print("\n[STUB] Summary selected.")
            # Will implement handle_summary() here next

        elif choice == "4":
            print("\nThank you for using Personal Finance CLI. Goodbye!")
            break


if __name__ == "__main__":
    main()

    