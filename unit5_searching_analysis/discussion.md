# Unit 5 Discussion: Linear and Binary Search

GitHub repository: https://github.com/lseino/cmsc315-discussions/tree/main/unit5_searching_analysis

For my implementation, I used a student-score lookup scenario. Linear search examined each score from the beginning until it found the requested value, while binary search maintained low and high boundaries and repeatedly checked the middle of an already sorted score list. Both functions returned the matching index or `-1` when the score was absent. I tested small and large datasets as well as empty, single-element, first-position, last-position, and missing-value cases.

Binary search is faster on large sorted datasets because every comparison eliminates approximately half of the remaining values. Its worst-case running time is O(log n), while linear search may inspect all n values and therefore uses O(n) time. For example, binary search is appropriate when a student information system repeatedly looks up scores in a large sorted index.

Linear search can still be the better choice for a small or unsorted collection, such as checking a short list of newly entered scores before they have been organized. It requires no sorting cost and works regardless of item order.

Binary search is not usable directly when the data is unsorted because a middle comparison cannot reveal which half contains the target. It is also less suitable when records change so frequently that maintaining sorted order costs more than the searches save, or when the structure does not support efficient indexed access.
