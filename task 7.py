#task1

n=int(input("enter the num"))
def calculate_fibonacci(n):
    a=0
    b=1
    c=0
    print(a)
    print(b)
    i=1
    while i<n:
        c=a+b
        a=b
        b=c
        i=i+1
        print(c)


calculate_fibonacci(n)

#task2


tasks=["prime numbers","even numbers"]
def add_task(tasks):
    TASK="fibonacci numbers"
    tasks.append(TASK)

add_task(tasks)
print(tasks)





def view(tasks):
    print(tasks)

view(tasks)



def mark_task(tasks):
   TASK=("even numbers")
ans=(input("Have you complete this task"))   

mark_task(tasks)
print(ans)



def remove_task(tasks):
    TASK="prime numbers"
    tasks.remove(TASK)

remove_task(tasks)
print(tasks)




