###Cell Phone Bill Calculator###


print ("")###Just to add more space###
print ("")###Just to add more space###
print ("The Economy plan includes $30 unlimited voice and text, 1 GB data for $10, and $6 for every GB over.")
print ("The Normal plan includes $30 unlimited voice and text, 5 GB data for $30, and $4 for every GB over.")
print ("")###Just to add more space###
plan = input ("What plan would you like? Type 'a' for Economy plan, or 'b' for Normal plan. > ")
d = int (float ("How many gigabytes of data do you use? > "))

if (plan == a):
    and (d <= 1):
         bill = (30+10)
    and (d > 1):
         bill = (30+10+(6*d))

if (plan==b):
    and (d <= 5):
         bill = (30+30)
    and (d > 5):
         bill = (30+5+(4*d))






print ("Your bill totals out to be," bill "dollars")
