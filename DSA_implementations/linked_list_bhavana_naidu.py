class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def print(self):
        itr=self.head
        if itr is None:
            print("Empty linked list:)")
            return
        s=''
        while itr:
            s+=str(itr.data)+'  '
            itr=itr.next
        print(s)
    def get_length(self):
        if self.head is None:
            return 0
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    def insert_at_beginning(self,data):
        new = Node(data,self.head)
        self.head=new
    def insert_at_end(self,data):
        if self.head is None:
            self.insert_at_beginning(self,data)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data)

    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            print("Enter valid index:")
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                new=Node(data,itr.next)
                itr.next=new
                break
            itr=itr.next
            count+=1
    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            print("ONly valid index please")
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
    def insert_values(self,data_list):
        for data in data_list:
            self.insert_at_end(data)
        self.print()
    def insert_after_value(self,value,data):
        if self.head is None:
            print("Empty linked list")
            return
        itr= self.head
        while itr:
            if itr.data==value:
                itr.next=Node(data,itr.next)
                return
            itr=itr.next
        print("Value not found in the linked list")
    def remove_by_value(self,data):
        if self.head is None:
            print("Empty linked list:)")
            return
        itr=self.head
        while itr.next:
            if itr.next.data==data:
                itr.next=itr.next.next
                return
            itr=itr.next
        print("No such value found:)")
    def remove_at_beginning(self):
        if self.head is None:
            print("Already empty")
            return
        if self.get_length()==1:
            self.head=None
            return
        self.head=self.head.next
    def remove_at_end(self):
        if self.head is None:
            print("Already empty")
            return
        if self.get_length()==1:
            self.head=None
            return
        itr = self.head
        while itr.next.next:
            itr=itr.next
        itr.next=None

l=LinkedList()
while True:
    print("1 for insertion at beginning: ")
    print("2 for insertion at end: ")
    print("3 for inserting values from a list: ")
    print("4 for inserting at an index: ")
    print("5 for inserting after value: ")
    print("6 for remove by value: ")
    print("7 for remove at index: ")
    print("8 for remove at beginning: ")
    print("9 for remove at end: ")
    print("10 for length: ")
    print("11 for printing")
    opt=int(input())
    if opt==1:
        l.insert_at_beginning(input("Enter data to be inserted: "))
    elif opt==2:
        l.insert_at_end(input("Enter data to be inserted: "))
    elif opt==3:
        l.insert_values(input("Enter data: ").split())
    elif opt==4:
        l.insert_at(int(input("Enter index: ")), input("Enter data: "))
    elif opt==5:
        l.insert_after_value(input("Enter existing value: "), input("Enter data"))
    elif opt==6:
        l.remove_by_value(input("Enter data: "))
    elif opt==7:
        l.remove_at(int(input("Enter index: ")))
    elif opt==8:
        l.remove_at_beginning()
    elif opt==9:
        l.remove_at_end()
    elif opt==10:
        print(l.get_length())
    elif opt==11:
        l.print()
    else:
        break
            
            
            
