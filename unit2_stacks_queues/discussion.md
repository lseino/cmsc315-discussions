# Unit 2 Discussion: Stacks, Queues, and Predictable Processing

**GitHub Repository:** https://github.com/lseino/cmsc315-discussions

I designed the application around two familiar workflows. Incoming help-desk tickets entered a queue, while recent editor actions entered a stack. Each structure had methods for adding, removing, viewing, and checking for an empty state. I handled empty operations safely so they returned clear results instead of crashing the program.

A stack uses last-in, first-out (LIFO) order because the newest item is removed first. This behavior fits an undo history: the most recent change must be reversed before an earlier change. A queue uses first-in, first-out (FIFO) order because items leave in arrival order. This fits a help desk or coffee-shop line, where the earliest request or customer should be served first.

The main challenge was confirming that viewing an item did not remove it and that empty operations behaved consistently. Testing empty and single-item structures helped verify these edge cases. Memory usage grows linearly, or O(n), because every added item requires another stored reference. Removing an item releases its reference. The list-backed stack and deque-backed queue provide efficient end operations, while `deque.popleft()` avoids the shifting cost of removing the first element from a regular Python list.
