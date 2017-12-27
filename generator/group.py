__author__ = "wdolowicz"


from model.group import Group
import random
import string
import os.path
import getopt
import sys
import time


import clr
clr.AddReferenceByName('Microsoft.Office.Interop.Excel, Version=15.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c')
from Microsoft.Office.Interop import Excel


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
if not os.path.exists("C:/Devel/ironpython_training/data/"):
    os.makedirs("C:/Devel/ironpython_training/data/")
    f = "data/groups.xlsx"
else:
    f = "data/groups.xlsx"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="")] + [
    Group(name=random_string("name", 10))
    for i in range(n)
    ]

if os.path.exists("C:/Devel/ironpython_training/data/groups.xlsx"):
    os.remove("C:/Devel/ironpython_training/data/groups.xlsx")
else:
    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

    excel = Excel.ApplicationClass()
    excel.Visible = True

    workbook = excel.Workbooks.add()
    sheet = workbook.ActiveSheet

    for i in range(len(testdata)):
        sheet.Range["A%s" % (i+1)].Value2 = testdata[i].name

    workbook.SaveAs(file)

    time.sleep(10)

    excel.Quit()
