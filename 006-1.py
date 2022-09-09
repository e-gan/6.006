##################################################
# Problem 1. BackFront
##################################################

# Create a datastructure to support O(1) random access,
# and O(1) amortized inserts/deletes to the front and back end of the record


class BackFront():
    def __init__(self):
        self.R = []
        self.size=0
        self.capacity=0
        self.start=0
        
    def triple(self, key='front'):
        if self.size==0:
            self.R=[None]
            self.capacity=1
        else:
            new=[]
            if key=='front':
                new=[None] * self.capacity
                self.start+=self.capacity
            new.extend(self.R)
            if key=='back':
                new.extend([None] * self.capacity)
            self.R=new
            self.capacity=self.capacity*2
        
    def append(self, value):
        if self.capacity==0 or (self.capacity-self.start<=self.start+self.size):
            self.triple('back')
        self.R[self.start+self.size]=value
        self.size+=1
        
    def prepend(self,value):
        if self.start==0:
            self.triple('front')
        self.R[self.start-1]=value
        if self.start!=0:
            self.start-=1
        self.size+=1
    
    def delete_first(self):
        self.R[self.start]=None
        self.start+=1
        self.size-=1
    
    def delete_last(self):
        self.R[self.start+self.size-1]=None
        self.size-=1
        
    def __setitem__(self,key,value):
        self.R[self.start+key]=value
    
    def __getitem__(self,key):
        return self.R[self.start+key]
    
    def as_list(self):
        return [self.R[self.start + i] for i in range(self.size)]
            
    
        