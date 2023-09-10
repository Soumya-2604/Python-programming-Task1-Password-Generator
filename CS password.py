import random
import string

#defining function to generate password
def generate_password(length,complexity):
    char=''
    if "u" in complexity:
        char += string.ascii_uppercase
    if "l" in complexity:
        char += string.ascii_lowercase
    if "d" in complexity:
        char += string.digits
    if "s" in complexity:
        char += string.punctuation
    if not char:
        print('please select at least one character type.')
        return None
    password= ''.join(random.choice(char) for _ in range(length))
    return password
def main():
    length=int(input('enter the desired length of the password :'))
    complexity =input("enter the choice for desired complexity : ").split(',')
    password=generate_password(length,complexity)
    if password:
        print(f'Generated password : {password}')
if __name__=="__main__":
    main()