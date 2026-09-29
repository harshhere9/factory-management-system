# main.py
# Main menu and execution loop
import inventory
import audit
import data_manager

def show_menu():
    print()
    print("=" * 50)
    print("        SMALL FACTORY MANAGEMENT SYSTEM         ")
    print("=" * 50)
    print("  [1] Add New Product")
    print("  [2] View All Inventory")
    print("  [3] View Registered Categories")
    print("  [4] Update Stock After Production")
    print("  [5] Run Floor Machine Audit")
    print("  [6] Save and Exit")
    print("=" * 50)
    print()

def start_program():
    data_manager.load_from_file()
    
    while True:
        show_menu()
        user_choice = input("Select an option (1-6): ").strip()
        print()
        
        if user_choice == '1':
            print("-" * 50)
            print("                NEW PRODUCT ENTRY                 ")
            print("-" * 50)
            print()
            
            p_id = input("Enter Product ID: ").strip()
            name = input("Enter Product Name: ").strip()
            category = input("Enter Category (e.g., Raw, Assembly): ").strip()
            
            try:
                stock = int(input("Enter Initial Stock Units: "))
                price = float(input("Enter Unit Price (INR): "))
                print()
                
                success, msg = inventory.add_new_product(p_id, name, stock, price, category)
                
                print("-" * 50)
                print(f"Status: {msg}")
                print("-" * 50)
                
            except ValueError:
                print()
                print("Error: Stock must be an integer and Price must be a decimal.")
                print("-" * 50)
                
        elif user_choice == '2':
            inventory.show_all_inventory()
            
        elif user_choice == '3':
            inventory.show_categories()
            
        elif user_choice == '4':
            print("-" * 50)
            print("               STOCK REPLENISHMENT                ")
            print("-" * 50)
            print()
            
            p_id = input("Enter Product ID to update: ").strip()
            
            try:
                amt = int(input("Enter manufactured units to add: "))
                print()
                
                if inventory.update_product_stock(p_id, amt):
                    print("-" * 50)
                    print(f"Status: Successfully added {amt} units to {p_id}.")
                    print("-" * 50)
                else:
                    print("-" * 50)
                    print(f"Status: Product ID '{p_id}' was not found.")
                    print("-" * 50)
                    
            except ValueError:
                print()
                print("Error: Quantity must be a valid integer.")
                print("-" * 50)
                
        elif user_choice == '5':
            audit.run_daily_audit()
            
        elif user_choice == '6':
            print("=" * 50)
            print("     All changes saved. Closing system. Goodbye!  ")
            print("=" * 50)
            print()
            break
            
        else:
            print("Invalid input. Please choose a number between 1 and 6.")
            print()

if __name__ == "__main__":
    start_program()
