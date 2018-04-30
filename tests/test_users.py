import pytest
import subprocess
from hr import users

#encripted password
password = '$6$JEtGef5Ky.7MfevO$kGS4WvXrnviyvkZdvlMOWxh/LKbh0gB.7Gb6iZ0Pdhep7qtNUD1JSA.PaRaYX98wqSf0NGJA8vnnhbTHbiSeI/'

user_dict = {
    'user' : 'Kevin',
    'group' : ['wheel', 'dev'],
    'password' : password
}
def test_users_add(mocker):
    """
    Given a user dictionary. `users.add(...)` should
    utilize `useradd` to create a user with the password
    and groups.
    """
    mocker.patch('subprocess.call')
    users.add(user_dict)
    subprocess.call.assert_called_with([
        'useradd',
        '-p',
        password,
        '-G',
        'wheel,dev',
        'kevin'
    ])
def test_users_remove(mocker):
    """
    Given a user dictionary, `users.remove(...)` should
    utilize `userdel` to delete the user.
    """
    mocker.patch('subprocess.call')
    users.remove(user_dict)
    subprocess.call.assert_called_with([
        'userdel',
        '-r',
        'kevin'
    ])

    
def test_user_update(mocker):
    """
    Given a user dictionary, `user.update(...)` should utilize
    `usermod` to update the user
    """
    mocker.patch('subprocess.call')
    users.update(user_dict)
    subprocess.call.assert_called_with([
        'usermod',
        '-p',
        password,
        '-G',
        'wheel,dev',
        'kevin'
    ])
def test_users_sync(mocker):
    """
    Given a list of user dictionaries, `users.sync(...)` should
    create missing users, remove extra non-system users, and update
    existing users. A list of existing usernames can be passed in
    or default users will be used.
    """
    existing_user_names = ['kevin', 'bob']
    users_info = [
            user_dict = {'name': 'joe', 'groups':['wheel'], 'password':password}   
    ]
    mocker.patch('subprocess.call')
    users.sync(users_info, existing_user_names)
       subprocess.call.assert_has_calls([
        mocker.call([
            'usermod',
            '-p',
            password,
            '-G',
            'wheel,dev',
            'kevin',
        ]),
        mocker.call([
            'useradd',
            '-p',
            password,
            '-G',
            'wheel',
            'jose',
        ]),
        mocker.call([
            'userdel',
            '-r',
            'bob',
        ]),
    ])






