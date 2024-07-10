from datetime import datetime

#comentario Hector

def verificar_idade():
    try:
        ano_atual = datetime.now().year
        ano_nascimento = int(input("Por favor, insira o seu ano de nascimento: "))
        idade = ano_atual - ano_nascimento

        if idade >= 18:
            print(f"Você tem {idade} anos. Você é maior de idade.")
        else:
            print(f"Você tem {idade} anos. Você é menor de idade.")
    except ValueError:
        print("Por favor, insira um ano válido.")

if __name__ == "__main__":
    verificar_idade()
