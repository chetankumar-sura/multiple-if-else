height = int(input("height is :"))
bill = 0
if height >= 120:
  print("can ride")
  age = int(input("age is :"))
  if age < 12:
    bill = 5
    print("pay 5$")
  elif age <= 18:
    bill = 7
    print("pay $7")
  
  else:
    bill = 12
    print("pay $12")

  want_photos  = input("Do you want photos? y / n")
  if want_photos == "y":
    bill += 3
  print(bill)
else:
  print("Sorry you have to grow little taller")