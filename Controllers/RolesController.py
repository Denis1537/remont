from Models.Roles import *

class RolesController:

    @classmethod
    def get(cls):
        return Roles.select()

    @classmethod
    def show(cls,id):
        return Roles.get_or_none(id)

if __name__ == "__main__":
    for row in RolesController.get():
        print(row.id, row.role_name)