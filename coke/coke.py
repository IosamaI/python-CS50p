
AmountDue = 50
while AmountDue > int(0) :
 
    print("Amount Due:", AmountDue )

    insertCoin = int(input("insert coin: "))

    if insertCoin == 25 or insertCoin == 10 or insertCoin == 5 :
     AmountDue -= insertCoin

       
    else:
        print("Amount Due:", AmountDue ) 


print("Change Owed:", abs(AmountDue) )
    