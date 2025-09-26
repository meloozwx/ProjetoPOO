import random

def jokenpo():
    
    while True:
        print("\n--- JOKENPO ---")
        print("1. Pedra")
        print("2. Papel") 
        print("3. Tesoura")
        
        try:

            escolha_jogador = int(input("Escolha uma opção (1-3): "))
            
            if escolha_jogador < 1 or escolha_jogador > 3:
                print("Opção inválida!")
                return
            
            escolha_computador = random.randint(1, 3)
            
            opcoes = {1: "Pedra", 2: "Papel", 3: "Tesoura"}
            
            jogador = opcoes[escolha_jogador]
            computador = opcoes[escolha_computador]
            
            print(f"\nVocê escolheu: {jogador}")
            print(f"Computador escolheu: {computador}")
            
            if escolha_jogador == escolha_computador:
                print("Empate!")
                desejo = input("Deseja continuar?"
                "1 para sim"
                "2 para não")
                if desejo == 1:
                    jokenpo()
                elif desejo == 2:
                    break
            elif (escolha_jogador == 1 and escolha_computador == 3) or \
                (escolha_jogador == 2 and escolha_computador == 1) or \
                (escolha_jogador == 3 and escolha_computador == 2):
                print("Você venceu!")
                desejo = input("Deseja continuar?"
                "1 para sim"
                "2 para não")
                if desejo == 1:
                    jokenpo()
                elif desejo == 2:
                    break
            else:
                print("Computador venceu!")
                desejo = input("Deseja continuar?"
                "1 para sim"
                "2 para não")
                if desejo == 1:
                    jokenpo()
                elif desejo == 2:
                    break
                
        except ValueError:
            print("Por favor, digite um número válido.")