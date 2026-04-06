import sys
import os

# Add root to path so we can import from previous days
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_2.models import Package
from Day_6.strategies import RegionalDispatcher

def test_regional_surge():
    print("--- NexGen Logistics: Day 6 (The Regional Hotspot) ---")
    
    # Setup our 3 distribution hubs with regional routing
    dispatcher = RegionalDispatcher(num_hubs=3)
    
    print("\n[PART 1: THE MEGA-SUPPLIER IS COMPLIANT]")
    # Our old "Mega-Supplier" sends 500 packages spread across 5 regions.
    megacorp = "Supplier_999"
    regions = ["North", "South", "East", "West", "Central"]
    
    for i in range(500):
        dest = regions[i % len(regions)]
        pkg = Package(f"MEGA-{i}", megacorp, dest)
        dispatcher.dispatch_package(pkg)
            
    dispatcher.get_network_status()
    print("Conclusion Part 1: By routing by destination, even massive suppliers get spread out!")

    print("\n[PART 2: THE REGIONAL HOTSPOT]")
    # Suddenly, a huge trade promotion happens in the "International" sector.
    print("Worldwide Flash Sale! 10,000 orders bound for 'International' arrive...")
    
    for i in range(10000):
        pkg = Package(f"SURGE-{i}", "Random_Vendor", "International")
        dispatcher.dispatch_package(pkg)
        
    dispatcher.get_network_status()
    
    print("\n--- The Failure Report ---")
    print("Because our rule binds an entire Region to one Hub, an 'International' surge")
    print("completely crushed Hub 1 (which handles International) while Hub 0 and 2 are idling.")
    print("We moved the hotspot from 'Who' (Supplier) to 'Where' (Destination)!")

if __name__ == "__main__":
    test_regional_surge()
