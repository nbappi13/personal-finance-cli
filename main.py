"""Personal Finance Calculator CLI

A command-line tool for tracking income, expenses, and analyzing savings habits.
"""


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
            print("\n[STUB] Income entry selected.")
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

    