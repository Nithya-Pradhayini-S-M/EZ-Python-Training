'''class Node:
    def __init__(self,data):
        self.value=data
        self.next=None
head=tail=Node(10)

tail.next=Node(20)
tail=tail.next

tail.next=Node(30)
tail=tail.next

def front_insert(data):
   head=tail=Node(10)

   tail.next=Node(20)
   tail=tail.next

   tail.next=Node(30)
   tail=tail.next
   curr=None
   if head == None:
       print("List is empty")
   else:
       curr.next=head
       head=curr        

front_insert(50)


def display(head):
    if head == None:
        print("List is empty")
        return
    curr=head
    while curr != None:
        print(curr.value)
        curr=curr.next

display(head)'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_list:
    def __init__(self):
        self.head=None

#Read data from user
    def Read_Data(self):
      user_input = input("Enter data: ")
      self.end_insert(user_input)   #insert a new node at the end of the linked list

#Inserting Node at the Beginning
    def front_insert(self,data):
       new_node=Node(data)
       if self.head is None:          #the list is empty (i.e., self.head is None), it sets the new node as the head of the list.
        self.head = new_node
        return
       else:
        new_node.next = self.head
        self.head=new_node

#Inserting Node at the end
    def end_insert(self,data):
     new_node=Node(data)
     if self.head is None:
        self.head=new_node
        return
     else:
        curr=self.head
        while(curr.next):
            curr=curr.next
        curr.next=new_node

#Delete Node from front
    def front_delete(self):
     if self.head is None:  
        return
     self.head=self.head.next

#Delete Node from end
    def end_deletion(self):
     if self.head is None:
        return
     else:
        curr=self.head
        while(curr.next.next):
            curr=curr.next
        curr.next=None

#Printing the linked list
    def print_link_list(self):
     curr=self.head
     while curr:
        print(curr.data, end=" ")
        curr=curr.next
     print()

#Size of linked_list
    def size(self):
     count = 0
     curr = self.head
     while curr:
        count += 1
        curr = curr.next
     return count

# Create a new Linked List
LL = Linked_list()

# Menu-driven interface
while True:
    print("\nMenu:")
    print("1. Read data")
    print("2. Insert at front")
    print("3. Insert at end")
    print("4. Delete from front")
    print("5. Delete from end")
    print("6. Print linked list")
    print("7. Get size of linked list")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        LL.Read_Data()
    elif choice == 2:
        data = input("Enter data to insert at front: ")
        LL.front_insert(data)
    elif choice == 3:
         data = input("Enter data to insert at end: ")
         LL.end_insert(data)
    elif choice == 4:
        LL.front_delete()
    elif choice == 5:
        LL.end_deletion()
    elif choice == 6:
        LL.print_link_list()
    elif choice == 7:
        print("Size of the linked list:", LL.size())
    elif choice == 8:
        break
    else:
        print("Invalid choice. Please try again.")







    