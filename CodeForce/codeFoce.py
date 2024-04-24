def find_number(n,k):
    num_odds = (n+1)//2
    
    if k <= num_odds:
        return 2*k-1
    
    else:
        return (k-num_odds) * 2
    
n, k = map(int, input().split())

    
print(find_number(n,k))


