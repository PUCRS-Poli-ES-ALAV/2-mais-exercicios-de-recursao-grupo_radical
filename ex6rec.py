def int2bin(n:int) -> str:
    if n == 0:
        return "0"
    return int2bin(n//2) + str(n%2)

def main():
    print ("bin de 11 =", int2bin(11))
    print ("bin de 111 =", int2bin(111))

if __name__ == "__main__":
    main()
