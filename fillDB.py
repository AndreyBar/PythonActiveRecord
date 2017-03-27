from user import User

"""Generic names to test our DB"""

names = ['Anatoliy','Andriy', 'Bogdan', 'Borys', 'Viktor',
'Volodymyr', 'Gennady', 'Petro', 'Pavlo', 'John']

surnames = ['Ponchyk', 'Vatra', 'Syrota', 'Ivaniv', 'Ninja',
'Lapochka', 'Kolobok', 'Vovk', 'Lys', 'Smith']

def fillDB():
    for i in range(0, len(names)):
        current_user = User()
        current_user.name = names[i]
        current_user.surname = surnames[i]
        current_user.save()


if __name__ == '__main__':
    fillDB()