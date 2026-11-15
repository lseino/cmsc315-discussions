# Unit 5 Discussion: Searching and Analysis

## Overview

I implemented linear search and binary search in a student-score lookup scenario. Both functions returned the matching zero-based index and returned `-1` when the requested score was absent.

## Implementation

I completed every TODO section while preserving the original prompts. Linear search traversed the list from beginning to end and stopped at the first match. Binary search maintained inclusive lower and upper boundaries, calculated the middle index, and eliminated half of the remaining sorted range after each unsuccessful comparison.

The demonstration searched a small sorted score list for present and missing values. It also searched a sorted dataset containing 100,000 integers and showed that both algorithms returned the same index even though their comparison growth differed.

## Performance Analysis

Linear search used O(n) time in the worst case because it could inspect every element. Binary search used O(log n) time because each iteration halved the possible search range. Both iterative algorithms used O(1) additional working space.

Binary search required sorted, indexable data. It was not directly usable on an unsorted collection because a middle comparison could not determine which half to discard. Sorting first could also cost more than a simple linear scan when the dataset was small, changed frequently, or was searched only once. Linear search remained appropriate for small or unsorted collections and did not require preparation.

## Edge Cases

I tested an empty list, a single-element list, the first element, the last element, and a missing value. Empty and missing searches returned `-1`, while the boundary and single-element searches returned their correct indexes.

## Running the Program

From the repository root, I ran:

```bash
python3 unit5_searching_analysis/unit5_discussion.py
```

No external packages were required.

## Original Assignment Requirements

All instructor TODO prompts remained visible in `unit5_discussion.py`. The completed program implemented both algorithms, compared small and large sorted datasets, documented efficiency, and demonstrated multiple boundary conditions.
