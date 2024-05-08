import unittest
 # exemplo de teste unitario dentro do NSA, já dentro da conta - usuario quer modificar a sua senha 
class Estudante:
    def __init__(self, useremail, password): # pode conter código de inicialização para ser importado
        self.useremail = useremail # self -> se refere a própria instância de uma classe
        self.password = password

    def change_password(self, new_password):
        self.password = new_password

class TestEstudante(unittest.TestCase):
    def test_change_password(self):
        # Cria um aluno de exemplo
        estudante = Estudante("mariarodrigues@etec.sp.gov.br", "senha123")

        # Verifica se a senha original está correta
        self.assertEqual(estudante.password, "senha123")

        # Muda a senha
        estudante.change_password("novaSenha456")

        # Verifica se a senha foi modificada corretamente
        self.assertEqual(estudante.password, "novaSenha456")

if __name__ == '__main__':
    unittest.main()
