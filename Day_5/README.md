# Day 5: Supplier-Based Routing (The Mega-Supplier Problem)

## Today's Logistics Innovation
In Day 4, our dispatcher had no rules. Today, we implemented **Supplier-Based Routing**.

**The Logic**: If a supplier sends a package, it is always processed by the same regional hub. This seems efficient—we know exactly where to find a supplier's inventory!

## The Result
Initially, this worked perfectly for 30 small local vendors. The load was split 10-10-10 between our 3 hubs.

## The Disaster
Then, an industrial giant (**Supplier_999**) arrived and injected 10,000 packages into our system. Because of our routing rule, **Hub 0** was assigned every single one of those packages.

* **Hub 0**: Overloaded and crashing.
* **Hub 1**: Idle.
* **Hub 2**: Idle.

## Lessons Learned
Routing based on **"WHO"** (the sender/user) creates dangerous hotspots. If one entity is significantly larger than the others, they will destroy the server assigned to them while the rest of the network stays empty.

We need a way to route packages based on *where* they are going instead.

## How to Run
```bash
python3 Day_5/test_mega_supplier.py
```
