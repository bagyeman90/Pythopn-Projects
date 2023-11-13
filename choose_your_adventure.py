name = input("Please enter your name: ").capitalize()
print("Hello Welcome to the adventure",  name)

# You are required to choose if you want to play the game
choice = input("Do you want to play the game? (yes/no) ").lower()

# If the user wants to play & Which avatar does the user want to use
if choice == "yes":
    print("Which avatar do you want? ")  
    avatar1 = input("(Spider Man, Batman, Iron Man)")  

    # When you choose Spider Man
    if avatar1 == "Spider Man".lower():
        print("You have 2 charaters to handle.")
        avatar2 = input("Which character do you want (Peter/Miles)?")

        # Which Spider man character do you want to play
        if avatar2 == "Peter".lower():
            print("This is a new charater and you can go ahead and play ")
            print("Do you want the first game or the seond? (firsft/second) ")

        elif avatar2 == "Miles".lower():
            print("You have a bunch of options to chose from ")
            suit = input("Which suit do you want? (Custom/Original?) ")
           
            # Which miles suit would you like to choose
            if suit == "Custom".lower():
                print("That is a new edition suit")
            elif suit == "Original".lower():
                print("This is the older version of suit")   
            else:
                print("Invalid choice made")    

        else:
            print("Invalid Option ")
    
    # When you choose Batman
    elif avatar1 == ("Batman".lower()):
        print("Which crime do you want to solve first?")
        avatar3 = input(" (Gotham, Prison, Corporate) ")
    
        # There are various issues to solve so which would you want to solve first?
        # (Gotham, Prison, Corporate)
        if avatar3 == "Gotham".lower():
            print("You will need to go after 2 criminals. " )
            avatar4 = input("(Penguin/Joker)")

            # Going after Penguin
            if avatar4 == "Penguin".lower():
                print("You have been able to defeat the vilian ")
                print("Congratulations")
            
            # Going after Joker
            elif avatar4 == "Joker".lower():
                print("You couldn't defeat him in 1 try")
                
                choice = input("Do you wanna try again? ")
            
                if choice == 'yes'.lower():
                    print("You were able to defeat him ")
                elif choice == "no".lower():
                    print("Bye")
                else:
                    print("Invlaid Option")
            
            # Choosing the wrong option
            else:
                print("Invalid choice")

        # This is when you choose Prison
        elif avatar3 == "Prison".lower():
            print("There was too much going on and you couldn't handle")
            print("You lost the battle")
            print("Try again next time")

        # This is the Corporate option for the Batman and solve the Corporate problem.        
        elif avatar3 == "Corporate".lower():
            print("There was nothing going on there")
            print("Try next time")                 
        else:    
            print("Invalid Avatar")      

    # This is the avatar option for Iron Man
    elif avatar1 == "Iron Man".lower():
        print("Do you want the bodysuit? (Tech-enhanced/Normal)")

        # What body suit will you want to choose?
        if "Tech-enhanced".lower():
            print("You have the maximum technology available to play")
        elif "Normal".lower():
            print("This doesn't have nuch protection and can die early.")
        else:
            print("Invalid option")

    else:
        print("Invalid Avatar")

# This option is when you don't want to play
elif "no":
    print("You can come again when you are ready to play.")

else:
    print("Thank you")