#given data
customers = [
"Ahmed", "Sara", "Omar", "Mona",
"Ali", "Nour", "Youssef", "Hana",
"Khaled", "Mariam", "Hassan", "Laila"
] 
scores = [
91, 45, 78, 66, 88, 30,
72, 95, 51, 60, 84, 39
]
#Classify Customers
risk_levels = []
for name, score in zip(customers,scores):
    if score >= 85:
        risk = "high"
    elif score >= 60:
        risk = "medium"
    else:
        risk = "low"
    risk_levels.append(risk)
#Calculate Statistics   
high_number = 0
medium_number = 0
low_number = 0
for risk in risk_levels:
    if risk == "high": 
      high_number +=1
    elif risk == "medium":
        medium_number += 1
    else:
        low_number += 1
total = 0
for score in scores:
    total += score
average_risk_score = total / len(scores)
#Find the Best and Worst Customers               
highest_risk =scores[0]
best_name = customers[0]
lowest_risk = scores[0]
worst_name = customers[0]
for name,score in zip(customers,scores):
    if score > highest_risk:
        highest_risk = score
        worst_name = name
    elif score < lowest_risk:
        lowest_risk = score
        best_name = name
#Display a Report
print("CUSTOMER RISK REPORT")
print("NAME  SCORE  RISK")
for name,score,risk in zip(customers,scores,risk_levels):
    print(name, "  " ,score, "  " ,risk)
print("______SUMMARY______")
print(f"high_number : {high_number}")
print(f"medium_number : {medium_number}")
print(f"low_number : {low_number}")
print(f"average_risk_score : {average_risk_score}")
print(f"best_customer : {best_name} ({lowest_risk})")
print(f"worst_customer : {worst_name} ({highest_risk})")
#Create an Interactive Menu
while  True:
    print("____________MENU____________")
    print("1. Show All Customers")
    print("2. Search for a Customer")
    print("0. Exit")
    print("---------------")
    choice = input("Enter your choice :")
    if choice == "1":
        print("CUSTOMER RISK REPORT")
        print("NAME  SCORE  RISK")
        for name,score,risk in zip(customers,scores,risk_levels):
            print(name, "  " ,score, "  " ,risk)
        print("______SUMMARY______")
        print(f"high_number : {high_number}")
        print(f"medium_number : {medium_number}")
        print(f"low_number : {low_number}")
        print(f"average_risk_score : {average_risk_score}")
        print(f"best_customer : {best_name} ({lowest_risk})")
        print(f"worst_customer : {worst_name} ({highest_risk})")    
    elif choice == "2":
        search = input("Enter customer name :")
        for name,score,risk in zip(customers,scores,risk_levels):
            if search == name:
                print(f"name : {name}")
                print(f"score : {score}")
                print(f"risk : {risk}")
    elif choice == "0":
        print("logged out")
        break
    else:
        print("incorrect choise!")




