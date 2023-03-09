def sum_between(j:int, k:int) -> int:
    if (j == k):
        return j
    if (j < k):
        return j + sum_between(j + 1, k)
    if (j > k):
        return j + sum_between(j - 1, k)

def main():
    print ("soma de 5 a 10 =", sum_between(5, 10))
    print ("soma de -10 a -5 =", sum_between(-10, -5))
    print ("soma de 10 a 5 =", sum_between(10, 5))
    print ("soma de -5 a -10 =", sum_between(-5, -10))
    
if __name__ == "__main__":
    main()