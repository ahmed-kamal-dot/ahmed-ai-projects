#python program that calculates how much a project will cost
#ask the user enter:
team_members = input("enter number of team members : ")
team_members = int(team_members)
print(f"team_members{team_members}")
months = input("enter number of months the project will take : ")
months = int(months)
print(f"months{months}")
monthiy_salary = input("enter monthly salary : ")
monthiy_salary = float(monthiy_salary)
print(f"monthiy_salary{monthiy_salary}")
cloud_cost = input("enter total cloud cost for the whole project : ")
cloud_cost = float(cloud_cost)
print(f"cloud_cost{cloud_cost}")
#then calculate
salary_cost = team_members * months * monthiy_salary
subtotal = salary_cost + cloud_cost
VAT = subtotal * 0.14
Total = subtotal + VAT
print(f"salary_cost : {salary_cost:,.2f}")
print(f"subtotal : {subtotal:,.2f}")
print(f"VAT : {VAT:,.2f}")
print(f"Total : {Total:,.2f}")

