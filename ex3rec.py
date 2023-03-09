def fib(n: int) -> int:
    if n < 0:
        return "Erro"
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fib(n-1) + fib(n-2)
    
def main():
    print ("fib de 5 =", fib(5))

if __name__ == "__main__":
    main()
