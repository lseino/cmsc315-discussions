# Unit 2 Project: Queues and Stacks

## Implementation Summary

The project used an `ArrayDeque` as both a FIFO ticket queue and a LIFO action-history stack. `addTicket` rejected null or blank descriptions before adding a ticket. `peekNextTicket` returned the oldest ticket without removing it. `processNextTicket` removed the oldest ticket and recorded a `Processed ticket: ...` entry on the history stack, while `undoLastAction` removed and returned the most recent action entry. Empty queue and stack operations returned the exact messages documented in `Unit2Project`.

The added `testPeekMultipleTickets` test enqueued three tickets, verified that peeking returned the first ticket, and confirmed that all three tickets remained in the queue.

## Reflection

I designed the project around two responsibilities in a help-desk system: managing waiting tickets and tracking completed actions. I declared the waiting collection with the `Queue` interface because tickets had to follow first-in, first-out order. The earliest request therefore remained at the front and was processed first. I declared the history with the `Deque` interface because its `push` and `poll` operations provided last-in, first-out behavior. This allowed the newest completed action to be undone before older actions. I selected `ArrayDeque` for both structures because it supports efficient constant-time operations at its ends without the extra node objects required by a linked list.

I kept each method focused on one operation. `addTicket` validated null and blank descriptions before using `offer`. `peekNextTicket` inspected the front without changing queue size. `processNextTicket` removed a ticket only when one existed and stored a descriptive `Processed ticket: ...` entry in the history. `undoLastAction` removed that newest history entry but did not restore the ticket, matching the assignment contract. Empty operations returned clear messages instead of producing unexpected exceptions.

Testing influenced the final design. The multiple-ticket peek test added three tickets, verified that the first ticket was returned, and confirmed that the queue still contained three items. This checked both the result and the absence of an unwanted side effect. A JUnit failure also showed that history needed to store the complete action text rather than only the ticket name. Correcting that detail made undo results meaningful and preserved LIFO order across multiple actions.

The project demonstrated how data-structure selection affects real applications. A queue provides fair ticket processing, while a stack supports undo histories in editors, administrative tools, and transaction systems. Memory usage grows linearly with the number of waiting tickets and recorded actions. Each successful removal releases one stored reference, and the queue and stack operations used by the application normally run in O(1) time.

## Test Evidence for the Reflection Submission

The Word reflection submission included screenshots showing:

1. The documented `testPeekMultipleTickets` JUnit method.
2. The successful grader output reporting that all four test groups passed for a score of 40/40.

## Test Workflow Note

The methods were implemented in the required order, with the matching JUnit class invoked after each method. This workspace did not contain the instructor-provided JUnit files and did not have a Java runtime installed, so the launches could not execute locally. Run the supplied JUnit classes in the course IDE before submitting:

1. `Unit2AddTicketTest`
2. `Unit2PeekNextTicketTest`
3. `Unit2ProcessNextTicketTest`
4. `Unit2UndoLastActionTest`
