class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Insert Functions
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current = self.head
        position = 0

        if index < 0 or index > self.sizeOfLinkedList():
            print("Invalid index value.")
            return

        if index == 0:
            self.insertAtBegin(data)
        else:
            while(current!= None and position+1!= index):
                position +=1
                current = current.next

            if current!= None:
                new_node.next = current.next
                current.next = new_node
            else:
                print("Cannot insert.\nIndex value not present..")

    def insertEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while(current.next != None):
            current = current.next
        current.next = new_node

    def updateNode(self, data, index):
        current = self.head
        position = 0

        if index < 0 or index >= self.sizeOfLinkedList():
            print("Invalid index value.")
            return

        if index == 0:
            current.data = data
        else:
            while(current!= None and position!= index):
                position += 1
                current = current.next

            if current!= None:
                current.data = data
            else:
                print("Cannot update value.\nIndex not present..")

    # Delete Functions
    def deleteFirst(self):
        if self.head == None:
            return
        
        self.head = self.head.next

    def deleteLast(self):
        if self.head == None:
            return None

        if self.head.next == None:
            self.head = None
        else:
            current = self.head

            while(current.next.next != None):
                current = current.next
            
            current.next = None

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.sizeOfLinkedList():
            print("Invalid index value.")
            return

        if index == 0:
            self.deleteFirst()

        else:
            current = self.head
            position = 0

            while(current.next!= None and position+1!= index):
                position += 1
                current = current.next

            if current.next!= None:
                current.next = current.next.next
            else:
                print("Cannot delete.\nIndex not present..")

    def delete(self, data):
        current = self.head

        if current.data == data:
            self.deleteFirst()
            return

        while(current!= None and current.next.data!= data):
            current = current.next

        if current == None:
            return
        else:
            current.next = current.next.next

    # Size of Linked List
    def sizeOfLinkedList(self):
        size = 0

        if self.head:
            current = self.head
            while(current):
                size += 1
                current = current.next
            return size
        else:
            return 0

    # Print the Linked List
    def printLinkedList(self):
        current = self.head
        linked_list = ''

        if current == None:
            print("Linked list is empty.")
            return

        while(current):
            linked_list += str(current.data) + '\t'
            current = current.next

        print(linked_list+'\n')      

def main():
    node = LinkedList()

    print('''
1. Insert At Beginning
2. Insert At End
3. Insert At Particular Index
4. Update a Node
5. Delete First Node
6. Delete Last Node
7. Delete At Particular Index
8. Delete Node with Particular Value
9. Size of Linked List
10. Print the Linked List
Enter 0 to quit  
''')
    
    while True:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = input("Enter data to insert: ")
            node.insertAtBegin(data)
            node.printLinkedList()

        elif choice == 2:
            data = input("Enter data to insert: ")
            node.insertEnd(data)
            node.printLinkedList()

        elif choice == 3:
            data = input("Enter data to insert: ")
            index = int(input("Enter the index value: "))
            node.insertAtIndex(data, index)
            node.printLinkedList()

        elif choice == 4:
            data = input("Enter data to insert: ")
            index = int(input("Enter the index value: "))
            node.updateNode(data, index)
            node.printLinkedList()

        elif choice == 5:
            node.deleteFirst()
            node.printLinkedList()

        elif choice == 6:
            node.deleteLast()
            node.printLinkedList()

        elif choice == 7:
            index = int(input("Enter the index value: "))
            node.deleteAtIndex(index)
            node.printLinkedList()

        elif choice == 8:
            data = input("Enter data to delete: ")
            node.delete(data)
            node.printLinkedList()

        elif choice == 9:
            print("Size of Linked List: ", node.sizeOfLinkedList())

        elif choice == 10:
            node.printLinkedList()

        else:
            exit('Program Exited...')    

if __name__ == '__main__':
    main()