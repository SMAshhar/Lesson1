donuts = ["Chocolate", "banana", "strawberry", "pinapple"]      # making a list of availble items in store
donuts.append("classic")
print(donuts)
donuts += ["Wheel"]
print(donuts)
donuts = donuts + ["Cheese Cake"]
print(donuts)
donuts.remove("classic")
donuts.insert(0, "classic")
print(donuts)
donuts += ["Limited edition special"]                           # some limited edition will be availale 
print(donuts)
del donuts[7]
print(donuts)
donuts[5] = "candy"
print(donuts)
print("\n\n")
print("Please select from the following")                       # adding things in your cart
print(f"1. {donuts[0]}  Rs. 10" + "\n" + f"2. {donuts[1]} Rs. 20" + "\n" + f"3. {donuts[2]}  Rs. 15" + "\n" + f"4. {donuts[3]} Rs. 10" + "\n" + f"5. Finish purchase")
def purchasing():
  b = 0
  c = 0
  d = 0
  e = 0 
  for x in range(20):
    a = int(input("\t\t"))
    if a == 1:
      print(f"One {donuts[0]} has been added to your cart")
      b += 1
    elif a == 2:
      print(f"One {donuts[1]} has been added to your cart")
      c += 1
    elif a == 3:
      print(f"One {donuts[2]} has been added to your cart")
      d += 1
    elif a == 4:
      print(f"One {donuts[3]} has been added to your cart")
      e += 1
    elif a == 5:
      print("Your cart has ", b, f"{donuts[0]} ", c, f"{donuts[1]} ", d, f"{donuts[2]} ", e, f"{donuts[3]}" )
      g = b * 10
      h = c * 20
      i = d * 15
      j = e * 10
      h = g + h + i + j
      break
  x = input(print("Proceed to check out? Press Y/N"))
  if x == "Y"or x == "y":
    print("Your bill is Rs.", h)
purchasing()
z = input(print("Do you want to continue shopping? Press Y/N"))
if z == "Y" or z == "y":
  purchasing()
else:
  print("End of purchasing")