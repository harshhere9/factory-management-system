---> Small Factory Management System <---

--> Overview:
	
This is a beginner-friendly Python project built for managing small-scale factory operations. It allows users to track product inventory, manage stock levels after production, and simulate daily machine audits to calculate factory efficiency.

--> Features:
	
* **Inventory Management:** Add new products and update stock using a dictionary.
* **Category Tracking:** Uses Python sets to keep track of unique product categories.
* **Daily Audit Simulation:** Uses the `random` and `math` modules to simulate machine breakdowns and calculate factory efficiency percentage.
* **Data Persistence:** Saves all inventory data automatically to `factory_stock.txt` so no data is lost when closing the program.

--> Technologies/Tools Used:
	
* Python 3.x
* Standard Libraries used: `os`, `random`, `math`, `datetime`

--> Steps to install & run the project:
	
1. Download or clone this repository.
2. Make sure you have Python installed on your computer.
3. Open a terminal or command prompt in the project folder.
4. Run the command: `python main.py`

--> Instructions for testing:
	
* Start the program and choose option 1 to add a product (e.g., ID: P01, Name: Gear, Stock: 50, Price: 15.5).
* Choose option 2 to check if it displays correctly.
* Close the program (Option 6) and restart it. Choose option 2 again—your data will still be there because it loads from the text file.
* Run Option 5 a few times to test the randomized audit system.
