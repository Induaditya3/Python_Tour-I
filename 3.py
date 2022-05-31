year=int(input("Year="))

days=365
hours=24
min=sec=60
#figure out no. of days
if (year%100!=0 and year%4==0) or year%400:
  days+=1
  
no_of_sec=days*hours*min*sec
print("Number of seconds:",no_of_sec)