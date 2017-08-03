class Queue():
    def __init__(self,maxsize=0):
        self.maxsize=maxsize
        self.front=0
        self.rear=0
        if self.maxsize<=0:
            self.array=list()
        else:
            self.array=[None]*(self.maxsize+1)

    def clear_queue(self):
        self.__init__()

    def queue_empty(self):
        if self.front==self.rear:
            return True
        else:
            return False

    def get_head(self):
        if not self.queue_empty():
            return self.array[self.front]
        else:
            print 'queue is empty'

    def enqueue(self,n):
        if self.maxsize<=0:
            self.array.append(n)
            self.rear+=1
        else:
            if (self.rear+1)%(self.maxsize+1)==self.front:
                print 'full queue'
            else:
                self.array[self.rear]=n
                self.rear+=1
                if self.rear==self.maxsize+1:
                    self.rear=0

    def dequeue(self):
        if self.front==self.rear:
            print 'empty queue'
            return
        if self.maxsize<=0:
            n=self.array[0]
            del self.array[0]
            self.rear-=1
        else:
            n=self.array[self.front]
            self.front+=1
            if self.front==self.maxsize+1:
                self.front=0
        return n

    def queue_length(self):
        if self.maxsize<=0:
            return self.rear
        else:
            return (self.rear-self.front+self.maxsize)%self.maxsize
