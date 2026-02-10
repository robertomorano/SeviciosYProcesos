import random 
def proceso_1(fecha):
    
    with open (f"{fecha}.txt", "w") as file:
        for i in range(20):
            file.write(random.randint(0,21))
            file.write(".")
            decimal = random.randint(0,99)
            if(decimal<10):
                file.write(f"0")
            file.write(decimal)

            



def proceso_2():
    pass