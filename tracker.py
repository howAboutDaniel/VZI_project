def main():
    print(f"Welcome to your Ledger")
    # Get user input for expense!
    get_user_input()

    # Write the expense to a file!
    log_expense()
    # Read the file and summ expenses!
    summarize()

def get_user_input(): # Funkcia pre vytvorenie uživateľvho výdaju
    print("Record an expense!")
    expense_name = input("Enter your expense name")
    print(f"Expense name entered: {expense_name}")
    
def log_expense():
    print("Saving your expense")

def summarize():
    print("Preview of your expenses: ")

if __name__ == "__main__": # Comment! 9'33"
    main()