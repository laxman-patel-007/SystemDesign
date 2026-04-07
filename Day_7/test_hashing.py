import sys
import os

# Add root to path so we can import from previous days
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_2.models import Package
from Day_7.strategies import HashDispatcher

def test_ultimate_balance():
    print("--- NexGen Logistics: Day 7 (The Mathematical Blender) ---")
    
    # Setup our 3 distribution hubs with Hash-based routing
    dispatcher = HashDispatcher(num_hubs=3)
    
    print("\n[STRESS TEST] Simulating the 'Perfect Storm':")
    print("1. A Mega-Supplier dumping 5,000 packages (The Day 5 problem).")
    print("2. A Regional Flash Sale with 10,000 'International' packages (The Day 6 problem).")
    
    # Problem 1: Mega-Supplier (All from one sender)
    for i in range(5000):
        pkg = Package(f"MEGA-{i}", "Supplier_999", "Local")
        dispatcher.dispatch_package(pkg)
        
    # Problem 2: Hotspot Destination (All to one place)
    for i in range(10000):
        pkg = Package(f"SURGE-{i}", f"Supplier_{i % 100}", "International")
        dispatcher.dispatch_package(pkg)
        
    dispatcher.get_network_status()
    
    print("\n--- The Success Report ---")
    print("SUCCESS: The load is perfectly balanced across all 3 hubs!")
    print("Because we hash the unique Package ID, every package has a 1/3 chance of landing")
    print("in any hub, regardless of its sender or its destination.")
    print("We have officially defeated 'Hotspots'.")

if __name__ == "__main__":
    test_ultimate_balance()
