# rock paper scissor
import random
option = ("rock" , "paper" , "scissor")
computer = random.choice(option)
player = input("Enter \"rock paper scissor\" : ")
while(player not in option):
    print("Invalid option")
    player = input("Enter \"rock paper scissor\" : ")
if player == computer :
    print("match is tie!!!!")
elif(player == 'rock' and computer == 'scissor'):
    print("you win!!!")
elif(player == 'paper'  and computer == 'rock'):
    print("you win!!!")
elif(player == 'scissor' and computer == 'paper'):
    print('you win!!!')
else:
    print("you lose!!!")

print(player)
print(computer)