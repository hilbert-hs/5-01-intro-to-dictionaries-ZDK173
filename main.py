# 5.01 Internet Slang

internet_slang = {
    'nbd': 'no big deal', 
    'imo': 'in my opinion',
    'btw': 'by the way',
    'smh': 'shaking my head',
    'tbh': 'to be honest',
    'idk': "I don't know"
}
for trm in internet_slang:
    print(f"{trm} means {internet_slang[trm]}.")
while True:
    term = input("What abbreviation would you like to look up? ")

    if term in internet_slang:
        print(f'{term} means {internet_slang[term]}.')
    else:
        print("That isn't a term I know.")
        add_to = input("Would you like to add it? (Y/N) ")
        if add_to.lower() == 'y':
            # add term to dictionary
            definition = input(f'What does {term} mean? ')
            internet_slang[term] = definition
        else:
            print("Goodbye")