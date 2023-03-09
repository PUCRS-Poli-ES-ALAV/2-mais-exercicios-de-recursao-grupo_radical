def permutations(str: str) -> list[str]:
    if len(str) == 1:
        return str    
    return [char + perm \
        for char in str \
        for perm in permutations(str.replace(char, ""))]

def main():
    str = "cao"
    print ("Permutacoes de cao =",permutations(str))
    
if __name__ == "__main__":
    main()
    