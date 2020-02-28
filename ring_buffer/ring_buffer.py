from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        else:
            self.storage.length = self.capacity
            delete_head = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if delete_head == self.current:
                self.current = self.storage.tail
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        begin = self.current
        list_buffer_contents.append(begin.value)
        # TODO: Your code here
        if begin.next:
            nxt = begin.next
        else:
            nxt = self.storage.head
        while nxt != begin:
            list_buffer_contents.append(nxt.value)
            if nxt.next:
                nxt = nxt.next
            else:
                nxt = self.storage.head
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
