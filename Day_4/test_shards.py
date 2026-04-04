import sys
import os

# Add root to path so we can import from Day_2
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_2.models import Package
from Day_4.shards import GlobalDispatcher

def test_distributed_network():
    print("Welcome to NexGen Logistics: Day 4")
    print("We are transitioning from one Central Hub to a 3-Hub Network.")
    
    # Initialize our system with 3 Distribution Hubs
    dispatcher = GlobalDispatcher(num_hubs=3)
    
    print("\nOur Global Dispatcher is now online.")
    print("However, we haven't given the Dispatcher any routing rules yet.")
    
    # Simulate an incoming package
    pkg = Package("TRK-8888", "Supplier_X", "West_Region")
    
    # Hand it to the dispatcher...
    print(f"Handing Package {pkg.package_id} to the Dispatcher...")
    dispatcher.dispatch_package(pkg)
    
    # Check if it was stored
    dispatcher.get_network_status()
    
    print("\nConclusion: The hubs are ready, but without routing logic, packages are being lost at the gate!")

if __name__ == "__main__":
    test_distributed_network()
