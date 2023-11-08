import random
import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.wyswietldateicene)
        self.show()

    def wyswietldateicene(self):
        cena = 0
        dni = 0
        lekarz = ''
        if self.ui.Internista.isChecked()==True:
            lekarz = 'Internista'
        if self.ui.Pediatra.isChecked()==True:
            lekarz = 'Pediatra'
        if self.ui.Dermatolog.isChecked()==True:
            lekarz = 'Dermatolog'
        if self.ui.checkBoxPrivate.isChecked()==True:
            cena = 200
            dni = random.randrange(0,14)
        else:
            cena = 0
            dni = random.randrange(0,1000)
        self.ui.result.setText("Pomyślnie zarezerowowano wizytę u lekarza: "+ lekarz +". Termin wizyty przypada za: "+str(dni)+" dni.\n Koszt wizyty: "+ str(cena)+" zł")

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())