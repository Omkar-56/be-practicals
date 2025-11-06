it_count = 0
rec_count = 0

def fib(n):
    global it_count
    it_count = 0 
    a = 0
    b = 1
    ser = []

    for _ in range(n):
        it_count += 1
        ser.append(a)
        a, b = b, a + b
        
    return ser

def fib_rec(n):
    global rec_count
    rec_count+=1

    if n <= 1:
        return n
    
    return fib_rec(n-1) + fib_rec(n-2)


if __name__ == "__main__":
    n = 10
    fib_series = fib(n)
    print(f"\nFibonacci using iteration:\t{fib_series}")
    print(f"Iteration counter:\t{it_count}\nTime Complexity: O(n) (linear growth)")

    fib_series = []
    for i in range(n):
        fib_series.append(fib_rec(i))
    print(f"\n\nFibonacci using recursion:\t{fib_series}")
    print(f"Recursion counter:\t{rec_count}\nTime Complexity: O(2^n) (exponential growth)\n")