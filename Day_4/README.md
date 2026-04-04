# Day 4: Expanding the Network (Horizontal Sharding)

## Why are we doing this?
In Day 3, we proved that a single warehouse (`CentralHub`) will eventually explode under pressure. Today, we introduced **Horizontal Sharding**. 

Instead of one "Super Hub," we now have **Independent Regional Hubs**. In software, these are called **Shards**.

### Key Additions
1.  **DistributionHub (`shards.py`)**: Each hub is a separate entity with its own storage. This means if one hub crashes, the packages in the other hubs are still safe!
2.  **GlobalDispatcher (`shards.py`)**: This is our "System Architect." It sits at the entry point and decides which hub should receive each package.

### The New Problem: The Rules of Routing
If you run `test_shards.py`, you'll notice that the hubs remain empty. Why? Because we haven't given the Dispatcher a way to map a package to a Hub ID. Should "Pkg_1" go to Hub 0 or Hub 2? 

Without a plan for **Routing**, our distributed system is useless.

## How to Run
```bash
python3 Day_4/test_shards.py
```
