##################################################


def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    # TODO your code here
    fullname = (fullname.upper()).strip()
    initials = [fullname[0]]
    # Scan for spaces and grab the following letter
    for letter in range(len(fullname)-1):
        if fullname[letter] == " ":
            initials.append(fullname[letter+1])
    return("".join(initials))


def main():
    print(get_initials(input("What's your full name?")))


if __name__ == "__main__":
    main()
