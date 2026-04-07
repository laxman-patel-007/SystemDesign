import sys
import os
import hashlib

# Import from Previous Days
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_4.shards import GlobalDispatcher

class HashDispatcher(GlobalDispatcher):
    """
    Routes packages by hashing the unique Package ID.
    Guarantees even distribution regardless of Supplier or Destination.
    """
    
    def get_target_hub(self, package_id):
        # We use MD5 to create a unique fingerprint of the Tracking ID
        hash_obj = hashlib.md5(str(package_id).encode())
        
        # Convert hex fingerprint to a large integer
        hash_number = int(hash_obj.hexdigest(), 16)
        
        # Distributed evenly across all hubs
        hub_index = hash_number % len(self.hubs)
        return self.hubs[hub_index]

    def dispatch_package(self, package):
        target_hub = self.get_target_hub(package.package_id)
        target_hub.store_package(package)
