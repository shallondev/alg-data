"""
Idea: "push" items to the stack on the stack and access items by "popping" them from the top
"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")
            return None

    def size(self):
        return len(self.items)


def main():
    # Initialize the stack
    stack = Stack()

    # Displays true because 
    print(stack.is_empty())

    # Add items to the stack
    stack.push("Minecraft")
    stack.push("Skyrim")
    stack.push("Doom")
    stack.push("FFVII")

    # No longer empty
    print(stack.is_empty())

    # Gets the top of the stack "FFVII" and removes it from stack
    get_item = stack.pop()

    # Display's the item we popped
    print(get_item)

    # Show's that "FFVII" is no longer in stack
    print(stack.items)

    # Show what item is next in the stack
    print(stack.peek())

if __name__ == "__main__":
    main()