import os
import pytest
import yaml
import requests
import mailer

with open('config.yaml', 'r') as f:
    conf = yaml.safe_load(f)
    
@pytest.fixture()
def get_token():
    response = requests.post(url=conf['login-url'], data={'username': conf['username'], 'password': conf['password']})
    return response.json()['token']

test_results = ''

def get_current_test():
    full_name = os.environ.get('PYTEST_CURRENT_TEST').split(' ')[0]
    test_file = full_name.split("::")[0].split('/')[-1].split('.py')[0]
    test_name = full_name.split("::")[1]
    return full_name, test_file, test_name

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    global test_results
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":
        full_name, test_file, test_name = get_current_test()
        if rep.failed:
            test_results = test_results + f"{full_name} - Failure\n"
        else:
            test_results = test_results + f"{full_name} - Success\n"

def pytest_unconfigure(config):
    mailer.send('Результаты выполнения тестов', test_results)