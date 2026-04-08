# Day 8: Systems Evolution (Stress & Failure)

## The Final Evolution
In Day 7, we achieved a perfectly balanced workload across our network using hashing. But real-world logistics isn't just about perfect storage—it's about **Resilience**.

In Day 8, we added two critical features:
1.  **Monitoring**: A "Load Audit" to detect hotspots.
2.  **Health Tracking**: Each hub now has an `is_online` status.

## The Experiment
We ran a stress test (`stress_test.py`) that simulated two events:
1.  **A massive traffic spike**: 3,000 packages. Our hashing logic handled this perfectly, splitting the load to exactly 1,000 per hub.
2.  **A Physical Disaster**: We "crashed" Hub 0 (simulating a regional power failure).

## The Catastrophe
When Hub 0 went offline, the system kept running. But our dispatcher was still blindly using the math: `Tracking_ID % 3`.

*   **1/3 of all incoming traffic** (approx 1,000 packages) was still being sent to Hub 0.
*   Because Hub 0 was offline, those 1,000 packages just **disappeared**. 
*   In the real world, this would mean 1,000 customers calling customer support to ask where their package went.

## Conclusion
We have reached the limit of basic Sharding. Our math was biased toward fixed numbers (Hub 0, 1, 2). When the world changed (a hub died), our math didn't adapt. 

The next step would be **Consistent Hashing**—a technique where packages automatically "flow" to the next available hub if their target is offline. But for now, we have learned the most important lesson in system design: **Balance is half the battle; Availability is the other half.**

## How to Run
```bash
python3 Day_8/stress_test.py
```
