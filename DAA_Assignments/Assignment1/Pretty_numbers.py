# cook your dish here
for i in range(int(input())):
    sum = 0
    l,r = map(int, input().split())
    for j in range(l, r+1):
        num = j%10
        if num == 2 or num == 3 or num == 9:
            sum = sum+1
            
    print(sum)
        