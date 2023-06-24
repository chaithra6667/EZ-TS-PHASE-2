#create 2 stack-push if input even in stack1 others push it to stack2

stack_1=[]
stack_2=[]

def push():
    for i in range(5):
        element=int(input("Enter the element"))
        if (element%2==0):
            stack_1.append(element)
        else:
            stack_2.append(element)

def pop_element():
    pop_what=input("1 or 2")
    if pop_what=="1":
        if not stack_1:
            print("stack is empty:",e)
        else:
            e=stack_1.pop()
            print("removed element:",e)
            print(stack_1)
    else:
        if not stack_2:
            print("stack is empty:",e)
        else:
            e=stack_2.pop()
            print("removed element:",e)
            print(stack_2)

def display():
    what=input("1 or 2:")
    if what=="1":
        print(stack_1)
    else:
        print(stack_2)

while True:
    print("Select operation 1.push 2.pop 3.display 4.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Enter a valid option")

            
