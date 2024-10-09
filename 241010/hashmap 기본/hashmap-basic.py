n = int(input())
d = dict()
for _ in range(n):
    cmd, *num = input().split()
    k = num[0]
    if cmd == 'add':
        v = num[1]
        d[k] = v
    elif cmd == 'remove':
        del d[k]
    else:
        if k in d.keys():
            print(d[k])
        else: print(None)