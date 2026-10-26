"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self._items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Appending places the newest value on top so it can be removed first.
        self._items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            return None
        return self._items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Index -1 views the newest value while leaving the stack unchanged.
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self._items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self._items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # Appending at the back preserves the arrival order of queued values.
        self._items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            return None
        return self._items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Index 0 views the oldest value while leaving the queue unchanged.
        if self.is_empty():
            return None
        return self._items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self._items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO: EDITOR ACTION HISTORY ===")
    action_history = Stack()
    actions = (
        "Typed title",
        "Added paragraph",
        "Formatted heading",
        "Inserted citation",
    )

    for action in actions:
        action_history.push(action)
        print(f"Recorded action: {action}")

    print(f"Most recent action (peek): {action_history.peek()}")
    print("Undo order demonstrates LIFO:")
    while not action_history.is_empty():
        print(f"  Undid: {action_history.pop()}")

    print(f"Pop on an empty stack returned: {action_history.pop()}")
    print(f"Peek on an empty stack returned: {action_history.peek()}")

    single_action = Stack()
    single_action.push("Saved document")
    print(f"Single-item stack removed: {single_action.pop()}")
    print(f"Single-item stack is now empty: {single_action.is_empty()}")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO: HELP-DESK TICKETS ===")
    ticket_queue = Queue()
    tickets = (
        "Reset password",
        "Install printer",
        "Update software",
        "Restore network access",
    )

    for ticket in tickets:
        ticket_queue.enqueue(ticket)
        print(f"Queued ticket: {ticket}")

    print(f"Next ticket (front): {ticket_queue.front()}")
    print("Processing order demonstrates FIFO:")
    while not ticket_queue.is_empty():
        print(f"  Processed: {ticket_queue.dequeue()}")

    print(f"Dequeue on an empty queue returned: {ticket_queue.dequeue()}")
    print(f"Front on an empty queue returned: {ticket_queue.front()}")

    single_ticket = Queue()
    single_ticket.enqueue("Unlock account")
    print(f"Single-item queue removed: {single_ticket.dequeue()}")
    print(f"Single-item queue is now empty: {single_ticket.is_empty()}")


if __name__ == "__main__":
    main()
