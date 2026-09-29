# inventory.py
# Core operations for stock and inventory tracking
from models import Product
import data_manager

def add_new_product(p_id, name, stock, price, category):
    if p_id in data_manager.inventory_data:
        return (False, f"Product ID '{p_id}' already exists in records!")
    
    new_product = Product(p_id, name, stock, price)
    data_manager.inventory_data[p_id] = new_product
    data_manager.categories.add(category)
    
    data_manager.save_to_file()
    return (True, f"Product '{name}' registered successfully.")

def update_product_stock(p_id, added_amount):
    if p_id in data_manager.inventory_data:
        data_manager.inventory_data[p_id].stock += added_amount
        data_manager.save_to_file()
        return True
    else:
        return False

def show_all_inventory():
    print()
    print("=" * 50)
    print("               CURRENT FACTORY STOCK              ")
    print("=" * 50)
    print()
    
    if len(data_manager.inventory_data) == 0:
        print("  Notice: No inventory registered yet.")
    else:
        for pid, prod in data_manager.inventory_data.items():
            prod.display_info()
            
    print()
    print("-" * 50)
    print()

def show_categories():
    print()
    print("=" * 50)
    print("             ACTIVE PRODUCT CATEGORIES            ")
    print("=" * 50)
    print()
    
    if len(data_manager.categories) == 0:
        print("  Notice: No categories registered yet.")
    else:
        for cat in data_manager.categories:
            print(f"  * {cat}")
            
    print()
    print("-" * 50)
    print()
