import random
print('this is a number guessing game!')
print('you can enter stop whenever to stop the game')
num = random.randint(0,100)
print(num)
guess = input('guess a number between 0 and 100:')
count = 0
while guess != 'stop':
    count += 1
    if int(guess) > num:
        guess = input('Try smaller number:')
    elif int(guess) < num:
        guess = input('Try larger number:')
    elif int(guess) == num:
        print('you got it! congrtulations!')
        guess = 'stop'
print('You tried %d times' % (count))
print('end of the game')
    
