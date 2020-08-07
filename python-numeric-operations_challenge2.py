print('Simple calculator!')
First_number = int(input('First number?'))
Operation = input('Operation?')
Second_number = int(input('Second number?'))
if Operation == '+':
    print('sum of', str(First_number), str(Operation), str(Second_number), 'equals', str(First_number+Second_number),sep= ' ')
    exit()
if Operation == '-':
    print('sum of', str(First_number), str(Operation), str(Second_number), 'equals', str(First_number-Second_number),sep= ' ')
    exit()
if Operation == '*':
    print('sum of', str(First_number), str(Operation), str(Second_number), 'equals', str(First_number*Second_number),sep= ' ')
    exit()
if Operation == '/':
    print('sum of', str(First_number), str(Operation), str(Second_number), 'equals', str(First_number/Second_number),sep= ' ')
    exit()
if Operation == '**':
    print('sum of', str(First_number), str(Operation), str(Second_number), 'equals', str(First_number**Second_number),sep= ' ')
    exit()
else:
    print('Operation not recognized.')
    exit()