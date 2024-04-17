'''
This code is in reference to Stack implementation using Array in C Language

typedef struct stack {
    int data;
    int size;
    int top;
} stack;

'''

class Stack:
    def __init__(self, top, size):
        self.top = top
        self.size = size
        self.arr = ['-'] * size

    def isFull(self):
        return self.top == self.size - 1
    
    def isEmpty(self):
        return self.top == -1
    
    def push(self, item):
        if(self.isFull()):
            print(f'Stack Overflow... Cannot push {item}...')
            return None
            
        self.top += 1
        self.arr[self.top] = item
    
    def pop(self):
        if(self.isEmpty()):
            print("Stack Underflow")
            return None
        
        data = self.arr[self.top]
        self.arr[self.top] = '-'
        self.top -= 1
        return data

    def printStack(self):
        print(*self.arr)

def main():
    top = -1
    size = int(input("Enter size of the array: "))

    stack = Stack(top, size)

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
            if item != None:
                print(f"Popped element is {item}")
                stack.printStack()

        elif(choice == 3):
            stack.printStack()

        else:
            exit('Program Exited...')

if __name__ == '__main__':
    main()