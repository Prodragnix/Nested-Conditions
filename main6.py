print('Sellect your ride:\n1.Car\n2.Bike')
choice1=int(input('Please enter your choice  '))
if choice1==1:
    print('What type of car?\n1.Sedan\n2.SUV')
    choice2=int(input('Please enter which type of car  '))
    if choice2==1:
        print('Nice choice. You chose a Sedan.')
    else:
        print('Amazing choice! You chose an SUV!')
elif choice1==2:
    print('What type of bike?\n1.Motorbike\n2.Scooter')
    choice3=int(input('Please enter your choice  '))
    if choice3==1:
        print('Fabulous choice! You chose a Motorbike.')
    else:
        print("Not my favourite, but it's up to you! You chose a Scooter.")
else:
    print('ERROR! Please rerun the program  :(')