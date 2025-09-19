def Escola():
    while True:
        print("Bem vindo a Escola!!!")
        papel = int(input("Digite 1 para Professor e 2 para Aluno: "))

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
            
            media = input("Você deseja ver sua média?")
            if media == "sim" and "s" and "Sim":
                not1 = int(input("Digite sua primeira nota"))
                not2 = int(input("Digite sua primeira nota"))
                not3 = int(input("Digite sua primeira nota"))
                not4 = int(input("Digite sua primeira nota"))
                
                media_final = (not1 + not2 + not3 + not4)/4

                print(f"Sua nota final é {media_final}")
                break
            else:
                print("ok!")
                break
        elif papel != 1 and 2:
            print("Escolha uma opção valida!")
            return Escola()
Escola()

git config --global user.email "jlucasgames909@gmail.com"
git config --global user.name "meloozwx"