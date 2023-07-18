# take two integer inputs for chocolates and children
chocolates = int(input())
children = int(input())

# find chocolates each children will get and and print it
number_of_chocolates = chocolates // children
print(number_of_chocolates)

# find remaining chocolates and print it
remaining_chocolates = chocolates % children
print(remaining_chocolates)