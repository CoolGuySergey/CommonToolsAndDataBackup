# OOP

import csv
import os

from Item import Item
from Phone import Phone

#==============================================================

if Item.all is not None:
    Item.all = []
#Instantiate from CSV
Item.instantiate_from_csv()

test = Phone("Brick", 40, 2)

print(len(Item.all))
