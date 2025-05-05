from pprint import pprint

from Models.User import *
from bcrypt import hashpw, gensalt, checkpw

class UserController:

    @classmethod
    def get(cls):
        return  User.select()

    @classmethod
    def show(cls, id):
        return User.get_or_none(id)

    @classmethod
    def show_login(cls, login):
        return User.get_or_none(User.login == login)

    @classmethod
    def add(cls, login, password, role_id):
        User.create(login=login,
                    password=password,
                    role_id=role_id)

    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            User.update({key: value}).where(User.id == id).execute()
    @classmethod
    def delete(cls, id):
        User.delete().where(User.id == id).execute()

    @classmethod
    def registration(cls, login, password, role_id):
        hash_password = hashpw(password.encode('utf-8'),gensalt())
        User.create( login = login, password = hash_password, role_id=role_id)


    @classmethod
    def auth(cls, login, password):
        if User.get_or_none(User.login == login) != None:
            hspassword = User.get_or_none(User.login == login).password

        if checkpw(password.encode('utf-8'),hspassword.encode('utf-8')):
            return True
        return False
if __name__ == "__main__":
    for row in UserController.get():
        print(row.id, row.login, row.password, row.role_id)


UserController.registration('user3','user3', '3')
#UserController.registration('cat23','Secur3P@ss!', '1')
#UserController.registration('sun4u','BlueSky#2023', '3')
#UserController.registration('star5','F1r3W@ll_Guard', '2')
#UserController.registration('fox99','Tr0ub1eM@ker', '3')
#UserController.registration('sky12','SunFl0wer$2023', '1')
#UserController.registration('moon3','N3v3rG1veUp!', '2')
#UserController.registration('dog78','M00nL1ght!', '3')
#UserController.registration('ice45','C0mpl3x!Ty_2023!', '1')
#UserController.registration('fire6','R@inb0w$h1ne', '2')
#UserController.registration('zen11','G0ld3nK3y!2023', '3')
#UserController.registration('joy22','T1ger$tr1pe#2023', '1')
#UserController.registration('max33','L1ghtn1ng@B0lt', '2')
#UserController.registration('neo44','Dr@gonF1re!2023', '3')
#UserController.registration('ace55','S3cr3tG@rden$', '1')
#UserController.registration('bee66','W1nd0wT0Sky#', '3')
#UserController.registration('art77','St@rl1ght*2023', '2')
#UserController.registration('fun88','M0untain$Top!', '1')
#UserController.registration('gem99','F0r3st#Tr3asure', '3')
#UserController.registration('pop00','Oc3anW@ve_2023', '2')
#UserController.registration('qwqwr','qw1qw', '3')