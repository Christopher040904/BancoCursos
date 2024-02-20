import sys
import mysql.connector as mc
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QLineEdit,QVBoxLayout, QPushButton

con= mc.connect(
    host="127.0.0.1",
    port="6556",
    user="root",
    password="123@senac",
    database="Senac"
)

cursor = con.cursor()


class CadCurso(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(30,40,600,250)
        self.setWindowTitle("Cadastro de Cursos")

        labelCurso = QLabel("Nome do Curso:")
        self.editCurso = QLineEdit()

        labelHorario = QLabel("Carga Horaria:")
        self.editHorario = QLineEdit()

        psbCadastro = QPushButton("Cadastrar")

        self.labelMsg = QLabel("Rua Coronel Luís Americano, 130 tatuapé, São Paulo")

        layout = QVBoxLayout()
        layout.addWidget(labelCurso)
        layout.addWidget(self.editCurso)

        layout.addWidget(labelHorario)
        layout.addWidget(self.editHorario)

        layout.addWidget(psbCadastro)
        psbCadastro.clicked.connect(self.cadCurso)

        layout.addWidget(self.labelMsg)

        self.setLayout(layout)

    def cadCurso(self):
        cursor.execute("insert into cursos(nome_curso,carga_horaria)values(%s,%s)",
                       (self.editCurso.text(),self.editHorario.text()))
        con.commit()
        self.labelMsg.setText("Curso cadastrado")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = CadCurso()
    tela.show()
    sys.exit(app.exec_())        