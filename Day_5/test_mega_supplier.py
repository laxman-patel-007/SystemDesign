import sys
import os

# Add root to path so we can import from previous days
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_2.models import Package
from Day_5.strategies import SupplierDispatcher

def test_mega_supplier_load():
    print("--- NexGen Logistics: Day 5 (The Mega-Supplier Problem) ---")
    
    # Setup our 3 distribution hubs with supplier-based routing
    dispatcher = SupplierDispatcher(num_hubs=3)
    
    print("\n[PART 1: NORMAL OPERATIONS]")
    # 30 small local vendors send 10 packages each
    for vendor_id in range(1, 31):
        for p_idx in range(10):
            pkg = Package(f"LOCAL-{vendor_id}-{p_idx}", f"Supplier_{vendor_id}", "Local_Delivery")
            dispatcher.dispatch_package(pkg)
            
    dispatcher.get_network_status()
    print("Conclusion Part 1: Load is distributed nicely among the 3 hubs.")

    print("\n[PART 2: THE MEGA-SUPPLIER ARRIVES]")
    # One giant corporation sends 10,000 packages at once
    mega_corp = "Supplier_999" # 999 % 3 = 0. All will go to Hub 0.
    print(f"Mega-Supplier {mega_corp} is dumping 10,000 packages into the system...")
    
    for i in range(10000):
        pkg = Package(f"MEGA-{i}", mega_corp, "Global_Shipping")
        dispatcher.dispatch_package(pkg)
        
    dispatcher.get_network_status()
    
    print("\n--- The Failure Report ---")
    print("Because we route by Supplier, Hub 0 is now drowning under 10,000+ packages.")
    print("Meanwhile, Hub 1 and Hub 2 are sitting empty and wasting resources.")
    print("The system has failed to scale horizontally for our biggest client!")

if __name__ == "__main__":
    test_mega_supplier_load()
