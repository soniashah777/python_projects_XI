# complete the following code module for a quiz.
def add_questions():
    enter="y"
    while enter=="y":
        que_list.append(input ("Enter question"))
        option1.append(input ("Enter option 1"))
        option2.append(input ("Enter option 2"))
        option3.append(input ("Enter option 3"))
        option4.append(input ("Enter option 4"))
        answer.append(input ("Enter answer"))
        enter=input ("Do you want to enter more question, enter y for yes")
    # add code to add questions here
def list_questions():
    for i in range (0,len(que_list)):
        print (que_list[i])
        print (option1[i])
        print (option2[i])
        print (option3[i])
        print (option4[i])
        print (answer[i])
que_list=[]
option1 =[]
option2=[]
option3=[]
option4=[]
answer =[]
uname="developer"
password="code"
print ("enter d for developer")
print ("enter u for user")

choice = input ("Enter your choice")
if (choice=="d"):
    if (input ("Enter username") == uname and input ("enter password")==password):
        while True:
            print ("Enter a for adding questions")
            print ("Enter l for listing questions")
            d_choice=input("Enter your choice here")
            if (d_choice=="a"):
                add_questions()
            elif (d_choice=="l"):
                list_questions()
            else:
                print ("invalid input")
            
    else:
        print ("Invalid username or password")
elif (choice=="u"):
    #Enter code to show quiz here
    print ("user code")
else:
    print ("invalid input")








    
