import datetime as time
now = time.datetime.now()
hour = now.hour

if hour < 12:
    print("Good morning")
elif hour > 11 and hour < 18:
    print("Good afternoon")
elif hour > 18 and hour < 19:
    print("Good evening")
else:
    print('Good night.')
def options():
    
    option = input("""
    Do you want to 
    a Play the game
    b See the rules
    : 
    """)
    if option == "a" or option == "A" or option == "Play the game" or option == "play the game":
        def reverse_func(s):
            return s == s[::-1]
        s = input("Enter a the word to check its reverse:  ")

        answer = reverse_func(s)

        if answer:
            print("You scored a point")
            c.execute('INSERT INTO points VALUES(1)')
            conn.commit()
        else:
            print("You did not get a point.")
            
            def try_again_func():
                try_again = input("""
                Do you want to 
                a Exit the game
                B Play again
                : 
                """)
                if try_again == "a" or try_again == "Exit" or try_again == "A" or try_again == "exit":
                    sum1 = 0
                    for num in sum1:
                        sum1 += int(num)
                    nal = [item for a in sum1 for item in a]
                    print(sum1)


            try_again_func()
        else:
            print("You don't get a point")
    elif option == "b" or option == "B" or option == "See the rules" or option == "see the rules":  
        print("These are the rules.")
        print("""
        1. Enter word that you think can be read forwards and backwards
        2. if it is correct you will score 1 point.
        3. If it is wrong you get 0 points.
        """)
        options()
    else:
        print("I did not understand you. Please try again.")
        options()
options()
def team_func():
    global team
    team = input("""Which team do you want to join:
    a Team Nesh.Motto(We will never give up).
    b Team Malli.Motto(Team work makes the dream work).
    : 
    """)
    if team == "a" or team == "A" or team == "Team Nesh" or team == "team Nesh":
        print("Welcome to Team Nesh! Our Motto is we will never give up.")
        options()
    elif team == "b" or team == "B" or team == "Team Malli" or team == "team Malli":
        print("Welcome to Team Malli! Our Motto is team work makes the dream work")
    
def username_func():
    global username
    username = input("Enter your name: ")
username_func()
if len(username) >= 3:
    def gender_func():
        global gender
        gender = input("""
        Are you:
        Male(m)/
        Female(F)/
        Dont wish to say(d)
        : 
        """)
    gender_func()
    if gender == "m" or gender == "M" or gender == "male" or gender == "Male":
        team_func()
    elif gender == "f" or gender == "F" or gender == "female" or gender == "Female":
        pass
    elif gender == "d" or gender == "D":
        pass
    else:
        print("I did not understand you")
        gender_func()
        
    
else:
    print("I did not understand you")
