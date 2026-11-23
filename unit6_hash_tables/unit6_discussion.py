"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    print("\n=== INSERT OPERATIONS ===")
    inventory = {}

    # A dictionary behaves like a hash table: each unique SKU key is hashed so
    # Python can associate it with one quantity value and find it efficiently.
    inventory["P100"] = 15
    inventory["P200"] = 9
    inventory["P300"] = 22
    inventory["P400"] = 7
    inventory["P500"] = 31
    print(f"Inventory after five inserts: {inventory}")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    # Python hashes each requested SKU and uses equality checks as needed to
    # locate the matching entry. Typical dictionary lookup is average O(1).
    print(f"P100 quantity: {inventory['P100']}")
    print(f"P400 quantity: {inventory['P400']}")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print(f"Before updating P100: {inventory}")
    # Assigning P100 again replaces its value; it does not add a duplicate key.
    inventory["P100"] = 20
    print(f"After updating P100 to 20: {inventory}")

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print(f"Before deleting P300: {inventory}")
    # pop removes both the P300 key and its associated quantity from the table.
    removed_quantity = inventory.pop("P300")
    print(f"Removed P300 quantity: {removed_quantity}")
    print(f"After deleting P300: {inventory}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    # get returns the provided default instead of raising KeyError for P999.
    print(f"Missing P999 lookup: {inventory.get('P999', 'SKU not found')}")

    # pop with a default safely reports a missing deletion and changes nothing.
    size_before = len(inventory)
    missing_removal = inventory.pop("P999", None)
    print(f"Missing P999 removal result: {missing_removal}")
    print(f"Size unchanged after missing removal: {len(inventory) == size_before}")

    # An empty dictionary supports the same safe lookup behavior.
    empty_inventory = {}
    print(f"Lookup in empty inventory: {empty_inventory.get('P100', 'SKU not found')}")

    # Different keys can produce the same table location (a collision). Python
    # resolves collisions internally, but many collisions can add comparisons
    # and reduce lookup performance from its usual average O(1) behavior.
    print("Collision note: more collisions can require extra key comparisons.")


if __name__ == "__main__":
    main()
