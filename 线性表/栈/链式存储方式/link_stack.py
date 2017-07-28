class LinkNode():
    def __init__(self,x):
        self.val=x
        self.next=None

class LinkStack():
    def __init__(self):
        self.top=None

    def show_nodes(self):
        node=self.top
        while node:
            print node.val,'=>',
            node=node.next
        print None


    def stack_empty(self):
        if self.top:
            return False
        else:
            return True

    def get_top(self):
        if self.top:
            return self.top
        else:
            print 'empty stack'
            return None

    def push(self,x):
        if self.top:
            p=LinkNode(x)
            p.next=self.top
            self.top=p
        else:
            self.top=LinkNode(x)

    def pop(self):
        if not self.top:
            print 'empty stack'
            return None
        else:
            x=self.top.val
            self.top=self.top.next
            return x

    def stack_length(self):
        k=self.top
        l=0
        while k:
            k=k.next
            l+=1
        return l

x=LinkStack()
x.show_nodes()
x.push(1)
x.push(2)
x.push(3)
x.push(5)
print x.stack_length()
# print x.pop()
x.show_nodes()

