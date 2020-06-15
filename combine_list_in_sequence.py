data=[  
        [5,6,7],[20,21,22,23],
        [15,16,17],[11,12,13,14],
        [8,9,10],[1,2,3,4],[30,31,32]
    ]
def test(data):
    answer= [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],[20,21,22,23],[30,31,32]]
    if len(data) == len(answer):
        count=0
        for d in data:
            if d in answer:
                count+=1
        if count==3:
            return True
    return False

def combine(data):
    def surround(point1BE,point2BE):
        b,e=point1BE
        b2,e2=point2BE
        if b==b2 and e==e2:
            return 0
        def connect(p1,p2):
            x=p1
            x2=p2
            if 0<=abs(x-x2)<=1:
                return True
            return False
        
        if connect(b,b2):
            return 1
        elif connect(b,e2):
            return 2
        elif connect(e,e2):
            return 3
        elif connect(e,b2):
            return 4
        return 0
    def modify(be,be2,s):
        if s==1:
            return be2[::-1]+be
        elif s==2:
            return be2+be
        elif s==3:
            return be+be2[::-1]
        elif s==4:
            return be+be2
    length = len(data)
    c=0
    while c!=length:
        d1=data[c]
        d1b=d1[0]
        d1e=d1[-1]
        for d2 in data:
            d2b=d2[0]
            d2e=d2[-1]
            connect = surround((d1b,d1e),(d2b,d2e))
            if connect:
                data.insert(0,modify(d1,d2,connect))
                data.remove(d1)
                data.remove(d2)
                length-=1
                break
        else:
            c+=1
    return data
                
    
    
    
value= combine(data)
print(value)
print(test(value))
