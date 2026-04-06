# Day 6: Regional Routing (The Regional Hotspot)

## Today's Logistics Innovation
In Day 5, we learned that routing by **Supplier** was a disaster if one supplier was too big. Today, we tried a more logical approach: **Regional Routing**.

**The Logic**: All packages for the "West Coast" go to Hub 0. All packages for "International" go to Hub 1. 

## The Result
This fixed our Mega-Supplier problem! Even if one client sends millions of packages, they are likely shipping to different regions, meaning the load gets spread naturally across our network.

## The New Disaster: The "Flash Sale" Problem
In the real world, the "where" can be just as problematic as the "who." 

We simulated a **Global Flash Sale**. Suddenly, 10,000 packages were all bound for the **"International"** destination. Because our rule forces every package for a specific destination into the exact same hub, we created a **Regional Hotspot**.

* **Hub 1 (handled International)**: Overwhelmed and crashing.
* **Hub 0 & 2**: Sitting perfectly empty.

## Conclusion
Routing based on logical groups (Supplier or Region) will *always* create hotspots when one of those groups becomes popular. We need a way to distribute packages randomly enough to be balanced, but mathematically enough to actually find them later.

## How to Run
```bash
python3 Day_6/test_regional_hotspot.py
```
