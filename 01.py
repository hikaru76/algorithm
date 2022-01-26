n, l = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))
a.append(l)

def devide(center):
    total_devide = 0
    length_memo = 0
    memo = l
    for i in a:
        # print("i="+str(i))
        # print("length="+str(length_memo))
        # print("center="+str(center))
        # print("total_devide=" + str(total_devide))
        # print()
        if i - length_memo >= center:
            length_memo = i
            total_devide += 1
        if total_devide >= k:
            memo = i
            break
    if total_devide >= k:
        if l - memo >= center:
            return 1
    else:
        return 0

left = 1
right = l
center = int((right + left) / 2)
while(1):
    if devide(center):
        left = center
        center = int((right + left) / 2)
    else:
        right = center
        center = int((right + left) / 2)
    if center == right or center == left:
        break

print(center)
