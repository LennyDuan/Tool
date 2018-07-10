def selectOption():
    print('-----------------------')
    print('Please choose your next steps:')
    print('1: List all accounts')
    print('2: Get exist account(s)')
    print('3: Creat/Save a new account')
    print('0: Exit')
    print('-----------------------')
    try:
        return int(input('Select option:'))
    except:
        print('[Error]: Invalid Input')
        return selectOption()
