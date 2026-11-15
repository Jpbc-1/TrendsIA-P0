# ResumoSmart — Organizador Inteligente de Notas de Estudo

Aplicação em Python desenvolvida para o projeto P0, utilizando a API do Google Gemini para transformar anotações de aulas brutas e desorganizadas em resumos acadêmicos estruturados.

## 1. Problema e Justificativa
Estudantes universitários frequentemente acumulam anotações rápidas e desestruturadas durante as aulas. Revisar esse material exige um esforço manual considerável de síntese e organização. O **ResumoSmart** resolve esse problema automatizando a extração de conceitos-chave, explicações claras e perguntas de revisão utilizando um LLM, o que seria inviável de resolver apenas com regras rígidas de texto devido à variação natural da escrita humana.

## 2. Público-Alvo
Estudantes universitários e pesquisadores que buscam otimizar o tempo de revisão de conteúdos acadêmicos.

## 3. Tecnologias Utilizadas
- **Python 3.10+**
- **Google Gemini API** (`gemini-2.5-flash-lite`)
- **google-genai** (Biblioteca oficial)
- **python-dotenv** (Gerenciamento de variáveis de ambiente)
- **pytest** (Testes automatizados)

## 4. Estrutura do Projeto
- `src/`: Contém a lógica modularizada (configuração, cliente LLM).
- `tests/`: Casos de teste automatizados (Nível Avançado).
- `data/`: Amostras de dados fictícios.
- `main.py`: Ponto de entrada da aplicação via terminal.

## 5. Instalação e Configuração

### 5.1. Clonar o repositório
```bash
git clone [https://github.com/Jpbc-1/TrendsIA-P0.git](https://github.com/Jpbc-1/TrendsIA-P0.git)
cd TrendsIA-P0
```
### 5.2. Criar e ativar o ambiente virtual
```bash
python -m venv .venv
# No Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# No Linux/macOS:
source .venv/bin/activate
```

### 5.3. Instalar dependências
```bash
pip install -r requirements.txt
```
## 5.4. Configurar as credenciais
```bash
Crie um arquivo .env na raiz do projeto baseando-se no .env.example:
GEMINI_API_KEY=sua_chave_real_aqui
GEMINI_MODEL=gemini-2.5-flash-lite
```

## 6. Como Executar
```bash
python main.py
```

# 7. Executando os Testes
```bash
Para rodar os testes unitários locais (sem consumir a API):
pytest
```

# 8. Limitações Conhecidas
```bash
- Depende de conexão ativa com a internet e da disponibilidade da API do Gemini.
- Textos excessivamente longos podem atingir os limites de tokens da janela de contexto da versão escolhida.
```