# 🏢 ArkeTech: Sistema de Gestão de RH (CLI)

Um sistema interativo de linha de comando (CLI) desenvolvido em Python para gerir o registo de colaboradores, com persistência de dados num banco de dados MySQL. Este projeto implementa as quatro operações fundamentais de banco de dados (CRUD) com foco em resiliência, validação de entradas e tratamento de exceções.

## 🚀 Funcionalidades (CRUD)

- **Create (C):** Registo de novos talentos (Nome, E-mail Corporativo e Cargo).
- **Read (R):** Listagem tabular de todos os utilizadores ativos na base de dados.
- **Update (U):** Atualização ágil de cargos e nomes através da chave primária (ID).
- **Delete (D):** Eliminação permanente de registos de forma segura.
- **Blindagem de Código:** Tratamento estruturado de erros (`try/except`) para evitar travamentos (`Crash`) em falhas de conexão ou introdução de dados incorretos pelo utilizador.

## 🛠️ Stack Tecnológico

- **Python 3.x** - Lógica de programação e interface no terminal.
- **MySQL** - Motor de base de dados relacional.
- **mysql-connector-python** - Driver oficial de integração.

## ⚙️ Pré-requisitos e Instalação

Para correr este projeto na sua máquina local, certifique-se de que tem o Python e um servidor MySQL (como o XAMPP, WAMP ou MySQL nativo no Linux Debian) instalados.

**1. Clone o repositório:**
```bash
git clone [https://github.com/SEU_USUARIO/arketech-python-crud.git](https://github.com/SEU_USUARIO/arketech-python-crud.git)
cd arketech-python-crud
```

### Nota de Transparência e IA

Este projeto foi estruturado e codificado com o auxílio de ferramentas de Inteligência Artificial Generativa. A IA atuou como um parceiro de desenvolvimento (Pair Programmer) na otimização da sintaxe Python, na formatação da saída de ecrã via f-strings e na consolidação das lógicas de tratamento de exceções (blocos try/except) que garantem a segurança e a estabilidade da aplicação em ambiente de produção.


#### Autor

Prof. Me. Leonardo Rocha - [Linkedin](https://www.linkedin.com/in/leonardossrocha/)  
Mestre e Doutorando em Ciência da Computação

