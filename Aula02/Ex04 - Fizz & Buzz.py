# %%

for i in range (1,101):
    msg = ""
    if i % 3 == 0:
        msg = msg + "Fizz"
    if i % 5 == 0:
        msg = msg + "Buzz"
    if msg == "":
        msg = i
    
    print(msg)