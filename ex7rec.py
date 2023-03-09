def sumArray (array: list[int]):
    if len(array) == 0:
        return 0
    return array[0] + sumArray(array[1:]) 

def main():
    array = [1,3,5,7,9]
    print ("Somatorio de  [1,3,5,7,9] =", sumArray(array))

if __name__ == "__main__":
    main()
