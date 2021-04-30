# key --> value

# sehirler = ['Zonguldak','İstanbul']
# plakalar = [67,34]

# print(plakalar[sehirler.index('İstanbul')])

# print(plakalar['Zonguldak']) --> 67
# print(plakalar['İstanbul']) --> 34

# example = { 'key' : value }

# plakalar = { 'Zonguldak' : 67, 'İstanbul' : 34 }

# print(plakalar['Zonguldak'])
# print(plakalar['İstanbul'])

# plakalar['Ankara'] = 6

# print(plakalar)
# print(plakalar['Ankara'])

users = {

    'Mehmet': {
        'age': 18,
        'roles': ['admin','user'],
        'phone': '5349182761',
        'address': 'Zonguldak',
        'email': 'mehmet@gmail.com'
    }
}

print(users['Mehmet']['roles'][0])