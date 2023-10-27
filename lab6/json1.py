import json
with open('sample-data.json') as file:
    data = json.load(file)

# print(json.dumps(data, indent=2))

print('Interface Status')
print('==================================================================================')
print('DN','\t','\t','\t''                     ','Description','\t','Speed','\t','    ','MTU')
print('-------------------------------------------','----------------',' ---------',' ---------')

for i in data['imdata']:
    print(i['l1PhysIf']['attributes']['dn'],'                   ',i['l1PhysIf']['attributes']['descr'],
          i['l1PhysIf']['attributes']['speed'],'    ',i['l1PhysIf']['attributes']['mtu'])

# print(data['imdata'])