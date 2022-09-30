
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, new):
        alreadyStart = self.head
        node = Node(new, alreadyStart)
        self.head = node

    def insert_at_end(self, new):
        if self.head is None:
            node = Node(new, None)
            self.head = node
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(new, None)

    def remove_at_start(self):
        self.head = self.head.next

    def remove_at_last(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            itr = self.head
            while itr.next.next:
                itr = itr.next
            itr.next = None
    def search(self, data):
        if self.head is None:
            print("Empty")
        else:
            itr = self.head
            found = False
            while itr:
                if data == itr.data:
                    found = True
                    break
                itr = itr.next
            if found:
                print("True")
            else:
                print("False")

    def print(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            itr = self.head
            string = ''
            while itr:
                string = string + str(itr.data) + '--->'
                itr = itr.next
            print(string)

def main():
    ll = LinkedList()

    ll.insert_at_beginning(58)
    ll.insert_at_beginning(100)
    ll.insert_at_beginning(33434)
    ll.insert_at_beginning(934)

    ll.print()

    ll.remove_at_last()

    ll.print()

    ll.search(100)
    ll.search(1)


main()

