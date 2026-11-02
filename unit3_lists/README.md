# Unit 3 Discussion: List Operations

## Overview

This assignment examined insertion, deletion, and searching in Python lists. I implemented a small playlist manager because an ordered song collection made the effects of each operation easy to see.

## Implementation

I completed the starter's `insert_at`, `delete_at`, and `search_value` functions while retaining every TODO prompt. `insert_at` used `list.insert` to place a song at a requested position. `delete_at` validated the index before using `pop`, returned the removed song for a valid operation, and returned `None` for an invalid operation. `search_value` used an explicit linear search and returned the first matching index or `-1` when no match existed.

The demonstration inserted songs at the beginning, middle, and end of a playlist. It then removed songs from all three positions and searched for both present and missing songs. Each operation printed the affected value and updated list.

## Edge Cases and Extension

The program inserted the first song into an empty playlist and safely handled deletion from an empty list. It also rejected an out-of-range index, a negative index, and a non-integer index without changing the list. As an additional test beyond the starter examples, I searched a playlist containing duplicate song titles and confirmed that the linear search returned the first match.

## Performance Analysis

Python lists are dynamic arrays. Inserting or deleting at the beginning or middle required later elements to shift and therefore took O(n) time in the worst case. Insertion at the end was normally amortized O(1), and deletion from the end was O(1). The linear search took O(n) time because it might inspect every item. The playlist used O(n) memory for n songs.

A linked list might outperform an array-based list when an application frequently inserted or removed nodes at known positions, especially near the beginning, because links could be updated without shifting the remaining items. A Python list was the better choice for this playlist demonstration because it preserved order, supported direct O(1) indexed access, and was simple to display. A real streaming service could use an ordered list for a user's playback queue or viewing history.

## Running the Program

From the repository root, I ran:

```bash
python3 unit3_lists/unit3_discussion.py
```

No external packages were required.

## Discussion Board Reflection

I learned how insertion, deletion, and linear searching affected both a Python list's contents and its performance. I implemented a playlist manager so every operation had an understandable purpose. Inserting at the beginning or middle shifted later songs to the right, while deleting from those positions shifted songs left. In contrast, operations at the end avoided most shifting. My main challenge was defining safe index behavior. Python normally permits negative indexes, but I used an explicit valid range from zero through the final index so invalid requests returned `None` consistently instead of modifying an unexpected song. I also used `-1` to represent an unsuccessful search and added tests for empty lists, invalid indexes, missing songs, and duplicate titles. These operations matter in real applications because shifting or sequentially scanning a large collection can become expensive when it happens frequently. A dynamic array works well when fast indexed access is important, while a linked list can be more efficient when an application repeatedly inserts or removes items at already-known node positions. The exercise showed me that selecting a list implementation depends on the operations the application performs most often.

## Original Assignment Requirements

All instructor TODO prompts remained visible in `unit3_discussion.py`. The completed program demonstrated insertion and deletion at the beginning, middle, and end; successful and unsuccessful searches; multiple edge cases; a customized real-world playlist scenario; and comments explaining behavior and performance.
