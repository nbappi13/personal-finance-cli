
def get_valid_amount(prompt_message):
    while True:
        raw_input = input(prompt_message).strip()

        # Guard clause 1: empty input check (falsy string)
        if not raw_input:
            print("❌ Input cannot be empty. Please try again.")
            continue

        # clean common user inputs
        cleaned_input = raw_input.replace("$", "").replace(",", "")

        # guard clause 2: check if numeric (allowing decimal point)
        # replace the first decimal point to validate floats via isnumeric/isdigit equivalent logic
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
    # display the current income and update it
    print(f"\n---INCOME MANAGEMENT---")
    if current_income > 0:
        print(f"Currently Monthly Income: {current_income:,.2f}")

    new_income = get_valid_amount("Enter your total monthly income: $")
    print(f"✅ Total income updated to: ${new_income:,.2f}")
    return new_income


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

        # 2. Get User Choice
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
            print("\n[STUB] Expense entry selected.")
            # Will implement handle_expense() here next

        elif choice == "3":
            print("\n[STUB] Summary selected.")
            # Will implement handle_summary() here next

        elif choice == "4":
            print("\nThank you for using Personal Finance CLI. Goodbye!")
            break


if __name__ == "__main__":
    main()

    