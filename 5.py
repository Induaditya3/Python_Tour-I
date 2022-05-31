n=float(input("n="))
day=input("First day of the year was ").capitalize()

days={"Monday":0,"Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4,"Saturday":5, "Sunday":6}

reverse_dic={value:key for key,value in days.items()}

print(reverse_dic[((days[day]+n-1)/7)])