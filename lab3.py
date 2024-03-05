#The code for this project represents my own, independent work. I
#have neither given nor received help on this assignment from other
#students.

#James Moore

true_price = int(input("What is the true price of the prize? "))
num_con = int(input("How many contestants are playing today? "))

win_con = 0
everyone_overbid = True
high_bid = 0
for i in range(num_con):
    con = i + 1
    bid = int(input(f'What is the bid for Contestant {i+1}? '))
    if i == 0 and bid <= true_price:
        high_bid = bid
        everyone_overbid = False
        win_con = con
    elif high_bid < bid and bid <= true_price:
        high_bid = bid
        win_con = con
        everyone_overbid = False


if everyone_overbid == True:
    print("All contestants have overbid!")
else:
    print(f'Contestant {win_con} wins')
    

    


