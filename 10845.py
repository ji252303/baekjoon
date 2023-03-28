import sys

q = list()				
n = int(sys.stdin.readline())			

for _ in range(n):
    cmd = sys.stdin.readline()		
    if "push" in cmd:				
        q.append(int(cmd.split(' ')[1]))
    elif "pop" in cmd:				
        if not q: print(-1)			
        else: print(q.pop(0))
    elif "size" in cmd:				
        print(len(q))
    elif "empty" in cmd:			
        if not q: print(1)			
        else: print(0)
    elif "front" in cmd:			
        if not q: print(-1)			
        else: print(q[0])
    elif "back" in cmd:				
        if not q: print(-1)			
        else: print(q[-1])

