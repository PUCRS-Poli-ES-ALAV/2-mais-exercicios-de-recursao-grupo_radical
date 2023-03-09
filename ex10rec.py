def numDig (n):
    if n < 10 and n >= 0:
        return 1
    if n > -10 and n <= 0:
        return 1
    return 1 + numDig(n/10) 


def main():
   
    print ("Num de digitos de um inteiro (5292) =", numDig(-5292))
    
if __name__ == "__main__":
    main()
