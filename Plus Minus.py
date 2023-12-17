def plusMinus():
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    positive_values = 0
    negative_values = 0
    zeros = 0
      
    for i in arr:
        if int(i)>0:
            positive_values+=1
        
        if int(i)<0:
            negative_values+=1
        
        if int(i)==0:
            zeros+=1
    print(positive_values/n)
    print(negative_values/n)
    print(zeros/n)

plusMinus()
