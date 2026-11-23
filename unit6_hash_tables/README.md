# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

I implemented a Python inventory application that used a dictionary as a hash table. Each product SKU acted as a unique key, and its inventory quantity acted as the associated value.

## Implementation

I preserved every instructor TODO prompt and completed all required sections. The program created an empty dictionary, inserted five SKU-quantity pairs, retrieved two existing entries, replaced the quantity of an existing SKU, and removed an entry. Assigning P100 a second time updated its value without creating a duplicate key.

I also handled missing-key and empty-table edge cases safely. `dict.get` returned a clear fallback message for an absent SKU. `dict.pop` used a default value so deleting an absent SKU did not raise an exception or change the inventory size.

## Hashing and Performance

The dictionary hashed an SKU to help locate its key-value entry. Insertions, lookups, updates, and deletions normally used average O(1) time. A collision occurred when different keys competed for the same internal location. Python resolved collisions internally, but a high collision rate could require additional comparisons and reduce performance. Maintaining adequate capacity and using well-distributed hash values helped preserve efficient access.

## Edge Cases

The program demonstrated a missing lookup, safe deletion of a missing SKU, and lookup in an empty dictionary. It confirmed that a failed removal did not change the table's size.

## Running the Program

From the repository root, I ran:

```bash
python3 unit6_hash_tables/unit6_discussion.py
```

No external packages were required.

## Discussion Board Reflection

I learned how Python dictionaries connected unique keys to values and supported inventory operations without scanning every record. Using SKUs made the behavior clear because each product needed one stable identifier and one current quantity. The easiest operation was lookup with `get`, while safe deletion required more thought because indexing or deleting a missing key directly could raise an exception. I handled that case with `pop(key, default)` and confirmed that the dictionary size stayed unchanged. Hash tables normally provide average O(1) insertion, lookup, update, and deletion because a hash function directs a key toward its storage location. Collisions occur when different keys compete for the same internal location. The runtime resolves those conflicts, but excessive collisions require extra comparisons and can slow operations. A good hash distribution and appropriate table capacity reduce collision frequency. The exercise showed why hash tables work well for inventory applications: a warehouse can retrieve or update a product by SKU quickly even as the catalog grows, while safe missing-key handling keeps routine inventory mistakes from crashing the application.

## Original Assignment Requirements

All TODO prompts remained visible. The completed program demonstrated insertion, lookup, update, deletion, edge cases, collision analysis, and a real-world inventory scenario.
