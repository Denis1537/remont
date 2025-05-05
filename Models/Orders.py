from Models.Base import *
from Models.User import *
from Models.Statuses import *
from Models.Payments import *

class Orders(Base):
     id = PrimaryKeyField()
     date = DateTimeField()
     user_id = ForeignKeyField(User)
     status_id = ForeignKeyField(Statuses)
     payments_id = ForeignKeyField(Payments)
     delivery_data = CharField()
     class Meta:
         table_name = 'Orders'

if __name__ == "__main__":
    pass