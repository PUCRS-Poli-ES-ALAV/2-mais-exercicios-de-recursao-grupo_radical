def findSubString(string: str, subString: str) -> bool:
    return string.endswith(subString) or findSubString(string[:-1], subString)

def main():
    print ("cba contains cb?",findSubString("cba", "cb"))

if __name__ == "__main__":
    main()
