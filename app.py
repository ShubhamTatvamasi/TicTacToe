#!/usr/bin/python3

print('Welcome to Tick Tack Toe\n')

player1 = input('Enter the name of player 1: ')
print('Welcome ' + player1 + ' you have to enter (x)\n')
player2 = input('Enter the name of player 2: ')
print('Welcome ' + player2 + ' you have to enter (o)\n')
print('Lets Play!\n')
winner = player1
A1,A2,A3,B1,B2,B3,C1,C2,C3 = '1','2','3','4','5','6','7','8','9'
playerwon = False

def table():
	print(A1+' | '+A2+' | '+A3)
	print('----------')
	print(B1+' | '+B2+' | '+B3)
	print('----------')
	print(C1+' | '+C2+' | '+C3)

table()

print("Please enter the number in which you want to enter the your input")
while playerwon == False:
	if (A1==A2==A3 or B1==B2==B3 or C1==C2==C3 or A1==B1==C1 or A2==B2==C2 or A3==B3==C3 or A1==B2==C3 or C1==B2==A3):
		playerwon = True
		break
	winner = player1
	answer1 = input(player1 + ' enter the number: ')
	if answer1 == '1':
		A1 = 'x'
	if answer1 == '2':
		A2 = 'x'
	if answer1 == '3':
		A3 = 'x'
	if answer1 == '4':
		B1 = 'x'
	if answer1 == '5':
		B2 = 'x'
	if answer1 == '6':
		B3 = 'x'
	if answer1 == '7':
		C1 = 'x'
	if answer1 == '8':
		C2 = 'x'
	if answer1 == '9':
		C3 = 'x'
	table()
	
	if (A1==A2==A3 or B1==B2==B3 or C1==C2==C3 or A1==B1==C1 or A2==B2==C2 or A3==B3==C3 or A1==B2==C3 or C1==B2==A3):
		playerwon = True
		break
	winner = player2
	answer2 = input(player2 + ' enter the number: ')
	if answer2 == '1':
		A1 = 'o'
	if answer2 == '2':
		A2 = 'o'
	if answer2 == '3':
		A3 = 'o'
	if answer2 == '4':
		B1 = 'o'
	if answer2 == '5':
		B2 = 'o'
	if answer2 == '6':
		B3 = 'o'
	if answer2 == '7':
		C1 = 'o'
	if answer2 == '8':
		C2 = 'o'
	if answer2 == '9':
		C3 = 'o'
	table()



print('Congratulation ' + winner + ' you have won the game!')