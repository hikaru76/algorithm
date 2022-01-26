h,w = map(int, input().split())
a = []
for i in range(h):
    a.append(list(map(int,input().split())))

li = [[0] * w] * h
row = [0] * h
col = [0] * w
for i in range(h):
    for j in range(w):
        row[i] += a[i][j]
        col[j] += a[i][j]
for i in range(h):
    for j in range(w):
        print(int(row[i] + col[j] - a[i][j]), end='')
        if j < w - 1:
            print(' ', end='')
    print()