import json

fin = open('laba24/in.json','r')
fout = open('laba24/out.json','w')

tasks = json.loads(fin.read())

users = {}
for task in tasks:
    if task['userId'] not in users:
        users[task['userId']] = 0
    if task['completed']:
        users[task['userId']] += 1

output = []
for user in users:
    output.append({'userId':user, 'task_completed':users[user]})

json.dump(output, fout, indent=2)