from Models.Base import *
class Statuses(Base):
    id = PrimaryKeyField()
    status = CharField()
    class Meta:
        table_name = 'Status'

if __name__ == "__main__":
    pass