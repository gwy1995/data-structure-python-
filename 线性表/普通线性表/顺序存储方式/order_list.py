class OrderList():
    def __init__(self):
        self.length=0
        self.array=list()

    def clear_list(self):
        self.__init__()

    def list_empty(self):
        if self.length:
            return False
        else:
            return True

    def get_elem(self,i):
        if i>=self.length or i<0:
            print 'out of range'
        else:
            return self.array[i]

    def loacate_elem(self,n):
        for index,x in enumerate(self.array):
            if x==n:
                return index
        else:
            return -1

    def list_insert(self,i,n):
        if i>=self.length or i<0:
            print 'out of range'
            return False
        else:
            self.array.append(self.array[self.length-1])
            j=self.length-1
            while j>i:
                self.array[j]=self.array[j-1]
                j-=1
            self.array[i]=n
            self.length+=1
            print 'success'

    def list_delete(self,i):
        if i>=self.length or i<0:
            print 'out of range'
            return False
        j=i
        while j<self.length-1:
            self.array[j]=self.array[j+1]
            j+=1
        del self.array[self.length-1]
        self.length-=1
        print 'success'

    def list_length(self):
        return self.length

    def append(self,n):
        self.array.append(n)
        self.length+=1
