from models import Package
from server import CentralHub

def run_simulation():
    print("Welcome to NexGen Logistics: Day 2")
    print("Setting up our first Central Hub...")
    
    # Initialize the single warehouse
    hq_hub = CentralHub()
    
    # Simulate 10 packages arriving from different suppliers
    for i in range(1, 11):
        pkg_id = f"TRK-{1000 + i}"
        supplier = f"Supplier_{i % 3}" # Simulating a few different suppliers
        destination = "East_Region"
        
        # Create a package object
        pkg = Package(pkg_id, supplier, destination)
        
        # Log it into the Central Hub
        hq_hub.receive_package(pkg)
        print(f"Logged: Package {pkg_id} from {supplier} has arrived.")

    print("\n--- Daily Operations Complete ---")
    hq_hub.status_report()

if __name__ == "__main__":
    run_simulation()
