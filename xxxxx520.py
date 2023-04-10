import requests
import os

def one():
    # index
    r = requests.get('https://www.xxxxx520.org/')
    print(r.cookies)
    cookies = {}
    cookies |= r.cookies.get_dict()
    print('cookies  ', cookies)

    # login
    r = requests.post('https://www.xxxxx520.org/wp-admin/admin-ajax.php', cookies=cookies,
                    data={'action': 'user_login', 'username': 'outman', 'password': os.environ.get('PASS_WORD')})
    print(r.cookies.get_dict())
    cookies |= r.cookies.get_dict()
    print('cookies  ', cookies)

    # checkout
    r = requests.post('https://www.xxxxx520.org/wp-admin/admin-ajax.php', cookies=cookies,
                    data={'action': 'user_qiandao'})
    print(r.json())


def two():
    # index
    r = requests.get('https://xxxxx520.cam/3ajuzuo')
    print(r.cookies)
    cookies = {}
    cookies |= r.cookies.get_dict()
    print('cookies  ', cookies)

    # login
    r = requests.post('https://xxxxx520.cam/wp-admin/admin-ajax.php', cookies=cookies,
                    data={'action': 'user_login', 'username': 'outman', 'password': 'fUpdor-8nimco-berjin'})
    print(r.cookies.get_dict())
    cookies |= r.cookies.get_dict()
    print('cookies  ', cookies)

    # checkout
    r = requests.post('https://xxxxx520.cam/wp-admin/admin-ajax.php', cookies=cookies,
                    data={'action': 'user_qiandao'})
    print(r.json())


if __name__ == '__main__':
    one()
    two()

