# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explored stack and queue data structures through two real-world scenarios. An editor action history demonstrated last-in, first-out behavior, while a help-desk ticket line demonstrated first-in, first-out behavior.

## Implementation

I implemented the `Stack` class with a private Python list. `push` appended a value, `pop` removed the newest value, and `peek` viewed that value without changing the stack. I implemented the `Queue` class with `collections.deque`. `enqueue` appended a value at the back, `dequeue` removed the oldest value with `popleft`, and `front` viewed the oldest value without removing it. Both classes included `is_empty` methods.

The demonstration added four editor actions to the stack and removed them in reverse order to show LIFO behavior. It also added four support tickets to the queue and processed them in arrival order to show FIFO behavior. The output clearly labeled every addition, preview, removal, and final state.

## Edge Cases

The program tested `pop` and `peek` on an empty stack and `dequeue` and `front` on an empty queue. These operations returned `None` instead of raising an unexpected exception. Separate single-item tests removed the only value and confirmed that each structure became empty afterward.

## Efficiency and Memory

The stack used O(n) memory for n stored values, and the queue used O(n) memory for n queued values. List `append` and end `pop` ran in amortized O(1) time. A deque was chosen for the queue because `append`, `popleft`, and front access ran in O(1) time. Using `pop(0)` on a regular list would have required shifting the remaining values and taken O(n) time.

## Running the Program

From the repository root, I ran:

```bash
python3 unit2_stacks_queues/unit2_discussion.py
```

No external packages were required.
