import sys
import os

# Import from Day 7
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_7.strategies import HashDispatcher

class AdvancedDispatcher(HashDispatcher):
    """
    Day 8: Adding monitoring and failure handling.
    """
    def __init__(self, num_hubs):
        super().__init__(num_hubs)
        # Add a health state to each hub
        for hub in self.hubs:
            hub.is_online = True
            
    def dispatch_package(self, package):
        target_hub = self.get_target_hub(package.package_id)
        
        # Check if the hub is functional before sending
        if not target_hub.is_online:
            # Disaster! The package disappears into the void
            return False
            
        target_hub.store_package(package)
        return True
        
    def perform_load_audit(self):
        # Calculate load percentage across the network
        total_pkgs = sum(len(h.inventory) for h in self.hubs)
        if total_pkgs == 0: return
        
        print("\n--- Network Load Audit ---")
        for hub in self.hubs:
            usage = (len(hub.inventory) / total_pkgs) * 100
            status = "ONLINE" if hub.is_online else "OFFLINE (CRASHED)"
            print(f"Hub {hub.id} [{status}]: {usage:.1f}% load ({len(hub.inventory)} pkgs)")
            
    def simulate_crash(self, hub_id):
        print(f"\n!!! [ALARM] Hub {hub_id} has suffered a major power failure! !!!")
        for hub in self.hubs:
            if hub.id == hub_id:
                hub.is_online = False
