# This represents our single Central Hub (the only warehouse we have)

class CentralHub:
    def __init__(self):
        # The master ledger of all packages received
        self.inventory = []
    
    def receive_package(self, package):
        # A new package arrives at the loading dock
        self.inventory.append(package)

    def status_report(self):
        # Check the total count of packages currently in the hub
        print(f"Total packages in Central Hub: {len(self.inventory)}")
