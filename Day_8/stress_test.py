import sys
import os

# Add root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_2.models import Package
from Day_8.advanced_manager import AdvancedDispatcher

def run_stress_test():
    print("--- NexGen Logistics: Day 8 (The Final Stress & Failure) ---")
    
    # Start with 3 hubs
    dispatcher = AdvancedDispatcher(num_hubs=3)
    
    print("\n[STEP 1: NORMAL SPIKE]")
    # 3,000 packages arrive
    for i in range(3000):
        pkg = Package(f"TEST-{i}", "Multi_Client", "Anywhere")
        dispatcher.dispatch_package(pkg)
        
    dispatcher.perform_load_audit()
    print("Result: Our Math (Hashing) kept the network perfectly balanced during the spike.")

    print("\n[STEP 2: PHYSICAL FAILURE]")
    # One hub goes offline
    dispatcher.simulate_crash(hub_id=0)
    
    print("\nAnother 3,000 packages arrive while Hub 0 is offline...")
    dropped_count = 0
    for i in range(3000, 6000):
        pkg = Package(f"TEST-{i}", "Multi_Client", "Anywhere")
        success = dispatcher.dispatch_package(pkg)
        if not success:
            dropped_count += 1
            
    dispatcher.perform_load_audit()
    
    print(f"\n--- Crisis Report ---")
    print(f"Total Packages Lost during Hub 0 Downtime: {dropped_count}")
    print("Wait... Why did we lose 1,000 packages?")
    print("Because our Math-Based Router still tried to send 1/3 of the traffic to Hub 0")
    print("even though the building was completely offline!")
    print("\nConclusion: Math is perfect for balance, but we need 'Consistency' to handle failures.")

if __name__ == "__main__":
    run_stress_test()
