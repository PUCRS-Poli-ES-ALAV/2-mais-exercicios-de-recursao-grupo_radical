def sum(n:int) -> int:
    if n == 0:
        return 0
    if (n > 0):
        return n + sum(n - 1)
    if (n < 0):
        return n + sum(n + 1)

def main():
    print ("soma de 5 =", sum(5))
    print ("soma de -5 =", sum(-5))

if __name__ == "__main__":
    main()