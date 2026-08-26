# Sistema de Saúde e Bem-Estar 

## Descrição do Projeto
Este é um sistema interativo via terminal (CLI) desenvolvido em Python que oferece ferramentas simples para o monitoramento da saúde e bem-estar. O programa apresenta um menu onde o usuário pode acessar três funcionalidades principais:
1. **Cálculo de IMC (Índice de Massa Corporal):** Calcula o IMC com base no peso e altura, retornando também a classificação do estado nutricional.
2. **Recomendação de Água Diária:** Estima a quantidade ideal de ingestão de água por dia com base no peso corporal (utilizando a métrica de 35ml por kg).
3. **Frequência Cardíaca Máxima:** Calcula o limite seguro de batimentos por minuto para atividades físicas, com base na idade do usuário.

---

## Relatório de Bugs Encontrados

Durante a auditoria de código, foram identificados e corrigidos os seguintes problemas estruturais e lógicos:

| Local do Bug (Função) | Comportamento Incorreto Observado | Solução Aplicada |
|---|---|---|
| `calcular_imc` | A fórmula multiplicava a altura por 2 (`altura * 2`), gerando um cálculo incorreto de IMC. | Alterado o operador para potenciação (`altura ** 2`), elevando a altura ao quadrado. |
| `classificar_imc` | Condições sobrepostas e buracos lógicos para valores decimais (ex: 24.95 não era classificado e retornava `None`). | Substituição das faixas rígidas por validações contínuas (`< 18.5`, `< 25.0`, etc.) e uso do `else` no final. |
| `calcular_agua_diaria` | A fórmula dividia o peso por 35 (`peso / 35`), subestimando gravemente a meta hídrica. | A fórmula foi corrigida para multiplicar o peso por 35 e, em seguida, dividida por 1000 para converter o resultado para Litros. |
| `calcular_frequencia_cardiaca_maxima` | A fórmula somava a idade a 220 (`220 + idade`) em vez de subtrair. | O operador de adição foi trocado pelo de subtração (`220 - idade`). |
| `menu` | A captura do menu retornava uma string bruta, ou forçava o tipo inteiro, o que poderia causar um travamento (`ValueError`) caso o usuário digitasse uma letra. | O input foi mantido como `string` para maior segurança e tratou-se com `.strip()` para evitar erros com espaços em branco. |
| `main` (if/elif do menu) | O programa tentava comparar a opção digitada (string) com números inteiros (`if opcao == 1:`), o que sempre resultava em falso e ativava a opção inválida. | As comparações foram alteradas para comparar a entrada com strings (ex: `if opcao == '1':`). |
| `main` (Loop `while`) | O programa entrava em loop infinito ao escolher a opção "Sair" (falta de `break`) ou encerrava precocemente as opções 1, 2 e 3. | Os `breaks` foram removidos das opções de cálculo e um único `break` foi posicionado exclusivamente na opção '4' (Sair). |

---

## Como Executar

Para rodar este projeto, você precisará ter o [Python](https://www.python.org/downloads/) instalado na sua máquina (versão 3.6 ou superior).

1. Clone o repositório ou baixe o arquivo `calculadora_saude.py` para o seu computador.
2. Abra o terminal (Prompt de Comando, PowerShell ou Terminal do Linux/Mac).
3. Navegue até a pasta onde o arquivo está salvo usando o comando `cd`. Exemplo:
   ```bash
   cd caminho/para/a/pasta
4. Execute o script com o seguinte comando:
  ```bash
    python calculadora_saude.py

Autor:
Kaio Moreira - 32510906
Erick Mello - 326211590
Icaro Ferreira - 325111358

Projeto desenvolvido como atividade acadêmica da disciplina de Garantia da Qualidade de Software, sob orientação do professor Daniel Paiva.
