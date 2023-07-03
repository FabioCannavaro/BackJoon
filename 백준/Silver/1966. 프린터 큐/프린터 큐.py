class Queue():
    def __init__(self):
        self.items=[]
        
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        return self.items.pop(0)
    
    def is_empty(self):
        return len(self.items)==0
    
    def size(self):
        return len(self.items)
    
def print_order(doc, target):
    queue=Queue()
    for i, d in enumerate(doc):
        queue.enqueue((i, d))
    cnt=0
    
    while not queue.is_empty():
        current_doc=queue.dequeue()
        
        if any(current_doc[1]<doc[1] for doc in queue.items):
            queue.enqueue(current_doc)
        else:
            cnt+=1
            
            if current_doc[0]==target:
                return cnt

num=int(input())
for i in range(num):
    
    n, m=map(int, input().split())
    doc=list(map(int, input().split()))
    printer=print_order(doc, m)
    print(printer)