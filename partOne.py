from Lazer import jokenpo
def Escola():
        while True:
            print("Bem vindo a Escola!!!")
            papel = int(input("Digite 1 para Professor, 2 para Aluno e 3 para Sair: "))

            if papel == 1:
                materia = input("Qual sua máteria?")
                nome = input("Qual seu nome?")
                idade = input("Qual sua idade?")

                aura = input("Qual conteudo você dará hoje? ")
                
                print(f"Você vai dar o conteudo {aura} na semana")

                break
            elif papel == 2:
                nome = input("Qual seu nome?")
                idade = input("Qual sua idade?")
                
                ocupacao = int(input("O que você deseja fazer?\n"
                "1 para media\n"
                "2 para lazer\n"
                "3 para sair: "))

                if ocupacao == 1:
                    not1 = int(input("Digite sua primeira nota"))
                    not2 = int(input("Digite sua segunda nota"))
                    not3 = int(input("Digite sua terceira nota"))
                    not4 = int(input("Digite sua quarta nota"))
                    
                    media_final = (not1 + not2 + not3 + not4)/4

                    print(f"Sua nota final é {media_final}")
                    return
                elif ocupacao == 2:
                        jokenpo()
                elif ocupacao == 3:
                    print("ok!")
            elif papel == 3:
                break
            elif papel not in [1, 2, 3]:
                print("Escolha uma opção válida!")
                return
Escola()
