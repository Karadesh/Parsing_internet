from unicodedata import name
import requests
import json

#Настоящий токен заменен на "ваш_токен" в целях безопасности.
# id моих сообществ можно найти в файле 'communities.json'

url = 'https://api.vk.com/method/groups.get?v=5.131&access_token=ваш_токен'
communities = requests.get(url)
json_communities = communities.json()
#print(json_communities)
inside_response = json_communities.get('response')
response_items = inside_response.get('items')
communities_object = {'communities': response_items}
print(response_items)
with open('communities.json', 'w', encoding='utf-8') as a:
    json.dump(communities_object, a)
