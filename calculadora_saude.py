# calculadora_saude.py

def calcular_imc(peso, altura):
    # Bug 1 resolvido: Usando potenciação
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    # Bug 2 resolvido: Usando < para capturar os decimais e fechando com else
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25.0:
        return "Peso normal"
    elif imc < 30.0:
        return "Sobrepeso"
    else:
        return "Obesidade"

def calcular_agua_diaria(peso):
    # Bug 3 resolvido: Multiplicação e conversão para litros
    litros = (peso * 35) / 1000
    return litros

def calcular_frequencia_cardiaca_maxima(idade):
    # Bug 4 resolvido: Subtração correta
    fc_max = 220 - idade
    return fc_max

def menu():
    print("\n" + "="*30)
    print("  SISTEMA DE SAÚDE E BEM-ESTAR  ")
    print("="*30)
    print("1. Calcular IMC")
    print("2. Calcular Recomendação de Água")
    print("3. Calcular Frequência Cardíaca Máxima")
    print("4. Sair")
    
    # Bug 5 resolvido: Mantendo como string e limpando espaços com .strip()
    opcao = input("Escolha uma opção (1-4): ").strip()
    return opcao

def main():
    while True:
        opcao = menu()
        
        # Bug 6 resolvido: Comparações ajustadas para string ('1', '2', etc.)
        if opcao == '1':
            peso = float(input("Digite seu peso (kg): "))
            altura = float(input("Digite sua altura (m): "))
            imc = calcular_imc(peso, altura)
            print(f"Seu IMC é: {imc:.2f}")
            print(f"Classificação: {classificar_imc(imc)}")
            
        elif opcao == '2':
            peso = float(input("Digite seu peso (kg): "))
            qtd_agua = calcular_agua_diaria(peso)
            print(f"Sua meta diária de água é: {qtd_agua:.2f} Litros")
            
        elif opcao == '3':
            idade = int(input("Digite sua idade: "))
            fc = calcular_frequencia_cardiaca_maxima(idade)
            print(f"Sua Frequência Cardíaca Máxima estimada é: {fc} bpm")
            
            
        elif opcao == '4':
            print("Encerrando o sistema...")
            print("Obrigado por usar nosso sistema!")
            # Bug 7 resolvido: O break fica APENAS aqui na opção de sair
            break 
            
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
