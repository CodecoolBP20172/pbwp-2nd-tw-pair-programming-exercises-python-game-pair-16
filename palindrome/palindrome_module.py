
def palindrome(str):
    str = ''.join(str.split())
    if str.lower() == str.lower()[::-1]: 
        return True
    else: 
        return False

def main():
    return


if __name__ == '__main__':
    main()

