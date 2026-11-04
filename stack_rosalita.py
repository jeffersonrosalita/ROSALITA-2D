class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print(f"Pushed letter '{item}' -> Stack: {self.items}")

    def pop(self):
        if self.is_empty():
            print("Stack is already empty!")
            return None
        removed = self.items.pop()
        print(f"Popped letter '{removed}' -> Stack: {self.items}")
        return removed


if __name__ == "__main__":
    print("--- STACK IMPLEMENTATION (ROSALITA) ---")
    my_stack = Stack()

    # 1. Idagdag ang bawat titik ng ROSALITA
    last_name = "ROSALITA"
    print("\n[PHASE 1: Adding letters (Push)]")
    for letter in last_name:
        my_stack.push(letter)

    # 2. Alisin ang bawat titik hanggang maging empty
    print("\n[PHASE 2: Removing letters until empty (Pop)]")
    while not my_stack.is_empty():
        my_stack.pop()

    print("\nStack is now completely empty!")