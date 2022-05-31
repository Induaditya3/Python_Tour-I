x=input("Please enter the first time: ")
y=input("Please enter the second time: ")

minute=int(y[2:4])-int(x[2:4])
hour=int(y[:2])-int(x[:2])
if minute<0:
  hour-=1
  minute=-minute

print(f"{hour} hours {minute} minutes")