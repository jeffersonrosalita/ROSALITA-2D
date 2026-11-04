class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.display()

    def delete_head(self):
        if self.is_empty():
            print("Linked List is already empty!")
            return
        removed_data = self.head.data
        self.head = self.head.next
        print(f"Deleted head node '{removed_data}'")
        self.display()

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Current Linked List:", " -> ".join(elements) + " -> None" if elements else "Empty (None)")


if __name__ == "__main__":
    print("--- LINKED LIST IMPLEMENTATION (ROSALITA) ---")
    ll = LinkedList()

    # 1. Idagdag ang bawat titik ng ROSALITA
    last_name = "ROSALITA"
    print("\n[PHASE 1: Adding letters (Append)]")
    for letter in last_name:
        ll.append(letter)

    # 2. Alisin ang bawat titik hanggang maging empty
    print("\n[PHASE 2: Removing letters until empty (Delete)]")
    while not ll.is_empty():
        ll.delete_head()

    print("\nLinked List is now completely empty!")