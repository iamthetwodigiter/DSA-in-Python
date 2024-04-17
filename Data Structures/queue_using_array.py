class Queue:
    def __init__(self, rear, front, size):
        self.front = rear
        self.rear = front
        self.data = None
        self.size = size
        self.arr = ['-'] * size

    def isFull(self):
        return self.rear == self.size - 1
    
    def isEmpty(self):
        return self.rear == self.front
    
    def enqueue(self, data):
        if(self.isFull()):
            print("Queue is Full... Cannot enqueue", data)
            return
        
        self.rear += 1
        self.arr[self.rear] = data

    def dequeue(self):
        if(self.isEmpty()):
            print("Queue is Empty... Cannot dequeue")
            return
        
        print("Dequeued element:", self.arr[self.front+1])
        self.arr[self.front+1] = -999
        self.front += 1

    def printQueue(self):
        if self.rear == -1:
            for i in range(self.size):
                print('-\t')
            return
        
        queue = ''
        for i in range(self.size):
            if not self.arr[i] == -999:
                queue += str(self.arr[i]) + '\t'
            else:
                queue += '-\t'
        print(queue,'\n')

def main():
    rear = front = -1
    size = int(input("Enter size of the queue: "))

    queue = Queue(rear, front, size)

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
            queue.printQueue()

        elif(choice == 3):
            queue.printQueue()

        else:
            exit('Program Exited...')

if __name__ == '__main__':
    main()