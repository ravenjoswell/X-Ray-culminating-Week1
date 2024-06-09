def exact_change(item_cost, money_paid):
    change_list = []
    change_string = ""
    change_total = money_paid - item_cost
   
    if money_paid < item_cost:
        print("You can't afford this item.")

    if change_total == 0:
        return "Your total is 0.00."
    
    
    


    money_denom = {
        "One Hundred Dollar Bill": 100,
        "Fifty Dollar Bill": 50,
        "Twenty Dollar Bill": 20,
        "Ten Dollar Bill": 10,
        "Five Dollar Bill": 5,
        "Two Dollar Bill": 2,
        "One Dollar Bill": 1,
        "Quarter": 0.25,
        "Dime": 0.10,
        "Nickel": 0.05,
        "Penny": 0.01,
    }
    total_change = money_paid - item_cost

    for bill_cents, amount in money_denom.items():
        
        temp = int(total_change // amount)
        # print(f"temp = {total_change} // {amount}")
        if temp == 0:
            continue
        
        total_change -= amount * temp
        # print(temp, bill_cents)
        change_list.append([temp, bill_cents])
        
        # print(change_list)
    for change in change_list:
        # print(change[0], change[1])
        x = "s"
        if change[0] > 1: 
        # print(change[1])
            if(change[1] == "Penny"):
                change[1] = "Pennies"
                # print(change[1])
            else:
                change[1] = f"{change[1]}{x}"
                # print(change[1])
      
            

    str_change = f"Your total is {format(change_total,".2f")}: "

    for index, value in enumerate(change_list):
        if len(change_list) == 1:
            str_change += f"{value[0]} {value[1]}."
        elif index == len(change_list) -1:
            str_change += f"and {value[0]} {value[1]}."
        else:
            str_change += f"{value[0]} {value[1]}, "

    return str_change     

      
    
# print(exact_change(1.34, 5))
# print(exact_change(0, 0.01))
# print(exact_change(53.73, 100))
# print(exact_change(10, 20))
# print(exact_change(20, 10))
# print(exact_change(0.75, 2))
# print(exact_change(10, 10))
# print(exact_change(10.75, 20))
# print(exact_change(5.0, 10))
print(exact_change(17.53, 30))
# print(exact_change(0, 999.99))
# print(exact_change(5.0, 10.0))
# print(exact_change(9.99, 20))
# print(exact_change(1000, 1200))
# print(exact_change(10.0, 20))



