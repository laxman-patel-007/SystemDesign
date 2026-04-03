# Day 2: The Basic Logistic Hub

Today, we built the foundation of NexGen Logistics. We have two main components:

1.  **Models (The Package)**: A blueprint for the data we move and store. Every package has an ID, a Supplier, and a Destination.
2.  **Server (The Central Hub)**: Our single warehouse. It has a list called `inventory` where it stores every package that arrives.

### The Problem with this Setup
If we stop here, we might think we've succeeded. But as we discussed in Day 1, this single list (`inventory`) will eventually grow too large for one computer's memory, and the single `receive_package` function will become a bottleneck when millions of packages try to arrive at the same time.

### How to Run
```bash
python3 Day_2/main.py
```
