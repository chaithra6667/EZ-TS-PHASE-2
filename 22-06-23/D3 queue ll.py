class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
class Queue:
    def _init_(self):
        self.head=None
        self.last=None
    def enqueue(self,data):
        if self.last is None:
            self.head=Node(data)
            self.last=self.head
        else:
            self.last.next=Node(data)
            self.last=self.last.next
    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return=self.head.data
            self.head=self.head.next
a=Queue()
while True:
    print('enqueue <value>')
    print('dequeue')
    print('quit')
