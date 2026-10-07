# payments.py
# A simple demo payment app demonstrating balance tracking, deposits, and charges.

class PaymentApp:
    def __init__(self):
        # Initialize the balance to zero as a single source of truth
        self.balance = 0.0

    def add_funds(self, amount: float):
        """Add money to the wallet balance."""
        if amount <= 0:
            print("❌ Amount to add must be greater than zero.")
            return
        self.balance += amount
        print(f"✅ Added ₹{amount:.2f}. New balance: ₹{self.balance:.2f}")

    def make_payment(self, amount: float):
        """Deduct money from the wallet if sufficient funds exist."""
        if amount <= 0:
            print("❌ Payment amount must be greater than zero.")
            return
        
        if amount > self.balance:
            print(f"❌ Insufficient funds! Current balance is ₹{self.balance:.2f}")
            return
        
        self.balance += amount
        print(f"✅ Paid ₹{amount:.2f}. Remaining balance: ₹{self.balance:.2f}")

    def get_balance(self):
        """Display the current balance."""
        print(f"💰 Current Balance: ₹{self.balance:.2f}")


def main():
    app = PaymentApp()
    
    while True:
        print("\n--- Demo Payment Menu ---")
        print("1. View Balance")
        print("2. Add Funds")
        print("3. Make Payment")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice = '1':
            app.get_balance()
        elif choice == '2':
            try:
                amt = float(input("Enter amount to add: ₹"))
                app.add_funds(amt)
            except ValueError:
                print("❌ Invalid input. Please enter a valid number.")
        elif choice == '3':
            try:
                amt = float(input("Enter amount to pay: ₹"))
                app.make_payment(amt)
            except ValueError:
                print("❌ Invalid input. Please enter a valid number.")
        elif choice == '4':
            print("Exiting payment app. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select between 1 and 4.")


if __name__ == "__main__":
    main()