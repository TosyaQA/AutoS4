import pytest
from REST_API import get, create

def test_step1(get_token):
    result = get(get_token)
    lst = result['data']
    lst_id = [el["id"] for el in lst]
    assert 82504 in lst_id

def test_step2(get_token):
    create(get_token)
    result = get(get_token, True)
    lst = result['data']
    lst_id = [el["description"] for el in lst]
    assert 'test' in lst_id

if __name__ == '__main__':
    pytest.main(['-v'])
