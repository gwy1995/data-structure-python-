class LinkNode():
    def __init__(self,x):
        self.val=x
        self.next=None



def show_nodes(l):
    while l:
        print l.val,'=>',
        l=l.next
    print None

x=[1,2,3,4,5]
# create LinkList
## head insert
link=None
for v in x:
    p=LinkNode(v)
    p.next=link
    link=p

show_nodes(link)

## tail insert
head=LinkNode(None)
tail=head
for v in x:
    p=LinkNode(v)
    tail.next=p
    tail=tail.next
link=head.next
show_nodes(link)


# insert 
def insert_link_list(l,n,v):
    if n==0:
        p=LinkNode(v)
        p.next=l
        l=p
        return
    else:
        k=l
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

insert_link_list(link, 0, 5)
show_nodes(link)

# delete
def delete_link_list(l,n):
    if n==0:
        v=l.val
        l=l.next
        return v
    k=l
    for i in range(n-1):
        k=k.next
    v=k.next.val
    k.next=k.next.next
    return v
delete_link_list(link, 0)
show_nodes(link)


def change(l):
    p=LinkNode(0)
    l=p
change(link)
show_nodes(link)