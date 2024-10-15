med=input('Do you have any medical cause? Write y for yes or n for no.  ')
attend=int(input('What is the attendance percentage of your child?  '))
if med=='y':
    print('You are allowed.')
else:
    if attend>=75:
        print('You are allowed')
    else:
        print("You aren't allowed")
           