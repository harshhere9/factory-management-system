# audit.py
# Machine status and factory floor audits
import random
import math
import datetime
from models import Machine

machine_list = [
    Machine("M-01", "Assembly Conveyor"),
    Machine("M-02", "Automated Paint Rig"),
    Machine("M-03", "Hydraulic Press"),
    Machine("M-04", "Packaging Line")
]

def run_daily_audit():
    today = datetime.date.today()
    
    print()
    print("=" * 50)
    print(f"          DAILY AUDIT REPORT: {today}          ")
    print("=" * 50)
    print()
    
    working_machines = 0
    
    for m in machine_list:
        chance = random.randint(1, 10)
        
        if chance > 8:
            m.is_working = False
            print(f"  [ALERT] {m.name} ({m.m_id}) -> FAULT DETECTED")
        else:
            m.is_working = True
            working_machines += 1
            print(f"  [OK]    {m.name} ({m.m_id}) -> OPERATIONAL")
            
    print()
    print("-" * 50)
    
    total = len(machine_list)
    efficiency = math.floor((working_machines / total) * 100)
    
    print(f"  Machines Online    : {working_machines} / {total}")
    print(f"  Overall Efficiency : {efficiency}%")
    
    if efficiency < 50:
        print()
        print("  ** WARNING: Factory running below minimum capacity! **")
        
    print("=" * 50)
    print()
