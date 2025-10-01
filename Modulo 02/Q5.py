class DispositivoEletronico:
    def ligar(self):
        print("Ligando...")

    def desligar(self):
        print("Desligando..")

class Computador(DispositivoEletronico):
    def instalar_software(self):
        print("Instalando software... ")

class Notebook(Computador):
    def verificar_bateria(self):
        print("Bateria em 80%")



n = Notebook()
n.ligar()
n.instalar_software()
n.verificar_bateria()