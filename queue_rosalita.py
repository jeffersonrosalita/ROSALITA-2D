class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued letter '{item}' -> Queue: {self.items}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is already empty!")
            return None
        removed = self.items.pop(0)
        print(f"Dequeued letter '{removed}' -> Queue: {self.items}")
        return removed


if __name__ == "__main__":
    print("--- QUEUE IMPLEMENTATION (ROSALITA) ---")
    my_queue = Queue()

    # 1. Idagdag ang bawat titik ng ROSALITA
    last_name = "ROSALITA"
    print("\n[PHASE 1: Adding letters (Enqueue)]")
    for letter in last_name:
        my_queue.enqueue(letter)

    # 2. Alisin ang bawat titik hanggang maging empty
    print("\n[PHASE 2: Removing letters until empty (Dequeue)]")
    while not my_queue.is_empty():
        my_queue.dequeue()

    print("\nQueue is now completely empty!")