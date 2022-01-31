import requests

url = "http://127.0.0.1:3002/"

api = {
    'users': {
        'add_friend': 'users/add_friend',
        'add_playlist': 'users/add_playlist',
        'add_user': 'users/add_user',
        'change_password': 'users/change_password',
        'get_playlist': 'users/get_playlist',
        'get_user': 'users/get_user'
    }
}

params = '?user_name='
username = 'Arnold'
response = requests.get(url + api['users']['get_user'] + params + username)
print(response.json())
