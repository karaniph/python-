
# get input value for total number of friends 
total_friends=int(input())

# get input value for total bill 
total_bill=float(input())

# calculate the tax amount
tax = 20 /100 * total_bill / total_friends

# divide bill among friends
split_amount = tax + total_bill /total_friends

# print the split amount
print(split_amount)