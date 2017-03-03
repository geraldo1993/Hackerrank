# Enter your code here. Read input from STDIN. Print output to STDOUT
n, k = map(int, raw_input().split(' '))
order = map(int, raw_input().split(' '))
amount_charged = int(raw_input())
order.pop(k)
annas_share = sum(order) / 2

if annas_share == amount_charged:
    print "Bon Appetit"
else:
    print amount_charged - annas_share
