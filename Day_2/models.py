# This file contains the building blocks for our logistics system

class Package:
    def __init__(self, package_id, supplier_id, destination_id, content="Standard Item"):
        # Unique tracking ID for the package
        self.package_id = package_id
        
        # Who is shipping it (The Supplier/Enterprise Client)
        self.supplier_id = supplier_id
        
        # Where it's going (The Regional Category/Store)
        self.destination_id = destination_id
        
        # What is inside
        self.content = content
