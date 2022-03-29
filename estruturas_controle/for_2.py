word = 'Paralelepiledo'

for l in word:
    print(l, end=', ')
print()

approved = ['Erick', 'Joao', 'Vinicius', 'Victor']

for name in approved:
    print(name)

for (pos, name) in enumerate(approved):
    print('{0} - {1}'.format(pos+1, name))

weekdays = ('Sunday', 'Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday')

for day in weekdays:
    print(day)
    
for letter in set('This is very very cool'):
    print(letter)
    
#Literal set
for l in {1, 2, 2, 3, 4, 5, 6, 6, 7}:
    print(l)
