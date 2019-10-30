from utilities import util

def nameInput(prompt):
    name = input(prompt)
    return name.strip()


def getName():
    tempName = ""
    while True:
        tempName = nameInput("\nWhat is your name? >> ")
        
        if len(tempName) <= 1:
            print("Name is too short...")
            continue

        yes = util.yesOrNo(tempName + ", is that your name? (Y/N) >> ")

        if yes:
            return tempName
        else:
            continue
