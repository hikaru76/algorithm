import itertools

n = int(input())

def check(a):
    left = 0
    for i in a:
        if i == '1':
            left += 1
        else:
            left -= 1
        if left < 0:
            return 0
    return 1

def printstr(a):
    for i in a:
        if i == 0:
            print(')', end='')
        else:
            print('(', end='')
    print()

if n % 2 == 0:
    all = []
    for i in range(2 ** n):
        li = []
        cnt_left = 0
        cnt_right = 0
        for j in range(n):
            if i >> j & 1:
                cnt_left += 1
                li.append(1)
            else:
                cnt_right += 1
                li.append(0)
            if cnt_right > cnt_left or cnt_left > n // 2:
                break
        if cnt_left == cnt_right:
            all.append(li)
    all.sort(reverse=True)
    for a in all:
        printstr(a)