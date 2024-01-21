# # create a program capabale of displaying questions like KBC.
# # use list data type to store the questions and their correct answers.
# # display the final amount the person taking the home after playing the game.
# print("Welcome to Kaun Banega Crorepati ")
# one = int(input("Enter press one (1) is keyboard and play the game"))
# match one:
#      case 1:
#
#
#        print("What is the capital of India")
#        print("Your option is (Delhi),(Lucknow),(Mumbai),(Kolkata)")
#        option = 1
#        print("(press 1 for Delhi),(press 2 for Lucknow) ,(press 3 for Mumbai), (press 4 for Kolkata)")
#        answer = int(input("Enter your Answer"))
#        if (option==answer):
#            print("Congratulation your Answer is correct")
#            second = int(input("press Two (2) and you enter in Second Round"))
#            match second:
#                 case 2:
#                     print("who is prime minister of india ")
#                     print("Your option is (Indira Gandhi),(Gulzarilal Nanda),(Lal Bahadur Shastri),(Narendra Modi)")
#                     print("(press 1 for Indira Gandhi ), (press 2 for Gulzarilal Nanda), (press 3 for Lal Bahadur Shastri), ( press 4 for Narendra Modi )")
#            answer = int(input("Enter your Answer"))
#            option = 4
#            if(option==answer):
#                print("Congratulation your Answer is correct")
#            else:
#                print("Wrong Answer")
questions=[["whixh language was used to create fb?","python","french","java","php","none",4],
["whixh language was used to create fb?","python","french","java","php","none",4],
["whixh language was used to create fb?","python","french","java","php","none",4],
["whixh language was used to create fb?","python","french","java","php","none",4],
["whixh language was used to create fb?","python","french","java","php","none",4]]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"\n\nquestions for rs {levels[i]}")
    print(f"a.{question[1]}          b.{question[2]}")
    print(f"c.{question[3]}          d.{question[4]}")
    reply=int(input("enter your answer(1-4)"))
    if (reply== question[-1]):
        print(f"correct answer, you won rupees \n{levels[i]}")
        if (i==4):
            money=10000
        elif (i==9):
            money=320000


    else:
        print("wrong answer")
        money=0
print(f"your takehome money is {money}")

