import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Farm_Website.settings')

import django
django.setup()
from website.models import Lot,Row

def populate():

    lots = {"a": {"num_rows": 13}, "b": {"num_rows": 10}, "c": {"num_rows": 45}, "d": {"num_rows": 17}}

    for lot_id, row_num in lots.items():
        lot = add_lot(lot_id)
        print(lot)
        print(row_num["num_rows"])
        for currentRow in range(row_num["num_rows"]):
            add_row(lot, currentRow+1)

def add_lot(id):
    l = Lot.objects.get_or_create(lotid=id)[0]
    l.save()
    return l

def add_row(lot_id,row_id):
    r = Row.objects.get_or_create(inlot=lot_id, rownum=row_id)[0]
    r.save()
    return r

if __name__ == '__main__':
    print("\nStarting population script...\n")
    populate()