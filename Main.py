
import oracledb

# Codigo_Nivel_Atendimento_SAC_Melhores_Compras.py
from sys import excepthook, exception


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


# Função para salvar no Oracle

def salvar_no_oracle(rm, idade, nota, classificacao):
    """
    
    Salva os dados de avaliação no banco de dados Oracle.
    Ajuste as credenciais de conexão (user, password, dsn).
    """

    try:
        conn = oracledb.connect(
            user="SEU_USUARIO",          # TROQUE AQUI
            password="SUA_SENHA",        # TROQUE AQUI
            dsn="localhost:1521/XEPDB1"  # TROQUE AQUI (host:porta/ServiceName
        )
        cursor = conn.cursor()

        # Exemplo: inserindo em SGV_SAC_CHAMADO
        # Ajuste os campos conforme sua modelagem
        cursor.execute("""
            INSERT INTO SGV_SAC_CHAMADO
                (cd_chamado, cd_cliente, vl_indice_satisfacao, st_chamado)
            VALUES
                (SGV_SAC_CHAMADO_SEQ.NEXTVAL, :1, :2,:3)
        """,(rm, nota, classificacao))

        conn.commit()
        print("✔ Avaliação salva no bano Oracle com sucesso!")

    except Exception as e:
        print(f" Erro ao salvar no banco: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

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

