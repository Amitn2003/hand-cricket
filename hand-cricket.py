import random
import time

print("Welcome to hand cricket πβΎββ")
nm = input("Enter your name :")
print(f"Hello {nm.capitalize()}!")

# This list says user won the toss or not

ts_lst = ["head", "tail"]
bt_bl_lst = ["bat", "boll"]
rand_run = [0, 1, 2, 3, 4, 5, 6]

plr_rn = 0
wicket = 0
comp_rn = 0
c_wicket = 0
p_wicket =0

# all functions starts from here


def recent_score():
	logs = open("player.txt")
	print(logs.read())





def match_result():
	# which run is big function
	if comp_rn < plr_rn:
			print(f"\nCongratulations π₯³ {nm.capitalize()}!!! \nYou won the match!! \n\n\n")
	elif comp_rn > plr_rn:
			print(f"\nSorry {nm.capitalize()}. You lost the match π \n \n")
	elif comp_rn == plr_rn:
			print("\nMatch draw ππ \n")
	else:
			print("An error occurred!")
	player = open("player.txt", "a")
	#storing the player name and score after opening this file
	player.write(f"Player name : {nm.capitalize()}. \n Computer score: {comp_rn} & Player runs are {plr_rn} !\n")
	player.close()
	time.sleep(1.1)

def ts():
	a = random.choice(ts_lst)
	return a

#computer choose bat or ball
def rand_bt_bl():
	cmp_bt_bl = random.choice(bt_bl_lst)
	return cmp_bt_bl

# btt is input batting from player

def plr_bat(btt):
	c_choice = random.choice(rand_run)
	global plr_rn
	global wicket
	#rand choice print(c_choice)
	if btt == c_choice:
		print(f"Computer choosen {c_choice} You choose {btt} \nWicketβΌοΈ")
		global wicket
		wicket += 1
		if wicket == 2:
			global plr_rn
			print(f"\nYou gave {plr_rn + 1} run target to the computer.")
			player_target = plr_rn + 1
	elif btt < 7:
		#global plr_rn
		plr_rn += btt 
		print(f"Computer choosen {c_choice} You choose {btt} \nYour run is {plr_rn}.")
	else:
		print(f"Error!! You entered {btt}.")
		
	

# player bolling function
def plr_boll(bll):
	c_choice = random.choice(rand_run)
	#rand choice print(c_choice)
	if bll == c_choice:
		print(f"Computer choosen {c_choice} You choose {bll} \nWicket ββ \nCongratulatin π₯³ you got 1 wicket.")
		global c_wicket
		c_wicket += 1
		
		#global p_wicket
		#p_wicket += 1
	elif bll < 7:
		global comp_rn
		comp_rn += c_choice
		print(f"Computer choosen {c_choice} You choose {bll}. \nComputer's run is {comp_rn}.")
	else:
		print(f"Error!! You entered {bll}.")

# all functions ends here

print("Press 1 for Head,\nPress 2 for Tail. \nPress 3 to see recent scores! ")

ts_inpt = int(input("Enter your choice : "))

if ts_inpt==1:
	print("You choosen Head.")
elif ts_inpt==2:
	print("You choosen Tail.")
elif ts_inpt==3:
	recent_score()
	print("\nBy default it chooses Tail!")
else:
	print("Error! Check your input.")
	time.sleep(1)


ts_usr = int(input("Let's toss: "))

ts_rslt = 1

if ts()=="head" and ts_inpt==1 or ts()=="tail" and ts_inpt==2:
	print(f"Congratulations {nm.capitalize()}!! You won the toss cause you choose {ts()}.")
	ts_rslt = 1 # ts_rslt is Toss Result
elif ts()=="head" and ts_inpt==2 or ts()=="tail" and ts_inpt==1:
	print(f"Sorry {nm.capitalize()}! You lost the toss. ")
	ts_rslt = 0 
	# this is toss result
else:
	print(f"Sorry {nm.capitalize()}! You lost the toss. ")
	ts_rslt = 0 

# if you lost the toss
if ts_rslt == 1:
	# won toss let him/her choose bat/boll
	print(f"Press 1 to choose Bat π \nPress 2 to choose boll")
	bt_bl = int(input("Select your choice: "))
	if bt_bl == 1:
		player_bat = 1
		print("You choosen Bat π")
		#let the player start batting
		while wicket < 2:
			plr_bat(int(input("Enter choice: ")))
			
		print(f"Computer have to reach  {plr_rn + 1} runs to win.")
		
		#computer boll
		while c_wicket < 2 and comp_rn <= plr_rn:
			plr_boll(int(input("Enter choice: ")))
		print(f"Computer run is total {comp_rn}.")
		
		match_result()
		
	elif bt_bl == 2:
		player_bat =0
		print("You choosen Boll βΎ")
		
		# let the player start bolling
		
		while c_wicket < 2:
			plr_boll(int(input("Enter choice: ")))
			
		print(f"Computer runs are total {comp_rn} !!")
		print(f"Computer gave you {comp_rn +1} runs target. π―")
		
		print("Let's start batting πποΈββοΈ")
		
		# start batting ποΈββοΈπ
		while plr_rn < comp_rn and wicket < 2:
			plr_bat(int(input("Let's hit the boll βΎ: ")))
			
			
		print(f"Your total runs are {plr_rn}	")	
		match_result()
		
		
elif ts_rslt == 0:
	print("You lost the toss...")
	print(f"Let the computer choose bat or bollβ¦")
	#programe will choose bat of boll
	rand_bt_bl = rand_bt_bl()
	print(f"Computer choosed {rand_bt_bl}. ")
	#print(rand_bt_bl)
	# if player lose the toss
	if rand_bt_bl == "bat":
		while c_wicket <2:
			plr_boll(int(input("Enter choice: ")))
		print(f"\nComputer''s total run is {comp_rn}!!")
		print(f"\nComputer gave you {comp_rn + 1} runs target.")
		time.sleep(0.4)
		# let the player batting
		while plr_rn < comp_rn and wicket < 2:
			plr_bat(int(input("Let's hit the boll βΎ: ")))
		
		print(f"Your total runs are {plr_rn}.")
		match_result()
		# match end
	elif rand_bt_bl == "boll":
		
		while wicket < 2:
			plr_bat(int(input("Enter choice: ")))
			
		print(f"Computer have to reach  {plr_rn + 1} runs to win.")
		time.sleep(0.4)
		
		#computer boll
		while c_wicket < 2 and comp_rn <= plr_rn:
			plr_boll(int(input("Enter choice: ")))
		print(f"Computer run is total {comp_rn}.")
		match_result()
		
		

print("Thanks for playing this game\nHope you enjoyed this game!!\n\n")


time.sleep(1)
print("Good byeβ¦")
time.sleep(0.8)
print("Exitingβ¦")
time.sleep(0.9)
