--> Problem Statement:

Small factory floor managers often rely on manual paper logs to track daily inventory production and note which machines are broken. This leads to lost data and inaccurate efficiency tracking.

--> Scope of the project:
	
This CLI-based application aims to digitize basic factory operations. It provides a simple, interactive menu to perform CRUD (Create, Read, Update) operations on factory stock, and automates daily machine checkups to provide a quick efficiency score. 

--> Target Users:
	
* Small-scale factory floor supervisors.
* Inventory managers.
* Maintenance staff (for checking audit logs).

--> High-level Features:
	
1. **Product CRUD:** Registering new factory items and updating their quantities after a manufacturing shift.
2. **Automated Auditing:** A module that tests the working state of registered machines to calculate a daily efficiency percentage.
3. **Local Storage:** Automatic reading and writing of data to local text files to ensure continuity between shifts.
