print("hello, how can I help you?")
while (True): 
  print("for menu- select 1, to order- press 2, to leave- type quit")
  user_input= input().lower()
  if user_input=='quit':
    print("thank you for eating with us!")
    break
  if user_input=='1': 
    print("burgers-$6, hotdogs-$5, fries-$3")
  if user_input=='2': 
    print("what would you like to order?")
    user_input2= input().lower()
    print( "thank you, your order will be ready shortly")
    print("would you like something else?")
  