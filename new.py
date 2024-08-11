import random
user_score = 0
computer_score = 0
a = 0
while a == 0:
    move = int(input("What do you choose 0 for Rock , 1 for Paper and 2 for Scissors?  "))

    x = random.randint(0, 2)
    if move == 0:
        print("Rock by user")
        print("""
              _______
          ---'   ____)
                (_____)
                (_____)
                (____)
          ---.__(___)
          """)
        if x == 0:
            print("Rock by computer")
            print("""
                  _______
              ---'   ____)
                    (_____)
                    (_____)
                    (____)
              ---.__(___)
              """)
            print("Draw")
            user_score = user_score + 0
            computer_score = computer_score + 0
        elif x == 1:
            print("Paper by computer")
            print("""
                   _______
              ---'    ____)____
                         ______)
                        _______)
                       _______)
              ---.__________)
              """)
            print("Computer wins")
            user_score = user_score + 0
            computer_score = computer_score + 1
        else:
            print("Scissor by computer")
            print("""
                  _______
              ---'   ____)____
                        ______)
                     __________)
                    (____)
              ---.__(___)
              """)
            print("User Wins")
            user_score = user_score + 1
            computer_score = computer_score + 0
    elif move == 1:
        print("Paper")
        print("""
               _______
          ---'    ____)____
                     ______)
                    _______)
                   _______)
          ---.__________)
          """)
        if x == 1:
            print("Paper by computer")
            print("""
                   _______
              ---'    ____)____
                         ______)
                        _______)
                       _______)
              ---.__________)
              """)
            print("Draw")
            user_score = user_score + 0
            computer_score = computer_score + 0
        elif x == 2:
            print("Scissor by computer")
            print("""
                  _______
              ---'   ____)____
                        ______)
                     __________)
                    (____)
              ---.__(___)
              """)
            print("Computer wins")
            user_score = user_score + 0
            computer_score = computer_score + 1
        else:
            print("Rock by computer")
            print("""
                  _______
              ---'   ____)
                    (_____)
                    (_____)
                    (____)
              ---.__(___)
              """)
            print("User Wins")
            user_score = user_score + 1
            computer_score = computer_score + 0
    elif move == 2:
        print("Scissors")
        print("""
              _______
          ---'   ____)____
                    ______)
                 __________)
                (____)
          ---.__(___)
          """)
        if x == 2:
            print("Scissors by computer")
            print("""
                  _______
              ---'   ____)____
                        ______)
                     __________)
                    (____)
              ---.__(___)
              """)
            print("Draw")
            user_score = user_score + 0
            computer_score = computer_score + 0
        elif x == 0:
            print("Rock by computer")
            print("""
                  _______
              ---'   ____)
                    (_____)
                    (_____)
                    (____)
              ---.__(___)
              """)
            print("Computer wins")
            user_score = user_score + 0
            computer_score = computer_score + 1
        else:
            print("Paper by computer")
            print("""
                   _______
              ---'    ____)____
                         ______)
                        _______)
                       _______)
              ---.__________)
              """)
            print("User Wins")
            user_score = user_score + 1
            computer_score = computer_score + 0

    else:
        print("Invalid input")
    print("~~~~~~~~~~~~~~Your current score is",user_score ,"~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~Computer current score is", computer_score, "~~~~~~~~~~~~~~~~~~~")



