from time import sleep
from os import system
from random import randint

def check_coords(slist):
    if len(slist)!=2 or len(slist[0])!=2 or len(slist[1])!=2:
        return False
    if slist[0][0]==slist[1][0] and slist[0][1]==slist[1][1]:
        return False
    strq ='ABCD'
    num = '1234'
    if not (slist[0][0] in strq) or (not slist[1][0] in strq) or (not str(slist[1][1]) in num) or (not str(slist[0][1]) in num):
        return False
    return True
n=4
print('Hello! This is a game for training your memory.\nFind all pairs of matching cards on 4*4 field.\n'
      'Max tries is 30.')
a = [['X']*n for i in range(n)]
print('  A B C D')
for i in range(n):
    print(i+1, end=' ')
    for j in range(n):
        print(a[i][j], end=' ')
    print()

symb=['@','#','$','%','&','*','?','+']
x1,x2,y1,y2=[1]*4
count_changes=0
b=0
a1=[['X']*n for i in range(n)]
while count_changes<n*n//2:
    while (x1==x2 and y1==y2) or a1[x1][y1]!='X' or a1[x2][y2]!='X':
        x1 = randint(0, 3)
        y1 = randint(0, 3)
        x2 = randint(0, 3)
        y2 = randint(0, 3)
    b = symb[count_changes]
    a1[x1][y1] = b
    a1[x2][y2] = b
    count_changes+=1
print()
guesses=0
good_guesses=0

while True:
    for i in a1:
        print(*i)
    if guesses==30:
        print('Sorry, you lost... try again.')
        exit()
    coords=[]
    while check_coords(coords)!=True:
        coords=[]
        coords.append(list(input('Enter coordinates of the first card please (in format A2): ')))
        coords.append(list(input('Enter coordinates of the second card please: ')))
    guesses+=1
    coords[0][0]=ord(coords[0][0])-64-1 # A is 1, B is 2
    coords[1][0]=ord(coords[1][0])-64-1
    coords[1][1]=int(coords[1][1])-1
    coords[0][1]=int(coords[0][1])-1
    #switch indexes
    if a1[coords[0][1]][coords[0][0]]==a1[coords[1][1]][coords[1][0]] and a[coords[1][1]][coords[1][0]]=='X':
        a[coords[0][1]][coords[0][0]]=a1[coords[0][1]][coords[0][0]]
        a[coords[1][1]][coords[1][0]]=a1[coords[1][1]][coords[1][0]]
        good_guesses+=1
        print('  A B C D')
        for i in range(n):
            print(i + 1, end=' ')
            for j in range(n):
                print(a[i][j], end=' ')
            print()
        sleep(3)
        system("cls")
    else:
        print('  A B C D')
        for i in range(n):
            print(i + 1, end=' ')
            for j in range(n):
                if i==coords[0][1] and j==coords[0][0]:
                    print(a1[coords[0][1]][coords[0][0]], end=' ')
                elif i==coords[1][1] and j==coords[1][0]:
                    print(a1[coords[1][1]][coords[1][0]], end=' ')
                else:
                    print(a[i][j], end=' ')
            print()
        sleep(3)
        system("cls")
    if good_guesses==8:
        m=round(good_guesses/guesses, 2)*100
        print(f'You guessed everything with {guesses} guesses and accuracy of {m} %.'
              f' Congratulations! \U0001F642 \U0001F947')
        sleep(5)
        exit()