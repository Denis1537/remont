from datetime import datetime

from Models.Payments import *

class PaymentsController:
    @classmethod
    def get(cls):
        return Payments.select()

    @classmethod
    def show(cls, id):
        return Payments.get_or_none(id)
    @classmethod
    def add(cls,payment,date = datetime.now()):
        #if date is None:
            #date = datetime.now()
        Payments.create(payment=payment, date= date)


if __name__ == "__main__":
    PaymentsController.add(1888.25)
    for row in PaymentsController.get():
        print(row.id, row.summ, row.date)