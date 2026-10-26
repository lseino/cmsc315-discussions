import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Queue;

/**
 * A simple ticket management system that demonstrates the use of
 * queues and stacks in Java.
 *
 * <p>Tickets are stored in a queue and processed in FIFO
 * (first-in, first-out) order. Processed ticket actions are stored
 * in a stack to support undo functionality using LIFO
 * (last-in, first-out) behavior.</p>
 *
 * <p>This project demonstrates common queue and stack operations
 * including adding, previewing, processing, and undoing actions.</p>
 *
 * @author lseino
 * @version 1.0
 */
public class Unit2Project {

    private Queue<String> ticketQueue = new ArrayDeque<>();
    private Deque<String> actionStack = new ArrayDeque<>();

    /**
     * Adds a new ticket to the end of the queue.
     *
     * <p>Tickets are processed in FIFO (first-in, first-out) order.</p>
     *
     * @param ticket the ticket description to add
     * @throws IllegalArgumentException if the ticket is null or empty
     */
    public void addTicket(String ticket) {
        // Reject unusable descriptions before they can enter the queue.
        if (ticket == null || ticket.trim().isEmpty()) {
            throw new IllegalArgumentException("Ticket cannot be null or empty.");
        }

        // offer adds at the back so tickets retain FIFO arrival order.
        ticketQueue.offer(ticket);
    }

    /**
     * Returns the next ticket in the queue without removing it.
     * <p>
     * This method allows previewing the ticket at the front of the queue
     * while preserving the queue state (FIFO order is unchanged).
     *
     * @return the next ticket in the queue, or a message indicating that
     *         no tickets are available if the queue is empty
     */
    public String peekNextTicket() {
        // peek reads the FIFO head without changing the queue or its size.
        String nextTicket = ticketQueue.peek();
        return nextTicket == null ? "No tickets available." : nextTicket;
    }

    /**
     * Processes the next ticket in the queue.
     *
     * <p>This method removes the ticket from the front of the queue
     * and records the action in the action history stack.</p>
     *
     * @return the ticket that was processed, or
     *         "No tickets to process." if the queue is empty
     */
    public String processNextTicket() {
        // poll removes the oldest queued ticket and safely returns null if empty.
        String processedTicket = ticketQueue.poll();
        if (processedTicket == null) {
            return "No tickets to process.";
        }

        // push records a descriptive action at the top for LIFO undo behavior.
        actionStack.push("Processed ticket: " + processedTicket);
        return processedTicket;
    }

    /**
     * Undoes the most recent processed ticket action.
     *
     * <p>This method removes the last recorded action from the stack.
     * It does not restore the ticket to the queue.</p>
     *
     * @return the most recent action, or
     *         "No actions to undo." if there are no recorded actions
     */
    public String undoLastAction() {
        // poll removes the top (most recent) stack entry without throwing if empty.
        String lastAction = actionStack.poll();
        return lastAction == null ? "No actions to undo." : lastAction;
    }

    /**
     * Returns the number of tickets currently waiting in the queue.
     *
     * @return the number of pending tickets
     */
    public int getPendingTicketCount() {
        return ticketQueue.size();
    }

    /**
     * Returns the number of recorded actions in the history stack.
     *
     * @return the size of the action history stack
     */
    public int getActionHistorySize() {
        return actionStack.size();
    }

    public static void main(String[] args) {
        Unit2Project app = new Unit2Project();

        // Add tickets
        app.addTicket("Reset password");
        app.addTicket("Install printer");
        app.addTicket("Update software");

        System.out.println("Pending tickets: " + app.getPendingTicketCount());
        System.out.println("Next up (peek): " + app.peekNextTicket());

        // Process tickets
        System.out.println("\nProcessing ticket:");
        String processed = app.processNextTicket();
        System.out.println("Processed: " + processed);

        System.out.println("Pending tickets: " + app.getPendingTicketCount());
        System.out.println("Action history size: " + app.getActionHistorySize());

        // Process another ticket
        System.out.println("\nProcessing another ticket:");
        System.out.println("Processed: " + app.processNextTicket());

        System.out.println("Pending tickets: " + app.getPendingTicketCount());
        System.out.println("Action history size: " + app.getActionHistorySize());

        // Undo last action
        System.out.println("\nUndo last action:");
        System.out.println(app.undoLastAction());

        System.out.println("Action history size: " + app.getActionHistorySize());

        // Final state
        System.out.println("\nFinal state:");
        System.out.println("Pending tickets: " + app.getPendingTicketCount());
        System.out.println("Next up: " + app.peekNextTicket());
    }
}
