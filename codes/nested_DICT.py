dict2 = {  # outer dictionary
    'Name': 'Steve',
    'Age': 30,
    'Designation': 'Programmer',
    'address': {  # inner dictionary
           'Street': 'Brigade Road',
           'City': 'Bangalore',
           'Country': 'India'
    }
}
print("len() method :", len(dict2))
print("len() method with keys() :", len(dict2.keys()))
print("len() method with values():", len(dict2.values()))

#as the length will be same as of every condition but we have 7 keys in the dictionary