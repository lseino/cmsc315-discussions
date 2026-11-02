"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # list.insert shifts the element at index and every later element right.
    # Inserting near the beginning is O(n), while inserting at the end avoids
    # shifting existing elements and is normally O(1) amortized.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Checking the bounds prevents IndexError and makes invalid operations
    # predictable for callers. Negative indexes are treated as invalid here so
    # the accepted range is explicit: zero through len(lst) - 1.
    if not isinstance(index, int) or isinstance(index, bool):
        return None
    if index < 0 or index >= len(lst):
        return None

    # pop returns the removed value. Elements after the index shift left, so
    # deleting near the beginning is O(n), while deleting the end is O(1).
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # This is a linear search because it checks values sequentially from the
    # beginning. It returns the first match and may examine all n elements.
    for index, item in enumerate(lst):
        if item == value:
            return index
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS: PLAYLIST MANAGER ===")
    playlist = ["Sunrise Drive", "Open Road", "Evening Lights"]
    print(f"Original playlist: {playlist}")

    # Index 0 inserts a song first and shifts all existing songs right.
    insert_at(playlist, 0, "Morning Coffee")
    print(f"After beginning insertion: {playlist}")

    # The midpoint keeps the playlist organized but shifts the later songs.
    middle_index = len(playlist) // 2
    insert_at(playlist, middle_index, "Midday Break")
    print(f"After middle insertion at index {middle_index}: {playlist}")

    # len(playlist) inserts after the final element without shifting songs.
    insert_at(playlist, len(playlist), "Night Drive")
    print(f"After end insertion: {playlist}")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    # Each call returns the deleted song so the user can confirm the operation.
    removed = delete_at(playlist, 0)
    print(f"Removed from beginning: {removed}; playlist: {playlist}")

    middle_index = len(playlist) // 2
    removed = delete_at(playlist, middle_index)
    print(
        f"Removed from middle index {middle_index}: {removed}; "
        f"playlist: {playlist}"
    )

    removed = delete_at(playlist, len(playlist) - 1)
    print(f"Removed from end: {removed}; playlist: {playlist}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    # The existing song returns its zero-based position.
    existing_song = "Midday Break"
    existing_index = search_value(playlist, existing_song)
    print(f"Found '{existing_song}' at index {existing_index}.")

    # A missing song returns the -1 sentinel instead of raising an exception.
    missing_song = "Ocean Air"
    missing_index = search_value(playlist, missing_song)
    print(f"Search for missing '{missing_song}' returned {missing_index}.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    empty_playlist = []

    # Insertion at index 0 safely adds the first item to an empty list.
    insert_at(empty_playlist, 0, "First Song")
    print(f"Inserted into an empty playlist: {empty_playlist}")

    # Invalid and empty deletions return None and leave the list unchanged.
    print(f"Delete at invalid index 99 returned: {delete_at(playlist, 99)}")
    print(f"Delete at negative index -1 returned: {delete_at(playlist, -1)}")
    print(f"Delete at non-integer index returned: {delete_at(playlist, 'first')}")
    print(f"Delete from an empty list returned: {delete_at([], 0)}")

    # An extra duplicate test demonstrates that linear search returns the first
    # matching index when a list contains the same value more than once.
    duplicate_playlist = ["Encore", "Acoustic Set", "Encore"]
    duplicate_index = search_value(duplicate_playlist, "Encore")
    print(
        "Duplicate search returned the first matching index: "
        f"{duplicate_index} in {duplicate_playlist}"
    )


if __name__ == "__main__":
    main()
