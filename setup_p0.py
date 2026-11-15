import os

def criar_estrutura_p0():
    print("Criando a estrutura de pastas e arquivos para o P0...")

    # Diretórios obrigatórios
    diretorios = ['src', 'tests', 'docs', 'logs', 'data']
    for diretorio in diretorios:
        os.makedirs(diretorio, exist_ok=True)
        # Cria um arquivo .gitkeep para garantir que pastas vazias sejam versionadas se necessário
        with open(os.path.join(diretorio, '.gitkeep'), 'w', encoding='utf-8') as f:
            pass

    # 1. README.md principal
    readme_conteudo = """# Projeto P0 - Configuração e Estrutura Inicial

Repositório público criado para a entrega do projeto P0.

## Estrutura do Repositório
- `src/`: Código-fonte principal da aplicação/agente.
- `tests/`: Casos de teste automatizados e validações.
- `docs/`: Relatório principal do projeto (`relatorio-principal.md`).
- `logs/`: Registros de execução e traces necessários à avaliação.
- `data/`: Amostras fictícias e dados públicos (sem informações restritas).

## Como Executar
1. Instale as dependências.
2. Configure o arquivo `.env` baseado no `.env.example`.
3. Execute os testes na pasta `tests/`.
"""
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_conteudo)

    # 2. .gitignore adequado
    gitignore_conteudo = """# Ambientes virtuais e dependências
venv/
env/
__pycache__/
*.py[cod]
node_modules/

# Configurações locais e segredos
.env
*.log
.DS_Store

# Dados sensíveis ou temporários
data/*.csv
!data/.gitkeep
"""
    with open('.gitignore', 'w', encoding='utf-8') as f:
        f.write(gitignore_conteudo)

    # 3. .env.example (sem segredos)
    env_example_conteudo = """# Exemplo de variáveis de ambiente necessárias
# Copie este arquivo para .env e preencha com seus valores locais (nunca versione o .env)
API_KEY=sua_chave_aqui
ENVIRONMENT=development
"""
    with open('.env.example', 'w', encoding='utf-8') as f:
        f.write(env_example_conteudo)

    # 4. Relatório principal em docs/
    relatorio_conteudo = """# Relatório Principal - P0

## 1. Visão Geral
Este documento apresenta a estruturação inicial do projeto P0, contemplando a arquitetura de pastas, padrões de versionamento e requisitos de entrega.

## 2. Evidências de Configuração
- Repositório público configurado no GitHub.
- Estruturação modular (`src`, `tests`, `docs`).
- Histórico de commits evolutivo com uso de Pull Request.
"""
    with open(os.path.join('docs', 'relatorio-principal.md'), 'w', encoding='utf-8') as f:
        f.write(relatorio_conteudo)

    print("Estrutura gerada com sucesso! Agora siga os passos do Git para versionar.")

if __name__ == '__main__':
    criar_estrutura_p0()