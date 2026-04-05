import sys
import os

# Import from Day 4 and Day 2
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_4.shards import GlobalDispatcher

class SupplierDispatcher(GlobalDispatcher):
    """
    Routes packages based on which supplier sent them.
    Logic: Hub_Index = Supplier_ID_Number % Total_Hubs
    """
    
    def get_target_hub(self, supplier_id):
        # Extract number from "Supplier_123"
        try:
            numeric_id = int(str(supplier_id).split("_")[1])
        except:
            # Fallback for non-standard IDs
            numeric_id = hash(supplier_id)
            
        hub_index = numeric_id % len(self.hubs)
        return self.hubs[hub_index]

    def dispatch_package(self, package):
        # 1. Look at the sender
        target_hub = self.get_target_hub(package.supplier_id)
        
        # 2. Assign package to that hub
        target_hub.store_package(package)
