import time
import sys
import os

# Add parent directory to path so we can import Day_2 models
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from Day_2.models import Package
from Day_2.server import CentralHub

def simulate_logistics_rush():
    print("=== Global Logistics Simulation: Black Friday Event ===")
    
    hub = CentralHub()
    
    # We'll simulate 100,000 packages being processed in a single rush
    package_count = 100000
    print(f"\nIncoming! {package_count:,} packages are arriving at the Central Hub...")

    start_time = time.time()

    for i in range(1, package_count + 1):
        pkg_id = f"PKG-{i:06d}"
        supplier = f"Supplier_{i % 500}" # 500 different suppliers
        destination = f"Region_{i % 50}"  # 50 different destinations
        content = "High-Priority Seasonal Item"

        pkg = Package(pkg_id, supplier, destination, content)
        hub.receive_package(pkg)

        if i % 20000 == 0:
            print(f"... Hub has logged {i:,} packages ...")

    end_time = time.time()
    time_taken = end_time - start_time

    print("\n--- Logistics Rush Completed ---")
    hub.status_report()
    print(f"Time taken to log {package_count:,} packages: {time_taken:.4f} seconds.")

    # Calculate memory usage
    # sys.getsizeof() on the list only gives size of the list structure (pointers)
    list_mem = sys.getsizeof(hub.inventory)
    # Estimate total memory including object overhead (simplified)
    # Each Package object + its strings
    avg_obj_size = 256 # Rough estimate in bytes
    total_memory_est = list_mem + (package_count * avg_obj_size)

    print(f"Estimated Hub Memory Usage: ~{total_memory_est / (1024*1024):.2f} MB")

    print("\n--- The Search Bottleneck ---")
    print("Now, let's try to find a specific package 'PKG-099999' in the massive inventory...")

    search_start = time.time()
    
    target_id = "PKG-099999"
    found = False
    for pkg in hub.inventory:
        if pkg.package_id == target_id:
            found = True
            break
            
    search_end = time.time()
    
    if found:
        print(f"Package found!")
    else:
        print("Package not found (this shouldn't happen).")
        
    print(f"Time taken to search the entire list: {search_end - search_start:.5f} seconds.")

    print("\n--- Conclusion ---")
    print("1. Memory: Storing everything in a single list in memory grows linearly. At millions of packages, this crashes.")
    print("2. Search: Searching a list is O(n). Doubling the packages doubles the search time.")
    print("3. Single Point of Failure: If this Hub goes down, we lose track of 100,000 shipments.")

if __name__ == "__main__":
    simulate_logistics_rush()
