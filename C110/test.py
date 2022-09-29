import time
def countdown(seconds):
    while seconds>0:
        min = seconds/60
        x =seconds%60
        timer = f'{min} : {x}' #f-string
        seconds-=1
        print(timer)
    print("Time Up")

seconds = int(input("enter seconds"))
countdown(seconds)