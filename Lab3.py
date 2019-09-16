#Lab 3, Jonathan Kelly, 9/12/19

def main():
    
    x = eval(input("How tall is the tree: "))
    x = round(x)
    
    count = 1
    
    while(x <= 0):
        x = eval(input("Please enter a positive height: "))
        x = round(x)
        
    x1 = x
        
    for i in range(x, 0, -1):
        for i in range(x - 1, 0, -1):
            print(" ", end = '')
        
        for i in range(0, count):
            print("#", end = '')
        
        x = x - 1
        count = count + 2
        print(" ")
    
    for i in range(x1 - 1, 0, -1):
            print(" ", end = '')
    print("#")
    
main()