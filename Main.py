# Codigo_Nivel_Atendimento_SAC_Melhores_Compras.py
from sys import excepthook


def classificar_satisfacao(nota):
    """
    Receber nota (int/float) entre 0 e 100 e retorna string classificando
    - 'Qualidade' para nota > 90
    - 'Neutro' para 70 <= nota <= 89
    - 'Insatisfação' para nota < 70
    Valida entrada e lança ValueError se inválida
    """

    try:
        valor = float(nota)
    except Exception:
        raise ValueError("Nota inválida: informe um número entre 0 e 100.")

    if valor >= 90:
        return "Qualidade"
    elif 70 <= valor <= 89:
        return "Neutro"
    else:
        return "Insatisfatorio"

def main():
      rm = input(" Insira seu RM: ")
      idade = input("Insira sua idade: ")

      if int(idade) >= 18:
          print("Sua Participação foi autorizada, aluno de RM {}!".format(rm))
          print("Mais informações serão enviadas para seu e-mail cadastrado!")

          entrada = input("Informe a nota de satisfação (0-100): ").strip()
          try:
              classificacao = classificar_satisfacao(entrada)
              print(f"Classificação: {classificacao}")
          except ValueError as e:
                print(f"Erro: {e}")

      else:
          print("Infelizmente, a participação não foi autorizada, aluno de RM{}.".format(rm))

if __name__ == "__main__":

        main()
