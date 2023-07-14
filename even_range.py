def count_even_numbers(A,queries):
    result=[]
    for query in queries:
        start=query[0]
        end=query[1]
        count=0
        for i in range(start,end,+1):
            if A[i]%2== 0:
                count+=1
        result.append(count)
    return result
A = list(map(int,input().split()))
Q = int(input("enter the number of queries:")) 
B = [] 
for i in range(Q):
    query=list(map(int, input("enter the start and end indices:".format(i + 1)).split()))
    B.append(query)
print(count_even_numbers(A,B))
