🪨📄✂️ Jogo Pedra, Papel e Tesoura
Bem-vindo ao repositório do Jogo Pedra, Papel e Tesoura! Este projeto simples em Python permite que você jogue contra o computador, demonstrando lógica básica, entrada/saída de usuário e testes unitários.

🚀 Como Clonar o Repositório
Para obter uma cópia local deste projeto, utilize o seguinte comando Git no seu terminal:

git clone https://github.com/Sidney00131/Jogo_pedra_papel_tesoura
cd Jogo_pedra_papel_tesoura

CASO DE USO
![Diagrama de classe](Diagramas/CasoUso.png)


DIAGRAMA DE CLASSE
![Diagrama de classe](Diagramas/Dclasse.png)

🎮 Como o Código do Jogo Funciona
O coração do jogo está no arquivo src/app.py (assumindo que a lógica principal do jogo está lá). Ele implementa as regras clássicas do Pedra, Papel e Tesoura.

Estrutura Principal:

opcoes: Uma lista que define as escolhas válidas do jogo ("pedra", "papel", "tesoura").

Loop Principal: O jogo roda dentro de um loop while True que continua até o jogador decidir sair.

Entrada do Jogador: Solicita ao jogador que digite sua escolha. A entrada é convertida para minúsculas para facilitar a comparação.

Escolha do Computador: Utiliza o módulo random do Python para que o computador faça uma escolha aleatória entre as opções disponíveis.

Validação da Entrada: Verifica se a escolha do jogador é uma das opções válidas. Se não for, pede para o jogador tentar novamente.

Determinação do Vencedor: Esta é a lógica central do jogo. Compara a escolha do jogador com a escolha do computador e determina se é um empate, vitória do jogador ou vitória do computador, seguindo as regras:

Pedra vence Tesoura

Tesoura vence Papel

Papel vence Pedra

Saída: Imprime as escolhas de ambos e o resultado da rodada.

✅ Como o Teste Pytest Funciona
Para garantir que a lógica de determinação do vencedor esteja correta, o projeto inclui testes unitários usando o framework pytest. O arquivo de teste tests/test_app.py verifica a função que decide quem vence.