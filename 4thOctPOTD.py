class Solution:
    # Function to reverse a circular linked list
    def reverse(self, head):
        if head is None or head.next == head:
            return head  # Empty list or single node, no need to reverse

        prev = None
        curr = head
        original_head = head

        while curr.next != original_head:  # Traverse until we are about to loop back
            next_node = curr.next  # Store the next node
            curr.next = prev  # Reverse the pointer
            prev = curr  # Move prev forward
            curr = next_node  # Move curr forward

        # Handle the final node (when curr == original_head)
        next_node = curr.next
        curr.next = prev
        head.next = curr  # Make the last node point to the new head
        head = curr

        return head

    # Function to delete a node from the circular linked list
    def deleteNode(self, head, key):
        if head is None:
            return None  # Empty list, nothing to delete

        curr = head

        # Special case: If head node is to be deleted
        if head.data == key:
            # If there's only one node in the list
            if head.next == head:
                del head  # Use 'del' to remove reference
                return None

            # Find the last node in the list to update its next pointer
            last = head
            while last.next != head:
                last = last.next

            # Update the last node's next pointer and delete the head
            last.next = head.next
            temp = head
            head = head.next
            del temp  # Use 'del' to remove reference
            return head

        # Traverse the list to find the node with the given key
        while curr.next != head:  # Stop if we return to the head
            if curr.next.data == key:
                temp = curr.next
                curr.next = curr.next.next  # Unlink the node
                del temp  # Use 'del' to remove reference
                return head
            curr = curr.next

        # If key wasn't found
        return head
