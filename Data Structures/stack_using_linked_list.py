class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    # Initialise an empty Linked List
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            print("Stack Underflow...")
            return
        else:
            current = self.head
            self.head = self.head.next
            current.next = None
            print('Popped element is: ',current.data)
            del current

    def printStack(self):
        if self.head is None:
            print("Stack is Empty!!")
            return
        
        current = self.head
        stack = ''
        
        while current != None:
            stack += str(current.data) + '\t'
            current = current.next
        print(stack+'\n')

def main():
    stack = Stack()

    while(True):
        print("""
Available Options: 
1. Push
2. Pop
3. Print the Stack
4. Exit
""")
        choice = int(input("Enter your choice: "))

        if(choice == 1):
            item = int(input("Enter an item to push: "))
            stack.push(item)
            stack.printStack()

        elif(choice == 2):
            item = stack.pop()
            stack.printStack()

        elif(choice == 3):
            stack.printStack()

        else:
            exit('Program Exited...')

if __name__ == '__main__':
    main()