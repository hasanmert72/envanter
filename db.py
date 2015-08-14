__author__ = 'hasan'

from PyQt4 import QtCore, QtGui
from PyQt4.QtSql import *
from PyQt4.QtGui import *
import MySQLdb

import MySQLdb
y = MySQLdb.connect(host="127.0.0.1",user="root",passwd="root",db="envanter")
with y:
    x = y.cursor()
    x.execute("INSERT INTO urunbilgileri VALUES('1','500','Cissco','Firewall','64','128','123')")
x.close()