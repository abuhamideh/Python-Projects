def main():
    while True:
        UserList = []
        UserList = str(input("Choose a few numbers: ")).split(',', )
        UserPower = int(input("To what power do you wish to raise this number: "))
        PowerMethod(UserList, UserPower)

def PowerMethod(list, power):
    newList = []
    for i in list:
        newList.append(int(i) ** power)
    print(newList)


main()
