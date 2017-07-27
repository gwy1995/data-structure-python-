class LinkNode():
    def __init__(self,x):
        self.val=x
        self.next=None

class LinkList():
    def __init__(self):
        self.head=None

    def show_nodes(self):
        node=self.head
        while node:
            print node.val,'=>',
            node=node.next
        print None

    def create_head_insert(self,x):
        self.head=None
        for v in x:
            p=LinkNode(v)
            p.next=self.head
            self.head=p

    def create_tail_insert(self,x):
        self.head=LinkNode(None)
        tail=self.head
        for v in x:
            p=LinkNode(v)
            tail.next=p
            tail=tail.next
        self.head=self.head.next

    def insert_link_list(self,n,v):
        if n==0:
            p=LinkNode(v)
            p.next=self.head
            self.head=p
            print 'success'
            return True
        else:
            k=self.head
            for i in range(n-1):
                k=k.next
                if not k:
                    print 'index error'
                    return False
            p=LinkNode(v)
            p.next=k.next
            k.next=p
        print 'success'
        return True

    def delete_link_list(self,n):
        if n==0:
            v=self.head.val
            self.head=self.head.next
            return v
        k=self.head
        for i in range(n-1):
            k=k.next
            if not k.next:
                print 'index error'
                return False
        v=k.next.val
        k.next=k.next.next
        return v

    def list_empty(self):
        if self.head:
            return False
        else:
            return True

    def clear_list(self):
        self.head=None

    def list_length(self):
        k=self.head
        l=0
        while k:
            l+=1
            k=k.next
        return l

    def get_elem(self,n):
        if n>=self.list_length():
            return 'out of range'
        if n==0:
            return self.head.val
        else:
            k=self.head
            j=0
            while j<n:
                k=k.next
                j=j+1
            return k.val

    def locate_elem(self,n):
        k=self.head
        i=0
        while k:
            if k.val==n:
                return i
            i+=1
            k=k.next
        return -1



y=LinkList()
y.create_head_insert([1,2,3,4,5])
y.show_nodes()
y.create_tail_insert([1,2,3,4,5])
y.show_nodes()
y.insert_link_list(0, 0)
y.show_nodes()
y.delete_link_list(2)
y.show_nodes()
print y.list_empty()
print y.get_elem(4)
print y.list_length()
print y.locate_elem(10)
y.clear_list()
y.show_nodes()

# insert_link_list(link, 1, 5)
# show_nodes(link)

# # delete
# def delete_link_list(l,n):
#     if n==0:
#         v=l.val
#         l=l.next
#         return v
#     k=l
#     for i in range(n-1):
#         k=k.next
#     v=k.next.val
#     k.next=k.next.next
#     return v
# delete_link_list(link, 0)
# show_nodes(link)


# def change(l):
#     p=LinkNode(0)
#     l=p
# change(link)
# show_nodes(link)