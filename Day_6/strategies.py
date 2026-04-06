import sys
import os

# Import from Previous Days
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_4.shards import GlobalDispatcher

class RegionalDispatcher(GlobalDispatcher):
    """
    Routes packages based on the destination region.
    Logic: Hub_Index = hash(region_name) % Total_Hubs
    """
    
    def get_target_hub(self, destination_id):
        # Convert destination string into a numerical index
        numeric_id = sum(ord(char) for char in str(destination_id))
        hub_index = numeric_id % len(self.hubs)
        return self.hubs[hub_index]

    def dispatch_package(self, package):
        target_hub = self.get_target_hub(package.destination_id)
        target_hub.store_package(package)
