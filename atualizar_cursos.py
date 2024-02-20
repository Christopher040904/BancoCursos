import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem,QLabel,QLineEdit,QVBoxLayout, QPushButton
import mysql.connector as mycon

cx = mycon.connect(
    host="127.0.0.1",
    port="6556",
    user="root",
    password="123@senac",
    database="Senac"
)
cursor = cx.cursor()

class AtualizarCursos(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100,100,500,400)
        self.setWindowTitle("Cursos cadastrados")

        labelId = QLabel("Id do Curso:")
        self.editId = QLineEdit()
        
        labelCurso = QLabel("Curso:")
        self.editCurso = QLineEdit()

        labelHorario = QLabel("Carga Horaria:")
        self.editHorario = QLineEdit()


        psbCadastro = QPushButton("Cadastrar")

        layout = QVBoxLayout()
        
        layout.addWidget(labelId)
        layout.addWidget(self.editId) 
        
        layout.addWidget(labelCurso)
        layout.addWidget(self.editCurso)

        layout.addWidget(labelHorario)
        layout.addWidget(self.editHorario)

        layout.addWidget(psbCadastro)
        psbCadastro.clicked.connect(self.upCursos)

        tbcursos = QTableWidget(self)
        tbcursos.setColumnCount(3)
        tbcursos.setRowCount(10)

        headerLine=["Id","Curso","Carga Horaria"]

        tbcursos.setHorizontalHeaderLabels(headerLine)
        cursor.execute("select * from cursos")
        lintb = 0
        for linha in cursor:
            tbcursos.setItem(lintb,0,QTableWidgetItem(str(linha[0])))
            tbcursos.setItem(lintb,1,QTableWidgetItem(linha[1]))
            tbcursos.setItem(lintb,2,QTableWidgetItem(linha[2]))
            lintb+=1
  
        layout.addWidget(tbcursos)
        self.setLayout(layout)
    
    def upCursos(self):
        if(self.editId.text()==""):
            print("Não é possível atualizar sem o Id do Curso")
        
        elif(self.editId.text()=="" and self.editCurso.text()=="" and self.editHorario.text()==""):
            print("Não é possível atualizar se não houver dados")
       
        elif(self.editId.text()!="" and self.editCurso.text()=="" and self.editHorario.text()==""):
            cursor.execute("update cursos set cursos_id=%s where cursos_id=%s",
                           (self.editId.text(),self.editId.text()))

        elif(self.editId.text()=="" and self.editCurso.text()!="" and self.editHorario.text()==""):
            cursor.execute("update cursos set nome_curso=%s where cursos_id=%s",
                           (self.editCurso.text(),self.editId.text()))            
        
        elif(self.editId.text()=="" and self.editCurso.text()=="" and self.editHorario.text()!=""):
            cursor.execute("update cursos set carga_horaria=%s where cursos_id=%s",
                           (self.editHorario.text(),self.editId.text()))            
        
        else:
            cursor.execute("update cursos set cursos_id=%s,nome_curso=%s,carga_Horaria=%s where cursos_id=%s",
                           (self.editId.text(),self.editCurso.text(),self.editHorario.text(),self.editId.text()))

        cx.commit()
        print("Todas as modificações foram realizadas")

if __name__=="__main__":
    app = QApplication(sys.argv)
    tela = AtualizarCursos()
    tela.show()
    sys.exit(app.exec_())        