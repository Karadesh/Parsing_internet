import requests
import json

url = 'https://api.github.com/users/Karadesh/repos'
repos = requests.get(url)
json_repos = repos.json()

repos_list = []
repos_object = {}
for i in json_repos:
    repos_list.append(i.get('name'))
    print(i.get('name'))
repos_object['repos'] = repos_list
with open('repos.json', 'w', encoding='utf-8') as a:
    json.dump(repos_object, a)