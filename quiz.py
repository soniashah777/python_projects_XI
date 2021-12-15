# complete the following code module for a quiz.

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
        print ("Enter a for adding questions")
        print ("Enter l for listing questions")
        d_choice=input("Enter your choice here")
        if (d_choice=="a"):
            add_questions()
        elif (d_choice=="i"):
            list_questions()
        else:
            print ("invalid input")
    else:
        print ("Invalid username or password")
elif (choice=="u"):
    #Enter code to show quiz here
else:
    print ("invalid input")


def add_questions():
    # add code to add questions here
def list_questions():
