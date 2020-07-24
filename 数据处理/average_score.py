import json
data = json.loads(open('result.json', encoding='utf-8').read())
res = {}
for key in data:
    user = data[key]
    res[key]=0
    for i in user:
        res[key]+=data[key][i]["score"]
    res[key]=res[key]/len(data[key])
filename = 'average_score.json'
with open(filename, 'w', encoding='utf-8') as file_obj:
    json.dump(res, file_obj, ensure_ascii=False, indent=4)
