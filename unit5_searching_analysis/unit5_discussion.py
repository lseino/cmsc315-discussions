"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # The loop may inspect all n elements, so worst-case running time is O(n).
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    low = 0
    high = len(lst) - 1

    while low <= high:
        middle = low + (high - low) // 2
        if lst[middle] == target:
            return middle
        if lst[middle] < target:
            # Sorted order eliminates the middle and the entire lower half.
            low = middle + 1
        else:
            # Sorted order eliminates the middle and the entire upper half.
            high = middle - 1

    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    small_scores = [55, 67, 72, 81, 90, 95]
    print(f"Sorted scores: {small_scores}")

    # Both searches return index 3 for 81 and -1 for the missing score 88.
    for target in (81, 88):
        print(
            f"Target {target}: linear index={linear_search(small_scores, target)}, "
            f"binary index={binary_search(small_scores, target)}"
        )

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    large_scores = list(range(1, 100_001))
    large_target = 99_999
    linear_index = linear_search(large_scores, large_target)
    binary_index = binary_search(large_scores, large_target)
    print(f"Dataset size: {len(large_scores):,}")
    print(f"Target {large_target}: linear index={linear_index}")
    print(f"Target {large_target}: binary index={binary_index}")
    # Linear search may check nearly 100,000 values here. Binary search needs
    # only about 17 comparisons because it halves the range on every step.
    print("Worst-case comparison growth: linear O(n), binary O(log n)")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    # Empty lists immediately return -1 because they have no valid index.
    print(f"Empty list, target 81: linear={linear_search([], 81)}, "
          f"binary={binary_search([], 81)}")

    # A single matching element is found at index zero by both algorithms.
    print(f"Single item [81], target 81: linear={linear_search([81], 81)}, "
          f"binary={binary_search([81], 81)}")

    # These tests confirm that both boundary indexes remain searchable.
    print(f"First value 55: linear={linear_search(small_scores, 55)}, "
          f"binary={binary_search(small_scores, 55)}")
    print(f"Last value 95: linear={linear_search(small_scores, 95)}, "
          f"binary={binary_search(small_scores, 95)}")


if __name__ == "__main__":
    main()
