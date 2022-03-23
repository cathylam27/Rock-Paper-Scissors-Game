from gameComponents import gameVars

def winorlose(status):
	#version 1 of function
	# print("Inside winorlose function; status is: ", status)
	print("You", status, "! Would you like to play again?")
	choice = input("Y / N? ")

	if choice == "N" or choice =="n":
		print("You chose to quit! Better luck next time!")
		exit()
	elif choice == "Y" or choice == "y":
		#reset the player lives and computer lives
		# and reset player choice to False, so our loop restar
		gameVars.player_lives = gameVars.total_lives
		gameVars.computer_lives = gameVars.total_lives
		gameVars.player_choice = False
		
	else:
		print("Make a valid choice - Y or N")
		#this might generate a bug that we need to fix later
		choice = input("Y / N? ")