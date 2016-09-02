def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4==0 and year%400==0:
        return  True
    else:
          return False

    
    return leap
    
    
year = int(raw_input())
print is_leap(year)
