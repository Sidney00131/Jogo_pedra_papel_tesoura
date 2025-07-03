import random

def determinar_vencedor(escolha_jogador, escolha_computador):
    """
    Determina o vencedor de uma rodada de Pedra, Papel, Tesoura.

    Parâmetros:
    escolha_jogador (str): A escolha do jogador ("pedra", "papel" ou "tesoura").
    escolha_computador (str): A escolha do computador ("pedra", "papel" ou "tesoura").

    Retorna:
    str: "Empate", "Jogador" se o jogador vencer, ou "Computador" se o computador vencer.
    """
    if escolha_jogador == escolha_computador:
        return "Empate"
    elif (escolha_jogador == "pedra" and escolha_computador == "tesoura") or \
         (escolha_jogador == "papel" and escolha_computador == "pedra") or \
         (escolha_jogador == "tesoura" and escolha_computador == "papel"):
        return "Jogador"
    else:
        return "Computador"

def jogar_pedra_papel_tesoura():
    """
    Função principal para jogar Pedra, Papel, Tesoura.
    """
    opcoes = ["pedra", "papel", "tesoura"]
    
    print("Bem-vindo ao Pedra, Papel, Tesoura!")
    print("Regras: Pedra > Tesoura, Tesoura > Papel, Papel > Pedra")

    while True:
        # Pede a escolha do jogador
        escolha_jogador = input("\nEscolha (pedra, papel, tesoura) ou 'sair' para encerrar: ").lower()

        # Verifica se o jogador quer sair
        if escolha_jogador == 'sair':
            print("Obrigado por jogar! Até a próxima.")
            break

        # Valida a escolha do jogador
        if escolha_jogador not in opcoes:
            print("Escolha inválida. Por favor, digite 'pedra', 'papel' ou 'tesoura'.")
            continue # Volta para o início do loop

        # Escolha do computador
        escolha_computador = random.choice(opcoes)

        print(f"\nVocê escolheu: {escolha_jogador.capitalize()}")
        print(f"O computador escolheu: {escolha_computador.capitalize()}")

        # Chama a nova função determinar_vencedor
        resultado = determinar_vencedor(escolha_jogador, escolha_computador)
        
        # Imprime o resultado
        if resultado == "Empate":
            print("Empate!")
        elif resultado == "Jogador":
            print("Você Venceu!")
        else: # resultado == "Computador"
            print("O Computador Venceu!")

# Chama a função para iniciar o jogo
if __name__ == "__main__":
    jogar_pedra_papel_tesoura()