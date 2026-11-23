# Unit 6 Discussion: Inventory Lookup with a Hash Table

GitHub repository: https://github.com/lseino/cmsc315-discussions/tree/main/unit6_hash_tables

I designed an inventory lookup application using a Python dictionary as a hash table. Each product SKU served as a unique key, and the associated value stored the current quantity. The program inserted five products, retrieved existing quantities, updated P100 without creating a duplicate key, and deleted P300. It also handled missing lookups, missing deletions, and an empty dictionary safely.

Hash tables normally provide average O(1) insertion, lookup, update, and deletion because the hash value directs the application toward the key's storage location. Collisions occur when different keys compete for the same internal location. The runtime resolves them, but frequent collisions can require more comparisons, reduce lookup efficiency, and make the application feel slower during high-volume inventory activity. Well-distributed hash values and adequate table capacity help control that cost.

I learned that dictionaries make key-value operations concise, but safe handling still matters. Lookup with `get` was straightforward. Deleting a missing SKU required more care because direct deletion could raise an exception, so I used `pop(key, default)` and verified that the inventory size remained unchanged. SKUs were appropriate keys because they uniquely and consistently identified products. From a user's perspective, these design choices allow a shopping or warehouse system to locate and update products quickly as the catalog grows. The exercise also showed that average constant-time performance depends on a suitable hash function and manageable collision frequency rather than being guaranteed for every possible input pattern.
