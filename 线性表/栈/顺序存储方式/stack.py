class Stack():
    def __init__(self):
        self.array=list()
        self.top=-1

    def destory_stack(self):
        del self.array
        del self.top

    def clear_stack(self):
        self.__init__()

    def stack_empty(self):
        if self.top==-1:
            return True
        else:
            return False

    def get_top(self):
        if self.top==-1:
            print 'empty stack'
            return None
        else:
            return self.array[self.top]

    def push(self,n):
        self.top+=1
        self.array.append(n)

    def pop(self):
        if self.top==-1:
            print 'empty stack'
            return None
        else:
            n= self.array[self.top]
            del self.array[self.top]
            self.top-=1
            return n

    def stack_length(self):
        return self.top+1