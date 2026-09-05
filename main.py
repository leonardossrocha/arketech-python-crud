import mysql.connector
from mysql.connector import Error
import os

# ==========================================
# CONFIGURAÇÃO DA CONEXÃO
# ==========================================
def conectar():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            database='arketech_db',
            user='root',          # Ajustar para o seu utilizador local
            password=''  # Ajustar para a sua palavra-passe
        )
        return conexao
    except Error as e:
        print(f"❌ Erro crítico ao ligar ao MySQL: {e}")
        return None

# ==========================================
# MÓDULOS DE CRUD
# ==========================================
def cadastrar_usuario(nome, email, cargo):
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            sql = "INSERT INTO usuarios (nome, email, cargo) VALUES (%s, %s, %s)"
            cursor.execute(sql, (nome, email, cargo))
            conexao.commit()
            print(f"\n✅ Utilizador '{nome}' registado com sucesso! (ID: {cursor.lastrowid})")
        except Error as e:
            print(f"\n⚠️ Erro ao registar: {e}")
        finally:
            cursor.close()
            conexao.close()

def listar_usuarios():
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT id, nome, email, cargo FROM usuarios")
            registos = cursor.fetchall()
            
            print("\n" + "="*50)
            print(f"| {'ID':<3} | {'NOME':<15} | {'CARGO':<20} |")
            print("="*50)
            
            if not registos:
                print("| NENHUM UTILIZADOR ENCONTRADO NA BASE DE DADOS  |")
            else:
                for linha in registos:
                    print(f"| {linha[0]:<3} | {linha[1]:<15} | {linha[3]:<20} |")
            print("="*50)
            
        except Error as e:
            print(f"\n⚠️ Erro ao consultar dados: {e}")
        finally:
            cursor.close()
            conexao.close()

def atualizar_usuario(id_usuario, novo_nome, novo_cargo):
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            sql = "UPDATE usuarios SET nome = %s, cargo = %s WHERE id = %s"
            cursor.execute(sql, (novo_nome, novo_cargo, id_usuario))
            conexao.commit()
            
            if cursor.rowcount > 0:
                print(f"\n🔄 Registo ID {id_usuario} atualizado com sucesso.")
            else:
                print(f"\n⚠️ Nenhum utilizador encontrado com o ID {id_usuario}.")
        except Error as e:
            print(f"\n⚠️ Erro ao atualizar: {e}")
        finally:
            cursor.close()
            conexao.close()

def excluir_usuario(id_usuario):
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            sql = "DELETE FROM usuarios WHERE id = %s"
            cursor.execute(sql, (id_usuario,))
            conexao.commit()
            
            if cursor.rowcount > 0:
                print(f"\n🗑️ Utilizador ID {id_usuario} eliminado permanentemente.")
            else:
                print(f"\n⚠️ Nenhum utilizador encontrado com o ID {id_usuario}.")
        except Error as e:
            print(f"\n⚠️ Erro ao eliminar: {e}")
        finally:
            cursor.close()
            conexao.close()

# ==========================================
# INTERFACE DE LINHA DE COMANDO (CLI)
# ==========================================
def exibir_menu():
    print("\n" + "="*40)
    print(f"|{'PAINEL ADMINISTRATIVO ARKETECH':^38}|")
    print("="*40)
    print(" 1. ➕ Registar Novo Utilizador")
    print(" 2. 📋 Listar Utilizadores")
    print(" 3. 🔄 Atualizar Dados")
    print(" 4. ❌ Eliminar Utilizador")
    print(" 5. 🚪 Sair do Sistema")
    print("="*40)

def iniciar_sistema():
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção (1-5): ")
        
        if opcao == '1':
            print("\n--- NOVO REGISTO ---")
            nome = input("Nome completo: ")
            email = input("E-mail corporativo: ")
            cargo = input("Cargo: ")
            cadastrar_usuario(nome, email, cargo)
            
        elif opcao == '2':
            listar_usuarios()
            
        elif opcao == '3':
            print("\n--- ATUALIZAR REGISTO ---")
            listar_usuarios()
            try:
                id_alvo = int(input("\nDigite o ID do utilizador que deseja alterar: "))
                novo_nome = input("Novo nome completo: ")
                novo_cargo = input("Novo cargo: ")
                atualizar_usuario(id_alvo, novo_nome, novo_cargo)
            except ValueError:
                print("\n⚠️ Erro: O ID deve ser um número inteiro.")
                
        elif opcao == '4':
            print("\n--- ELIMINAR REGISTO ---")
            listar_usuarios()
            try:
                id_alvo = int(input("\nDigite o ID do utilizador que deseja eliminar: "))
                confirmacao = input(f"Tem a certeza que deseja eliminar o ID {id_alvo}? (S/N): ")
                if confirmacao.upper() == 'S':
                    excluir_usuario(id_alvo)
                else:
                    print("\n🛑 Operação cancelada.")
            except ValueError:
                print("\n⚠️ Erro: O ID deve ser um número inteiro.")
                
        elif opcao == '5':
            print("\nEncerrando a ligação com a base de dados. Até logo!")
            break
            
        else:
            print("\n⚠️ Opção inválida. Tente novamente.")

# Executa o programa principal
if __name__ == "__main__":
    iniciar_sistema()