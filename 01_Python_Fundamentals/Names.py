# Part I
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def names(arr):
    for value in arr:
        print value.get('first_name'), value.get('last_name')


names(students)

# Part II
users = {
    'students': [
        {'first_name':  'Michael', 'last_name': 'Jordan'},
        {'first_name': 'John', 'last_name': 'Rosales'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ],
    'instructors': [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'Martin', 'last_name': 'Puryear'}
    ]
}


def more_names(arr):
    for key in arr:
        print key.upper()
        count = 1
        for i in arr[key]:
            print count, "- " + i['last_name'], i['first_name'], len(i['last_name']) + len(i['first_name'])


more_names(users)
