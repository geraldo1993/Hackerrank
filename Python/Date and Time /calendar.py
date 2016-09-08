import datetime

n=raw_input()

p= datetime.datetime.strptime(n, '%m %d %Y').strftime('%A')

print p.upper()
