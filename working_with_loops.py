done = False
people = []

while not done:
    name = input('what your name is: ')
    if not name:
        done = True
    else:
        color = input("whats your favorite color: ")
        age = input("how old are you: ")
        question = input('do you want to add someone else: ' )
    if question == 'no':
        done = True
    people.append({'name': name, 'color': color, 'age': age})

#print(people)
for x in people:
    print('Name: ' + x['name'])
    print('Favorite Color: ' + x['color'])
    print('Age: ' + x['age'])
