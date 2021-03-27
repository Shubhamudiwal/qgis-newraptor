from qgis.PyQt.QtWidgets import *
from .impact_table_dialoge import Ui_DlgImpacts


class DlgTable(QDialog,Ui_DlgImpacts):
    def __init__(self):
        super(DlgTable,self).__init__()
        self.setupUi(self)

        self.tblImpacts.setColumnWidth(1,200)
