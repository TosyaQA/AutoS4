import requests as requests
import yaml

with open('config.yaml', 'r') as f:
    conf = yaml.safe_load(f)

def get_token():
    response = requests.post(url=conf['login-url'], data={'username': conf['username'], 'password': conf['password']})
    return response.json()['token']

def get(token: str, my_posts: bool = False):
    params = {} if my_posts else {"owner": "notMe"}

    response = requests.get(conf["posts-url"],
                          headers={"X-Auth-Token": token},
                          params=params)
    return response.json()

def create(token: str):
    response = requests.post(conf["posts-url"], headers={"X-Auth-Token": token}, data={
        "title": 'test',
        "description": 'test',
        "content": 'test',
    })
    return response.content


if __name__ == '__main__':
    print(create(get_token()))