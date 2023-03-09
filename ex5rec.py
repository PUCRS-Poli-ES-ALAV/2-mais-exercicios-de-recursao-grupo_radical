def isPal(text: str) -> str:
    if (len(text) == 0):
        return True
    if text[0] != text[-1]:
        return False
   
    isPal(text[1:-1])
    return True
    
def main():
    text = "aba"
    print ("Palindromo aba =", isPal(text))
   

if __name__ == "__main__":
    main()
