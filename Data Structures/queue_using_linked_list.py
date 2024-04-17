class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return ("Cannot dequeue element... Queue is Empty!!", None)
        
        data = self.front.data
        self.front = self.front.next
        return data
        
    def printQueue(self):
        current = self.front
        if current:
            while current != self.rear:
                print(current.data, end=" ")
                current = current.next
            print(current.data)
        else:
            pass
        
def main():
    queue = Queue()

    while(True):
        print("""
Available Options: 
1. Enqueue
2. Dequeue
3. Print the queue
4. Exit
""")
        choice = int(input("Enter your choice: "))

        if(choice == 1):
            item = int(input("Enter an item to enqueue: "))
            queue.enqueue(item)
            queue.printQueue()

        elif(choice == 2):
            item = queue.dequeue()
            if type(item) == tuple:
                print(item[0])
                pass
            else:
                print("Dequeued item: ", item)
            queue.printQueue()

        elif(choice == 3):
            queue.printQueue()

        else:
            exit('Program Exited...')

if __name__ == '__main__':
    main()