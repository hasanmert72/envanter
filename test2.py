__author__ = 'hasan'
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import user

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(457, 300)
        Dialog.setWindowTitle(_fromUtf8(""))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)

        users = {}
        status = ""

        def displayMenu():
            status = raw_input("Yeni kayit olusturmak istermisiniz e/h Cikmak için q basiniz : ")
            if status == "h":
                oldUser()
            elif status == "e":
                newUser()

        def newUser():
            createLogin = raw_input("Yeni Kullanıcı adı : ")

            if createLogin in users: # kullanıcı adı şifre oluşturma
                print "\nLogin name already exist!\n"
            else:
                createPassw = raw_input("Yeni şifre : ")
                users[createLogin] = createPassw # HESAP OLUŞTURULDU !
                print("\nHesap oluşturuldu!\n")

        def oldUser(): #login
            login = raw_input("Kullanıcı adınız : ")
            passw = raw_input("Şifreniz : ")

            # giriş kontrolü
            if login in users and users[login] == passw:
                print "\nGiriş başarılı!\n"
            else:
                print "\nKullanıcı adınız veya şifreniz hatalı!\n"

        while status != "q":
            displayMenu()


        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 60, 101, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 100, 81, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(180, 60, 113, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 100, 113, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self.label.setText(_translate("Dialog", "Kullanici Adi :", None))
        self.label_2.setText(_translate("Dialog", "Sifre :", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())



