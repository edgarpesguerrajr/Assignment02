money_str = input('Enter the amount of your money: ')
apples_str = input('Enter the price of the apple: ')
money = int(money_str)
apple = int(apples_str)
totalapple = money//apple
totalamount = totalapple*apple
print(f'You can buy {totalapple} apples and your change is {money-totalamount} pesos.')