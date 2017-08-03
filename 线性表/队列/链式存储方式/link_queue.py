class LinkNode():
    def __init__(self,x):
        self.val=x
        self.next=None

class LinkQueue():
    def __init__(self):
        self.head=None
        self.tail=None

    def show_nodes(self):
        node=self.head
        while node:
            print node.val,'=>',
            node=node.next
        print None

    def enqueue(self,x):
        if not self.head:
            self.head=LinkNode(x)
            self.tail=self.head
            return
        p=LinkNode(x)
        self.tail.next=p
        self.tail=self.tail.next

    def dequeue(self):
        if self.head:
            self.head=self.head.next
        else:
            print 'empty queue'

    def queue_empty(self):
        if self.head:
            return False
        else:
            return True

    def clear_queue(self):
        self.head=None

    def queue_length(self):
        k=self.head
        l=0
        while k:
            l+=1
            k=k.next
        return l

    def get_head(self):
        return self.head



y=LinkQueue()
y.enqueue(1)
print y.queue_length()
y.show_nodes()
y.enqueue(2)
print y.get_head()
print y.queue_length()
y.show_nodes()
y.dequeue()
y.show_nodes()
y.dequeue()
y.show_nodes()
print y.queue_empty()
y.dequeue()
y.show_nodes()
y.clear_queue()
y.show_nodes()