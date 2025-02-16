import json

task = json.load(open('sample-date.json', 'r', encoding='utf-8'))

arr = task['imdata']

print('Interface Status')
print('='*80)

print(f"{'DN':<50} {'Description':<20}  Speed    MTU  ")

print(f"{'-'*50} {'-'*20}  {'-'*6}  {'-'*6}")



for i in arr:
    print(f"{i['l1PhysIf']['attributes']['dn']:<50} {i['l1PhysIf']['attributes']['descr']:<20}  {i['l1PhysIf']['attributes']['speed']:<6}  {i['l1PhysIf']['attributes']['mtu']:<6}") 