# Python program to display the Fibonacci sequence
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
nterms = 7
# check if the number of terms is valid
if nterms <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonaccisequence:")
for i in range(nterms):

    print(recur_fibo(i))



OR



def recursive_fibonacci(n):
    if n<=1:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

def non_recursive_fibonacci(n):
    first=0
    second=1
    print(first)
    print(second)
    while n-2>0:
        third = first + second
        first=second
        second=third
        print(third)
        n-=1

if __name__=="__main__":
    n=10
    for i in range(n):
        print(recursive_fibonacci(i))
    
    non_recursive_fibonacci(n)
