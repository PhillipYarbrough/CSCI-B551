import random as r
from warnings import catch_warnings

def remark(x):
    cor_list = ["Very good!", "Nice work!", "Keep up the good work!"]
    inc_list = ["No. Please try again.","Wrong. Try once more.","No.Keep trying."]
        
    if x == 0:
        temp = r.randint(0,(len(cor_list)-1))
        return(cor_list[temp])
    
    else:
        temp = r.randint(0,(len(inc_list)-1))
        return(inc_list[temp])


def easy_int_return():
    x = r.randint(1,9)
    return (x)
def hard_int_return():
    x = r.randint(1,99)
    return (x)

def problem_type(x,temp1,temp2):
    if x ==1:
        prompt = ("How much is " + str(temp1) + " plus " + str(temp2)+ " ? \n" )
        answer = temp1 + temp2
        return (prompt, str(answer))
    elif x ==2:
        prompt = ("How much is " + str(temp1) + " minus " + str(temp2)+ " ? \n" )
        answer = temp1 - temp2
        return (prompt, str(answer))
    elif x==3:
        prompt = ("How much is " + str(temp1) + " times " + str(temp2)+ " ? \n" )
        answer = temp1 * temp2
        return (prompt, str(answer))
    elif x==4:
        prompt = ("How much is " + str(temp1) + " divided by " + str(temp2)+ " ?\n If whole number, add '.0 to integer. \n Round to the nearest hundreth \n" )
        answer = round(float(temp1 / temp2),2)
        return (prompt, str(answer))
    elif x == 5:
        x = r.randint(1,4)
        return(problem_type(x,temp1,temp2))

def main():

    difficulty = int(input("Difficulty Level 1 or 2 ? \n"))
    if difficulty == 1:
        temp1 = easy_int_return()
        temp2 = easy_int_return()
    elif difficulty == 2:
        temp1 = hard_int_return()
        temp2 = hard_int_return()

    operand = int(input("Pick problem type. 1:Addition  2:Subtraction  3:Multiplication  4:Division 5:Random \n"))
    catch = problem_type(operand,temp1,temp2)
    problem = catch[0]
    solution = catch[1]
    
    statement = "Would you like to continue? Yes or No \n"
    proceed = " "
    while proceed!= "No":
        answer = input(problem)
        if proceed == "No":
            print("Goodbye.")
            break 

        elif answer == solution:
            print(remark(0))
            proceed = input(statement)
            if proceed == "No":
                print("Goodbye.")
                break
            
            if difficulty == 1:
                temp1 = easy_int_return()
                temp2 = easy_int_return()
            elif difficulty == 2:
                temp1 = hard_int_return()
                temp2 = hard_int_return()
            operand = int(input("Pick problem type. 1:Addition  2:Subtraction  3:Multiplication  4:Division 5:Random \n"))
            catch = problem_type(operand,temp1,temp2)
            problem = catch[0]
            solution = catch[1]

            
        else:
            print(remark(1))
            proceed = input(statement)
main()



