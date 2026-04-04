# Day 3: Scaling Bottlenecks (Logistics Edition)

## The Challenge

In **Day 2**, we built a simple centralized logistics system. Today, we push that system to its limits by simulating a massive event: **The Black Friday Global Rush**.

## The Experiment

We used `load_simulator.py` to flood our `CentralHub` with **100,000 packages** in a single burst. Our goal was to see how a single in-memory inventory behaves under high load.

## Observations

### 1. Memory Inflation
While Python's lists are efficient at appending, storing every single package as an object in a single list consumes significant RAM. 
- **The Risk:** In a real-world system processing millions of packages, a single server would eventually run out of memory (OOM) and crash.
- **Data Persistence:** Because the `CentralHub` is entirely in-memory, a crash means every record of every package is lost instantly.

### 2. The Search "Wall"
When we needed to find a specific package (e.g., for a status update), we had to perform a **Linear Search**.
- **Performance:** As the list grows, searching becomes visibly slower. 
- **O(n) Complexity:** Search time grows 1:1 with the number of packages. Searching 1,000,000 packages takes 10x longer than 100,000.

## Key Insights for System Design

1.  **Vertical Scaling Limits:** You can only add so much RAM to one server before it becomes too expensive or impossible.
2.  **The Need for Databases:** Moving from a simple list to a database allows for **Indexing**, which turns O(n) searches into O(log n) or O(1).
3.  **Horizontal Scaling:** Instead of one giant Hub, we need to distribute packages across multiple nodes (Sharding).

## How to Run

Execute the simulation to see the bottlenecks in action:
```bash
python3 load_simulator.py
```

Observe how memory usage and search times correlate with the volume of data.
