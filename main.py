
"""Personal Finance Calculator CLI

A command-line tool for tracking income, expenses, and analyzing savings habits.
"""

def get_valid_amount(prompt_message: str) -> float:
    """Prompts the user for a numeric value and validates it.
    Applies string cleaning, guard clauses, and type conversion to ensure
    the input is a valid positive float.

    Args:
        prompt_message (str): The prompt message to display to the user.
    
    Returns:
        float: A validated positive dollar amount
    """
    while True:
        raw_input = input(prompt_message).strip()

        # Guard clause 1: empty input check 
        if not raw_input:
            print("❌ Input cannot be empty. Please try again.")
            continue

        # clean common floating inputs
        cleaned_input = raw_input.replace("$", "").replace(",", "")

        # Guard Clause 2: Check if string is numeric (allowing one decimal point)
        test_str = cleaned_input.replace(".", "", 1)
        if not test_str.isdigit():
            print("❌ Invalid entry. Please enter a valid positive number.")
            continue

        # safe conversion to float
        amount = float(cleaned_input)

        # guard clause 3: logical validation
        if amount <= 0:
            print("❌ Amount must be greater than 0.")
            continue

        return amount


def handle_income(current_income: float) -> float:
    """Displaying current income and updating it using get_valid_amount()."""
    print("\n--- INCOME MANAGEMENT ---")
    if current_income > 0:
        print(f"Currently Monthly Income: {current_income:,.2f}")

    new_income = get_valid_amount("Enter your total monthly income: $")
    print(f"✅ Total income updated to: ${new_income:,.2f}")
    return new_income


def get_expense_category() -> str:
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


def handle_expense(expenses: dict) -> None:
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



def get_financial_advice(
        income: float,
        savings_rate: float,
        expenses: dict
) -> list:

    """Generates personalized financial feedback using conditional logic and search"""
    advice_list = []

    # 1. Savings Rate Analysis
    if savings_rate >= 20.0:
        advice_list.append(
            "🌟 Excellent! Your are hitting or exceeding the recommended" 
            " 20% savings target."
        )
    elif savings_rate > 0:
        advice_list.append(
            " ⚠️ You have a positive cash flow, but your savins rate is"
            " below 20%. Try cutting non-essential spending."
        )
    else:
        advice_list.append(
            " 🚨DEFICIT ALERT!: You are spending more than you earn!"
            "Immediate expense reductions needed."
        )

    # 2. Highest Expense Category Search Patten
    if expenses:
        top_category = ""
        max_spent = 0.0
        for category, amount in expenses.items():
            if amount > max_spent:
                max_spent = amount
                top_category = category

        category_pct_of_income = (max_spent / income) * 100
        advice_list.append(f"📌 Largest Expense: '{top_category}' (${max_spent:,.2f} / {category_pct_of_income:.1f}% of income).")

        if category_pct_of_income > 40.0:
            advice_list.append(f"⚠️ Warning: '{top_category}' consumes over 40% of your income. Look into lowering this fixed cost")

    return advice_list



def handle_summary(income: float, expenses: dict) -> None:
    """Calculating metrics and printing a clean formated financial report."""
    # Guard Clause: Income required
    if income == 0.0:
        print("\n⚠️ Please set your total monthly income (Option 1) before viewing summary and advice.")
        return

    total_expenses = sum(expenses.values())
    net_savings = income - total_expenses
    savings_rate = (net_savings / income) * 100

    print("\n==============================================")
    print("         MONTHLY FINANCIAL SUMMARY            ")
    print("\n==============================================")
    print(f" Total Monthly Income : ${income:12,.2f} ")
    print(f" Total Expenses       : $ {total_expenses:12,.2f}")
    print("----------------------------------------------")
    if net_savings >= 0:
        print(f" Net Monthly Savings : ${net_savings:12,.2f}")
    else:
        print(f" Monthly Deficit     : ${abs(net_savings):12,.2f}")
    print(f" Savings Rate            : {savings_rate:12.1f}%")
    print("\n==============================================")

    # Category Breakdown Table
    if expenses:
        print("\n--- CATEGORY BREAKDOWN ---")
        for category, amount in expenses.items():
            percentage = (amount / income) * 100
            print(f" • {category:<20} : ${amount:9,.2f} ({percentage:5.1f}% of income)")

    # Smart Advice Section
    print("\n--- SMART FINANCIAL ADVICE ---")
    advice = get_financial_advice(income, savings_rate, expenses)
    for item in advice:
        print(f"{item}")
    print("----------------------------------------------")
        


def main() -> None:
    """Main application loop & command-line router"""
    total_income = 0.0
    expenses = {}  
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
            handle_summary(total_income, expenses)

        elif choice == "4":
            print("\nThank you for using Personal Finance CLI. Goodbye!")
            break


if __name__ == "__main__":
    main()

    