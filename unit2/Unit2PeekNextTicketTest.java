import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class Unit2PeekNextTicketTest {

    @Test
    void testPeekMultipleTickets() {
        // Create a fresh ticket system for this test.
        Unit2Project project = new Unit2Project();

        // Add three tickets in the order in which they should be processed.
        project.addTicket("Reset password");
        project.addTicket("Install printer");
        project.addTicket("Update software");

        // Peek at the first ticket without removing it from the queue.
        String nextTicket = project.peekNextTicket();

        // Verify that FIFO order makes the first added ticket the next ticket.
        assertEquals("Reset password", nextTicket);

        // Verify that peeking did not change the number of queued tickets.
        assertEquals(3, project.getPendingTicketCount());
    }
}
