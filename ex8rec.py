def find_biggest(array: list[int], biggest:int = 0) -> int:
    if len(array) == 0:
        return biggest
    return find_biggest (array[1:], max(biggest, array[0]))

def main():
    array = [1,13,5,7,9]
    print ("Maior elemento de  [1,13,5,7,9] =", find_biggest(array))
    
if __name__ == "__main__":
    main()
