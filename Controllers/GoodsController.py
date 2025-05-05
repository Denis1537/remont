from Models.Goods import *

class GoodsController:
    @classmethod
    def get(cls):
        return Goods.select()
    @classmethod
    def show(cls, id):
        return Goods.get_or_none(id)

    @classmethod
    def add(cls, name, cost, quantity, description):
        Goods.create(name=name,
                     cost=cost,
                     quantity=quantity,
                     description=description)

    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Goods.update({key: value}).where(Goods.id == id).execute()

    @classmethod
    def delete(cls,id):
        Goods.delete().where(Goods.id == id).execute()

if __name__ == "__main__":
    GoodsController.add('PS4 PRO', '1000', '10', 'OLD PS4 PRO')
    for Goods in GoodsController.get():
        print(Goods.id,Goods.name, Goods.quantity, Goods.description)