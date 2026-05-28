Camping Artistas Pipeline

Sistema em Python para automação e tratamento de inscrições via Google Forms e Google Sheets.

Objetivo

Este projeto realiza:

leitura automática de dados do Google Sheets;
limpeza e padronização de informações;
validação de CPF;
validação de telefone;
detecção de registros duplicados;
separação automática entre:
dados válidos;
dados inválidos;
dados duplicados.
Tecnologias utilizadas
Python 3.12
gspread
Google Sheets API
pandas
regex
Estrutura do projeto
config/
services/
utils/
data/

main.py
requirements.txt
Como executar
1. Clonar o projeto
git clone URL_DO_REPOSITORIO
2. Instalar dependências
pip install -r requirements.txt
3. Configurar credenciais Google

Adicionar o arquivo JSON da Service Account na raiz do projeto.

4. Executar
python main.py
Funcionalidades atuais
Integração com Google Sheets
Pipeline automatizado
Limpeza de dados
Validação básica
Separação automática em abas
Melhorias futuras
Exportação CSV
Dashboard
Interface administrativa
Logs
Deploy em nuvem
Agendamento automático
Observação

O arquivo JSON de credenciais não está incluído por segurança.