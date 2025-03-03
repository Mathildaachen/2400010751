import sys
from collections import deque
data = sys.stdin.read().split()
if not data:
    exit()
t = int(data[0])
idx = 1
res = []
for _ in range(t):
    n = int(data[idx])
    idx += 1
    stack = []
    queue = deque()
    valid_stack = True
    valid_queue = True
    for _ in range(n):
        op = int(data[idx])
        val = int(data[idx + 1])
        idx += 2
        if op == 1:
            stack.append(val)
            queue.append(val)
        else:
            if valid_stack:
                if not stack or stack[-1] != val:
                    valid_stack = False
                else:
                    stack.pop()
            if valid_queue:
                if not queue or queue[0] != val:
                    valid_queue = False
                else:
                    queue.popleft()
    res.append("Stack" if valid_stack else "Queue")
sys.stdout.write("\n".join(res))
