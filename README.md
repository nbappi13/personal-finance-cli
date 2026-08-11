# Personal Finance Calculator CLI

A professional, terminal-based financial planning application written in python. This tool helps users track monthly income, categorize spending, calculate net cash flow and saving rates, and receive automated, data-driven financial advice.

---

## Key Features

- **Interactive CLI Loop**: Non-blocking command interface driven by input validation and routing.

- **Robust Input Cleaning**: Automatically handles messy user inputs, stripping commas & symbols cleanly.

- **Categorized Expense Accumulation**: Log expenses across standard categories or dynamic custom categories using dictionary accumulation patterns.

- **Financial Ratios & Metrics**: Real-time calculations for Total Expenses, Net Monthly savings/Deficit, and Savings Rate percentages.

- **Smart Advisory Engine**: Automated checks analyzing savings benchmarks and highlighting disproportionate cost centers.

- **Aligned Terminal Presentation**: Custom formatted tables using advanced python f-string aligned and padding.

---

## Python Concepts Applied
This application was engineered purely with foundational python constructs:

- **Data Structures**: Dictionary for category-amount mapping, Tuples for immutable option sets.

- **Control Flow**: `while` loops, `if/elif/else` branching, and **Guard Clause Patterns** for early validation exits.

- **String Manipulation**: Methods like `.strip()`, `.title()`, `.replace()`, and `.isdigit()`.

- **Formatting**: Advanced f-string formatting for visual alighnment.

- **Software Standards**: Strict adherence to **PEP 8** naming conventions & module structure.

---

## Installation & Usage Guide

### Prerequisites
- Python 3.8 or higher installed on your machine.

## How to Run

1. **Clone the repository**:
```bash
git clone [https://github.com/nbappi13/personal-finance-cli.git](https://github.com/nbappi13/personal-finance-cli.git)
cd personal-finance-cli


--- Execute the script:

- Windows (PowerShell / Command Prompt):

python main.py


- macOS / Linux:
python3 main.py
