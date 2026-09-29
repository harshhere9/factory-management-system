# data_manager.py
# Handles saving and loading text records
import os

inventory_data = {}
categories = set()

def save_to_file():
    try:
        file = open("factory_stock.txt", "w")
        for pid, prod in inventory_data.items():
            line = f"{pid},{prod.name},{prod.stock},{prod.price}\n"
            file.write(line)
        file.close()
    except Exception as e:
        print()
        print("!" * 50)
        print(f"Error saving data: {e}")
        print("!" * 50)
        print()

def load_from_file():
    if not os.path.exists("factory_stock.txt"):
        return
    
    from models import Product
    
    file = open("factory_stock.txt", "r")
    for line in file:
        parts = line.strip().split(",")
        if len(parts) == 4:
            p_id = parts[0]
            name = parts[1]
            stock = int(parts[2])
            price = float(parts[3])
            
            loaded_prod = Product(p_id, name, stock, price)
            inventory_data[p_id] = loaded_prod
    file.close()
