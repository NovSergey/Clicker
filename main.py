import sqlite3
import sys
import traceback
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from random import randrange
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
conn = sqlite3.connect("data.db")
cursor = conn.cursor()


class nach(QMainWindow):
    def __init__(self):
        global countmoney, xp, nick
        super().__init__()
        uic.loadUi('design.ui', self)
        self.btn1.clicked.connect(self.reg)
        self.btn2.clicked.connect(self.inp)

    def reg(self):
        self.w0 = reg()
        self.w0.show()
        self.close()

    def inp(self):
        self.w = inp()
        self.w.show()
        self.hide()


class inp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design0.ui', self)
        self.btn1.clicked.connect(self.play)

    def play(self):
        global nick, countmoney, xp
        try:
            db = QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('data.db')
            db.open()
            nick = self.le.text()
            r2 = cursor.execute(f"SELECT r2 FROM nicks WHERE nick = '{nick}'")
            r3 = cursor.execute(f"SELECT r3 FROM nicks WHERE nick = '{nick}'")
            r4 = cursor.execute(f"SELECT r4 FROM nicks WHERE nick = '{nick}'")
            r5 = cursor.execute(f"SELECT r5 FROM nicks WHERE nick = '{nick}'")
            r6 = cursor.execute(f"SELECT r6 FROM nicks WHERE nick = '{nick}'")
            r7 = cursor.execute(f"SELECT r4 FROM nicks WHERE nick = '{nick}'")
            countmoney = cursor.execute(f"SELECT money FROM nicks WHERE nick = '{nick}'").fetchone()
            xp = cursor.execute(f"SELECT exp FROM nicks WHERE nick = '{nick}'").fetchone()
            countmoney = str(countmoney)
            countmoney = countmoney.replace('(', '')
            countmoney = countmoney.replace(')', '')
            countmoney = countmoney.replace(',', '')
            countmoney = int(countmoney)
            print(xp)
            xp = str(xp)
            xp = xp.replace('(', '')
            xp = xp.replace(')', '')
            xp = xp.replace(',', '')
            xp = int(xp)
            self.w0 = MyWindow()
            self.w0.show()
            self.hide()
        except ValueError:
            self.msg = QtWidgets.QMessageBox.question(self, "Ошибка", "Такого никнейма нет",QtWidgets.QMessageBox.Ok)

        except sqlite3.OperationalError:
            self.msg = QtWidgets.QMessageBox.question(self, "Ошибка", "Такого никнейма нет",QtWidgets.QMessageBox.Ok)



class reg(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design1.ui', self)
        self.btn1.clicked.connect(self.play)


    def play(self):
        cursor.execute("""CREATE TABLE IF NOT EXISTS nicks (
    nick  STRING    PRIMARY KEY
                  NOT NULL,
    r2    BOOLEAN,
    r3    BOOLEAN,
    r4    BOOLEAN,
    r5    BOOLEAN,
    r6    BOOLEAN,
    r7    BOOLEAN,
    money INTEGER,
    exp   INTEGER
)
""")
        self.play1()
    def play1(self):
        global countmoney,xp, nick
        try:
            db = QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('data.db')
            db.open()
            nick = self.le1.text()
            cursor.execute(f"INSERT INTO nicks VALUES ('{nick}', 0,0,0,0,0,0,0,0)")
            conn.commit()
            countmoney = 0
            xp = 0
            self.w1 = MyWindow()
            self.w1.show()
            self.hide()
        except sqlite3.IntegrityError:
            self.msg = QtWidgets.QMessageBox.question(self, "Ошибка", "Такой никнейм уже существует",QtWidgets.QMessageBox.Ok)

class MyWindow(QMainWindow):
    global nick
    def __init__(self):
        global countmoney, moneyeffect, i1,i2, i3, i4, check1, check2, check3, check4
        super().__init__()
        uic.loadUi('design2.ui', self)
        moneyeffect = 0
        i1, i2, i3, i4 = 0, 0, 0, 0
        check1, check2, check3, check4 = 0, 0, 0, 0
        self.needxp = 1000
        self.lvl = 1
        self.ng = 1000
        self.moneyadd = 1
        self.lb2.setText(f"Рублей: {countmoney}")
        self.lb13.setText(f"{xp}|{self.needxp} xp")
        self.btn1.clicked.connect(self.click)

        self.btn2.clicked.connect(self.rab1)

        self.btn10.clicked.connect(self.buy1)
        self.btn3.clicked.connect(self.rab2)
        self.btn3.setEnabled(False)

        self.btn11.clicked.connect(self.buy2)
        self.btn4.clicked.connect(self.rab3)
        self.btn4.setEnabled(False)

        self.btn12.clicked.connect(self.buy3)
        self.btn5.clicked.connect(self.rab4)
        self.btn5.setEnabled(False)

        self.btn13.clicked.connect(self.buy4)
        self.btn6.clicked.connect(self.rab5)
        self.btn6.setEnabled(False)

        self.btn14.clicked.connect(self.buy5)
        self.btn7.clicked.connect(self.rab6)
        self.btn7.setEnabled(False)

        self.btn15.clicked.connect(self.buy6)
        self.btn8.clicked.connect(self.rab7)
        self.btn8.setEnabled(False)

        self.btn16.clicked.connect(self.ef1)
        self.btn16.setEnabled(False)

        self.btn17.clicked.connect(self.ef2)
        self.btn17.setEnabled(False)

        self.btn18.clicked.connect(self.ef3)
        self.btn18.setEnabled(False)

        self.btn19.clicked.connect(self.ef4)
        self.btn19.setEnabled(False)
        self.rab1()
        if countmoney >= 1500 and check1 == 0:
            self.btn16.setEnabled(True)

        if countmoney >= 3500 and check2 == 0:
            self.btn17.setEnabled(True)

        if countmoney >= 6000 and check3 == 0:
            self.btn18.setEnabled(True)

        if countmoney >= 12000 and check4 == 0:
            self.btn19.setEnabled(True)

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(
            self,
            "Выход",
            "Вы хотите сохранить?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )

        if reply == QtWidgets.QMessageBox.Yes:
            self.save()
            event.accept()
        else:
            event.accept()

    def save(self):
        global nick
        cursor.execute(f"UPDATE nicks SET money = {countmoney} WHERE nick = '{nick}'")
        cursor.execute(f"UPDATE nicks SET exp = {xp} WHERE nick = '{nick}'")
        conn.commit()

    def ef1(self):
        global countmoney, moneyeffect, i1, check1
        countmoney -= 1500
        self.lb2.setText(f"Рублей: {countmoney}")
        check1 = 1
        self.btn16.setEnabled(False)
        moneyeffect += 1
        if rab == 1:
            self.rab1()

        if rab == 2:
            self.rab2()

        if rab == 3:
            self.rab3()

        if rab == 4:
            self.rab4()

        if rab == 5:
            self.rab5()

        if rab == 6:
            self.rab6()


    def ef2(self):
        global countmoney, moneyeffect, i2, check2
        countmoney -= 3500
        self.lb2.setText(f"Рублей: {countmoney}")
        check2 = 1
        self.btn17.setEnabled(False)
        moneyeffect += 4
        if rab == 1:
            self.rab1()

        if rab == 2:
            self.rab2()

        if rab == 3:
            self.rab3()

        if rab == 4:
            self.rab4()

        if rab == 5:
            self.rab5()

        if rab == 6:
            self.rab6()

    def ef3(self):
        global countmoney, moneyeffect, i3, check3
        countmoney -= 6000
        self.lb2.setText(f"Рублей: {countmoney}")
        check3 = 1
        self.btn18.setEnabled(False)
        moneyeffect += 8
        if rab == 1:
            self.rab1()

        if rab == 2:
            self.rab2()

        if rab == 3:
            self.rab3()

        if rab == 4:
            self.rab4()

        if rab == 5:
            self.rab5()

        if rab == 6:
            self.rab6()

    def ef4(self):
        global countmoney, moneyeffect, i4, check4
        countmoney -= 12000
        self.lb2.setText(f"Рублей: {countmoney}")
        check4 = 1
        self.btn19.setEnabled(False)
        moneyeffect += 16
        if rab == 1:
            self.rab1()

        if rab == 2:
            self.rab2()

        if rab == 3:
            self.rab3()

        if rab == 4:
            self.rab4()

        if rab == 5:
            self.rab5()

        if rab == 6:
            self.rab6()


    def click(self):
        global countmoney, moneyeffect, check1, check2, check3, check4, i1, i2, i3, i4, xp
        countmoney += self.moneyadd
        xp += 1
        self.lb2.setText(f"Рублей: {countmoney}")
        self.lb13.setText(f"{xp}|{self.needxp} xp")
        if xp >= self.needxp:
            self.lvl += 1
            countmoney += self.ng
            self.lb12.setText(f"Твой лвл: {self.lvl}")
            self.lb13.setText(f"{xp}|{self.needxp} xp")
            if self.lvl == 2:
                self.ng += 9000
                self.needxp += 9000
            else:
                self.ng += 10000
                self.needxp += 10000

        if countmoney >= 1500 and check1 == 0:
            self.btn16.setEnabled(True)

        if countmoney >= 3500 and check2 == 0:
            self.btn17.setEnabled(True)

        if countmoney >= 6000 and check3 == 0:
            self.btn18.setEnabled(True)

        if countmoney >= 12000 and check4 == 0:
            self.btn19.setEnabled(True)

        if check1 == 1:
            i1 += 1
            if rab == 1:
                if i1 == 1000:
                    moneyeffect -= 1
                    check1 = 0
                    self.btn16.setEnabled(True)
                    self.rab1()

            if rab == 2:
                if i1 == 1000:
                    moneyeffect -= 1
                    check1 = 0
                    self.btn16.setEnabled(True)
                    self.rab2()

            if rab == 3:
                if i1 == 1000:
                    moneyeffect -= 1
                    check1 = 0
                    self.btn16.setEnabled(True)
                    self.rab3()

            if rab == 4:
                if i1 == 1000:
                    moneyeffect -= 1
                    check1 = 0
                    self.btn16.setEnabled(True)
                    self.rab4()


            if rab == 5:
                if i1 == 1000:
                    moneyeffect -= 1
                    check1 = 0
                    self.btn16.setEnabled(True)
                    self.rab5()


            if rab == 6:
                if i1 == 1000:
                    moneyeffect -= 1
                    check1 = 0
                    self.btn16.setEnabled(True)
                    self.rab6()

        if check2 == 1:
            i2 += 1
            if rab == 1:
                if i2 == 1000:
                    moneyeffect -= 4
                    check2 = 0
                    self.btn17.setEnabled(True)
                    self.rab1()

            if rab == 2:
                if i2 == 1000:
                    moneyeffect -= 4
                    check2 = 0
                    self.btn17.setEnabled(True)
                    self.rab2()

            if rab == 3:
                if i2 == 1000:
                    moneyeffect -= 4
                    check2 = 0
                    self.btn17.setEnabled(True)
                    self.rab3()

            if rab == 4:
                if i2 == 1000:
                    moneyeffect -= 4
                    check2 = 0
                    self.btn17.setEnabled(True)
                    self.rab4()

            if rab == 5:
                if i2 == 1000:
                    moneyeffect -= 4
                    check2 = 0
                    self.btn17.setEnabled(True)
                    self.rab5()

            if rab == 6:
                if i2 == 1000:
                    moneyeffect -= 4
                    check2 = 0
                    self.btn17.setEnabled(True)
                    self.rab6()

        if check3 == 1:
            i3 += 1
            if rab == 1:
                if i3 == 1000:
                    moneyeffect -= 8
                    check3 = 0
                    self.btn18.setEnabled(True)
                    self.rab1()

            if rab == 2:
                if i3 == 1000:
                    moneyeffect -= 8
                    check3 = 0
                    self.btn18.setEnabled(True)
                    self.rab2()

            if rab == 3:
                if i3 == 1000:
                    moneyeffect -= 8
                    check3 = 0
                    self.btn18.setEnabled(True)
                    self.rab3()

            if rab == 4:
                if i3 == 1000:
                    moneyeffect -= 8
                    check3 = 0
                    self.btn18.setEnabled(True)
                    self.rab4()

            if rab == 5:
                if i3 == 1000:
                    moneyeffect -= 8
                    check3 = 0
                    self.btn18.setEnabled(True)
                    self.rab5()

            if rab == 6:
                if i3 == 1000:
                    moneyeffect -= 8
                    check3 = 0
                    self.btn18.setEnabled(True)
                    self.rab6()

        if check4 == 1:
            i4 += 1
            if rab == 1:
                if i4 == 1000:
                    moneyeffect -= 16
                    check4 = 0
                    self.btn19.setEnabled(True)
                    self.rab1()

            if rab == 2:
                if i4 == 1000:
                    moneyeffect -= 16
                    check4 = 0
                    self.btn19.setEnabled(True)
                    self.rab2()

            if rab == 3:
                if i4 == 1000:
                    moneyeffect -= 16
                    check4 = 0
                    self.btn19.setEnabled(True)
                    self.rab3()

            if rab == 4:
                if i4 == 1000:
                    moneyeffect -= 16
                    check4 = 0
                    self.btn19.setEnabled(True)
                    self.rab4()

            if rab == 5:
                if i4 == 1000:
                    moneyeffect -= 16
                    check4 = 0
                    self.btn19.setEnabled(True)
                    self.rab5()

            if rab == 6:
                if i4 == 1000:
                    moneyeffect -= 16
                    check4 = 0
                    self.btn19.setEnabled(True)
                    self.rab6()

    def buy1(self):
        global countmoney
        if countmoney >= 2000:
            countmoney -= 2000
            self.lb2.setText(f"Рублей: {countmoney}")
            self.btn10.setEnabled(False)
            self.btn3.setEnabled(True)

    def buy2(self):
        global countmoney
        if countmoney >= 25000:
            countmoney -= 25000
            self.lb2.setText(f"Рублей: {countmoney}")
            self.btn11.setEnabled(False)
            self.btn4.setEnabled(True)

    def buy3(self):
        global countmoney
        if countmoney >= 25000:
            countmoney -= 25000
            self.lb2.setText(f"Рублей: {countmoney}")
            self.btn12.setEnabled(False)
            self.btn5.setEnabled(True)

    def buy4(self):
        global countmoney
        if countmoney >= 500000:
            countmoney -= 500000
            self.lb2.setText(f"Рублей: {countmoney}")
            self.btn13.setEnabled(False)
            self.btn6.setEnabled(True)

    def buy5(self):
        global countmoney
        if countmoney >= 5000000:
            countmoney -= 5000000
            self.lb2.setText(f"Рублей: {countmoney}")
            self.btn14.setEnabled(False)
            self.btn7.setEnabled(True)

    def buy6(self):
        global countmoney
        if countmoney >= 25000000:
            countmoney -= 25000000
            self.lb2.setText(f"Рублей: {countmoney}")
            self.btn15.setEnabled(False)
            self.btn8.setEnabled(True)

    def rab1(self):
        global moneyeffect, rab
        self.lb1.setPixmap(QtGui.QPixmap("photo/бутылка.jpeg"))
        self.moneyadd = 1
        rab = 1
        self.moneyadd += moneyeffect
        self.btn1.setText("Собрать бутылку")

    def rab2(self):
        global moneyeffect, rab
        self.lb1.setPixmap(QtGui.QPixmap("photo/курьер.png"))
        self.moneyadd = 2
        rab = 2
        self.moneyadd += moneyeffect
        self.btn1.setText("Довести посылку")

    def rab3(self):
        global moneyeffect, rab
        self.lb1.setPixmap(QtGui.QPixmap("photo/Уборщик.jpg"))
        self.moneyadd = 5
        rab =3
        self.moneyadd += moneyeffect
        self.btn1.setText("Убрать мусор")

    def rab4(self):
        global moneyeffect, rab
        self.lb1.setPixmap(QtGui.QPixmap("photo/Строитель.jpg"))
        self.moneyadd = 10
        rab = 4
        self.moneyadd += moneyeffect
        self.btn1.setText("Положить кирпич")

    def rab5(self):
        global moneyeffect, rab
        self.lb1.setPixmap(QtGui.QPixmap("photo/Продавец.jpg"))
        self.moneyadd = 50
        rab = 5
        self.moneyadd += moneyeffect
        self.btn1.setText("Продать")

    def rab6(self):
        global moneyeffect, rab
        self.lb1.setPixmap(QtGui.QPixmap("photo/Бухгалтер.jpg"))
        self.moneyadd = 100
        rab = 6
        self.moneyadd += moneyeffect
        self.btn1.setText("Сделать отчёт")

    def rab7(self):
        self.w3 = NewWork()
        self.w3.show()
        self.hide()



class NewWork(QMainWindow):
    def __init__(self):
        global countmoney
        super().__init__()
        uic.loadUi('design3.ui', self)
        self.pb1.clicked.connect(self.click)
        self.pb3.clicked.connect(self.click2)
        self.pb2.clicked.connect(self.click3)
        self.spis = {1: 'Шаурма', 2: 'Хот-Дог', 3: 'Яичница', 4: "Пицца", 5: "Бургер", 6: "Сосиска в тесте", 7: "Чебурек"}
        self.data = list(self.spis.keys())
        self.key = self.data[randrange(len(self.data))]
        self.lb1.setText(self.spis[self.key])
        self.msg = QMessageBox()
        self.countzac = 0
        self.lb12.setText(f"Денег: {countmoney}")

    def click3(self):
        self.w2 = MyWindow()
        self.w2.show()
        self.hide()

    def click2(self):
        self.key = self.data[randrange(len(self.data))]
        self.lb1.setText(self.spis[self.key])

    def click(self):
        global countmoney
        if self.lb1.text() == 'Шаурма':
            if self.cb1.checkState() == 2 and self.cb2.checkState() == 2 and self.cb3.checkState() == 2 and self.cb4.checkState() == 2 and self.cb5.checkState() == 0 and self.cb6.checkState() == 0 and self.cb7.checkState() == 0:
                self.countzac += 1
                countmoney += 120
                self.lb12.setText(f"Денег: {countmoney}")
                self.lb2.setText(f"Собрано заказов: {self.countzac}")
                self.msg.setText("Ты сделал шаурму")
                self.returnValue = self.msg.exec()
                self.key = self.data[randrange(len(self.data))]
                self.lb1.setText(self.spis[self.key])
                self.cb1.setCheckState(0)
                self.cb2.setCheckState(0)
                self.cb3.setCheckState(0)
                self.cb4.setCheckState(0)
                self.cb5.setCheckState(0)
                self.cb6.setCheckState(0)
                self.cb7.setCheckState(0)

            else:
                self.msg.setText("Что это такое? Переделай!")
                self.returnValue = self.msg.exec()

        elif self.lb1.text() == 'Хот-Дог':
            if self.cb1.checkState() == 0 and self.cb2.checkState() == 2 and self.cb3.checkState() == 2 and self.cb4.checkState() == 2 and self.cb5.checkState() == 2 and self.cb6.checkState() == 0 and self.cb7.checkState() == 0:
                self.msg.setText("Ты сделал хот-дог")
                self.countzac += 1
                countmoney += 70
                self.lb12.setText(f"Денег: {countmoney}")
                self.lb2.setText(f"Собрано заказов: {self.countzac}")
                self.returnValue = self.msg.exec()
                self.key = self.data[randrange(len(self.data))]
                self.lb1.setText(self.spis[self.key])
                self.cb1.setCheckState(0)
                self.cb2.setCheckState(0)
                self.cb3.setCheckState(0)
                self.cb4.setCheckState(0)
                self.cb5.setCheckState(0)
                self.cb6.setCheckState(0)
                self.cb7.setCheckState(0)

            else:
                self.msg.setText("Что это такое? Переделай!")
                self.returnValue = self.msg.exec()

        elif self.lb1.text() == 'Яичница':
            if self.cb1.checkState() == 0 and self.cb2.checkState() == 0 and self.cb3.checkState() == 0 and self.cb4.checkState() == 0 and self.cb5.checkState() == 2 and self.cb6.checkState() == 2 and self.cb7.checkState() == 0:
                self.msg.setText("Ты сделал яичницу")
                self.countzac += 1
                countmoney += 50
                self.lb12.setText(f"Денег: {countmoney}")
                self.lb2.setText(f"Собрано заказов: {self.countzac}")
                self.returnValue = self.msg.exec()
                self.key = self.data[randrange(len(self.data))]
                self.lb1.setText(self.spis[self.key])
                self.cb1.setCheckState(0)
                self.cb2.setCheckState(0)
                self.cb3.setCheckState(0)
                self.cb4.setCheckState(0)
                self.cb5.setCheckState(0)
                self.cb6.setCheckState(0)
                self.cb7.setCheckState(0)

            else:
                self.msg.setText("Что это такое? Переделай!")
                self.returnValue = self.msg.exec()

        elif self.lb1.text() == 'Пицца':
            if self.cb1.checkState() == 2 and self.cb2.checkState() == 2 and self.cb3.checkState() == 2 and self.cb4.checkState() == 2 and self.cb5.checkState() == 0 and self.cb6.checkState() == 0 and self.cb7.checkState() == 2:
                self.msg.setText("Ты сделал пиццу")
                self.countzac += 1
                countmoney += 250
                self.lb12.setText(f"Денег: {countmoney}")
                self.lb2.setText(f"Собрано заказов: {self.countzac}")
                self.returnValue = self.msg.exec()
                self.key = self.data[randrange(len(self.data))]
                self.lb1.setText(self.spis[self.key])
                self.cb1.setCheckState(0)
                self.cb2.setCheckState(0)
                self.cb3.setCheckState(0)
                self.cb4.setCheckState(0)
                self.cb5.setCheckState(0)
                self.cb6.setCheckState(0)
                self.cb7.setCheckState(0)

            else:
                self.msg.setText("Что это такое? Переделай!")
                self.returnValue = self.msg.exec()
        elif self.lb1.text() == 'Бургер':
            if self.cb1.checkState() == 2 and self.cb2.checkState() == 2 and self.cb3.checkState() == 2 and self.cb4.checkState() == 0 and self.cb5.checkState() == 0 and self.cb6.checkState() == 0 and self.cb7.checkState() == 2:
                self.msg.setText("Ты сделал бургер")
                self.countzac += 1
                countmoney += 80
                self.lb12.setText(f"Денег: {countmoney}")
                self.lb2.setText(f"Собрано заказов: {self.countzac}")
                self.returnValue = self.msg.exec()
                self.key = self.data[randrange(len(self.data))]
                self.lb1.setText(self.spis[self.key])
                self.cb1.setCheckState(0)
                self.cb2.setCheckState(0)
                self.cb3.setCheckState(0)
                self.cb4.setCheckState(0)
                self.cb5.setCheckState(0)
                self.cb6.setCheckState(0)
                self.cb7.setCheckState(0)

            else:
                self.msg.setText("Что это такое? Переделай!")
                self.returnValue = self.msg.exec()
        elif self.lb1.text() == 'Сосиска в тесте':
            if self.cb1.checkState() == 0 and self.cb2.checkState() == 2 and self.cb3.checkState() == 0 and self.cb4.checkState() == 0 and self.cb5.checkState() == 2 and self.cb6.checkState() == 0 and self.cb7.checkState() == 0:
                self.msg.setText("Ты сделал сосиску в тесте")
                self.countzac += 1
                countmoney += 40
                self.lb12.setText(f"Денег: {countmoney}")
                self.lb2.setText(f"Собрано заказов: {self.countzac}")
                self.returnValue = self.msg.exec()
                self.key = self.data[randrange(len(self.data))]
                self.lb1.setText(self.spis[self.key])
                self.cb1.setCheckState(0)
                self.cb2.setCheckState(0)
                self.cb3.setCheckState(0)
                self.cb4.setCheckState(0)
                self.cb5.setCheckState(0)
                self.cb6.setCheckState(0)
                self.cb7.setCheckState(0)

            else:
                self.msg.setText("Что это такое? Переделай!")
                self.returnValue = self.msg.exec()
        elif self.lb1.text() == 'Чебурек':
            if self.cb1.checkState() == 2 and self.cb2.checkState() == 2 and self.cb3.checkState() == 0 and self.cb4.checkState() == 0 and self.cb5.checkState() == 0 and self.cb6.checkState() == 0 and self.cb7.checkState() == 0:
                self.msg.setText("Ты сделал чебурек")
                self.countzac += 1
                countmoney += 60
                self.lb12.setText(f"Денег: {countmoney}")
                self.lb2.setText(f"Собрано заказов: {self.countzac}")
                self.returnValue = self.msg.exec()
                self.key = self.data[randrange(len(self.data))]
                self.lb1.setText(self.spis[self.key])
                self.cb1.setCheckState(0)
                self.cb2.setCheckState(0)
                self.cb3.setCheckState(0)
                self.cb4.setCheckState(0)
                self.cb5.setCheckState(0)
                self.cb6.setCheckState(0)
                self.cb7.setCheckState(0)

            else:
                self.msg.setText("Что это такое? Переделай!")
                self.returnValue = self.msg.exec()

def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("Oбнаружена ошибка !:", tb)

if __name__ == '__main__':
    sys.excepthook = excepthook
    app = QApplication(sys.argv)
    ex = nach()
    ex.show()
    sys.exit(app.exec_())