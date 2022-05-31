def foot_to_inch(feet):
  inches=feet*12
  return f"{inches} inch"
  
def ask_foot():
  return float(input("Number of feet="))

def display(inches):
  print(inches)
  
display(foot_to_inch(ask_foot()))