# cook your dish here
for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    fr = {}
    
    for num in arr:
        if num in fr:
            fr[num] += 1
        else:
            fr[num] = 1
            
    max_fr = max(fr.values())
    print(len(arr)-max_fr)
    
    