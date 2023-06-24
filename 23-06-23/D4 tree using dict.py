#Dictionaries(Forest of 3 trees:)

Families={
    'Nick':
    { 'klaus' : { 'Damon','Stefan'},
      'Caroline' : { 'Enid'}},
    'Mick':
    { 'Ben': {'Olive'},      'Zeke':{'zared'},
      'sanvi':{'vance'}},
    'Zade':
    { 'Adeline':'Enzo','Roman': 'Reid'}

    }
for parent,children in Families.items():
    print(f"{parent} has {len(children)} kid(s):")
    print(f" {' and '.join([str(child)for child in[*children]])}")
