import hashlib


def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode("utf-8"))
    return md5.hexdigest()


def register():
    username = input("username:")
    password = input("password:")
    db = {}
    password = calc_md5(password + username + 'the salt')
    db[username] = password
    return db


def login(username, password):
    if calc_md5(password + username + 'the salt') == db[username]:
        print('ok')
    else:
        print("username or password is not correct.")

print("...............\n Please register!\n...............")
db = register()
print("..............login..........")
name = input("please input your name: ")
password = input("please input your password: ")
login(name, password)
