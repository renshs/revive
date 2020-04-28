from requests import post, get

# print(get('http://localhost:5000/api/news/1').json())

print(get('http://localhost:5000/api/users').json())

# print(post('http://localhost:5000/register',
#            json={'name': 'Vladimir',
#                  'email': 'put@in',
#                  'about': 'krytoi chel',
#                  'hashed_password': '123',
#                  }).json())


