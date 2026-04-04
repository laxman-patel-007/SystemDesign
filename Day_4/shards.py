# This file defines our new Distributed Network structure.

class DistributionHub:
    def __init__(self, hub_id):
        # A unique identifier for this specific warehouse (e.g. Hub 0, Hub 1)
        self.id = hub_id
        
        # This hub's private inventory list. 
        # It doesn't know what's in other hubs!
        self.inventory = []

    def store_package(self, package):
        # Package arrives at THIS specific regional hub
        self.inventory.append(package)


class GlobalDispatcher:
    def __init__(self, num_hubs):
        # Create a network of multiple distribution hubs
        self.hubs = [DistributionHub(i) for i in range(num_hubs)]

    def dispatch_package(self, package):
        # A package arrives at the main gate.
        # We need to decide which Hub (0, 1, or 2) it should go to.
        #
        # (Status: Pending Instructions. We haven't set routing rules yet!)
        pass
        
    def get_network_status(self):
        # Check how busy every hub in the network is
        print("\n--- Global Network Status ---")
        for hub in self.hubs:
            print(f"Hub {hub.id}: {len(hub.inventory)} packages stored.")
