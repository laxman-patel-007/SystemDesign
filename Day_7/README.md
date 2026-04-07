# Day 7: Hash-Based Routing (The Math Approach)

## Today's Logistics Innovation
In Day 5 and 6, we learned that grouping packages by **Supplier** or **Region** is dangerous. If one group gets too big, the assigned server dies.

Today, we implemented **Hash-Based Routing**.

**The Logic**: We take the unique **Package ID** (Tracking Number) and run it through a mathematical blender called **MD5 hashing**. This produces a gigantic, unpredictable number. We then use the remainder (modulo) to pick a hub.

## Why it Works
Crucially, hashing the Tracking ID means that two packages from the *same* supplier or going to the *same* region will likely end up in *different* hubs. 

We threw our two worst-case scenarios at the system at once:
1.  A Mega-Supplier (5,000 packages).
2.  A Regional Flash Sale (10,000 packages).

The result? The load was split almost exactly **33.3% / 33.3% / 33.3%** across our 3 hubs. 

## The Trade-Off (Scatter-Gather)
We solved the scaling problem, but we created a new one: **Data Fragmentation**.
If a supplier calls us and asks: *"Where are all my 500 packages?"*, we no longer have a single place to look. We have to check every single hub in our global network and "gather" the results. 

Scaling is about making trade-offs!

## How to Run
```bash
python3 Day_7/test_hashing.py
```
