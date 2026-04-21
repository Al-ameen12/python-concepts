import json

data = '''
{
    "name": "Al-ameen",
    "age": 30,
    "isDeveloper": true,
    "skills": ["Python", "JavaScript", "C++"],
    "address": {
        "street": "123 Main St",
        "city": "Lagos",
        "country": "Nigeria"
    }
}
'''

info = json.loads(data)
print('Name:', info['name'])
print('Address:', info['address']['city'])