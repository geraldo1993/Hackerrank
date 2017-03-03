

tTrips=input()
tTrips=int(tTrips)
for i in range(0,tTrips):
        
    mn=int(input()),int(input())
    prices=input()
    prices = [int(i) for i in prices.split(' ')]
    for k in range(len(prices)-1):
        
        if mn[0]-prices[k] in prices[k+1:]:
             print(k+1,prices[k+1:].index(mn[0]-prices[k])+k+2)
    
    
    
