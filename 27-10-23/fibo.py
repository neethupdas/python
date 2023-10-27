
def Fibonacci(number):
           if(number == 0):
                      return 0
           elif(number == 1):
                      return 1
           else:
                      return (Fibonacci(number - 2)+ Fibonacci(number - 1))
number = int(input("Enter the Range Number: "))
for n in range(0, number):
           print(Fibonacci(n))
