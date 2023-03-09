def fat(n: int) -> int:
    if n == 0:
        return 1
    return n * fat(n - 1)

def main():
    print ("fatorial de 5 =", fat(5))

if __name__ == "__main__":
    main()
