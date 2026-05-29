# Camping Artistas Pipeline

Pipeline operacional desenvolvido em Python para gerenciamento de inscrições de eventos/festivais com integração ao Google Sheets.

O projeto começou como uma automação simples de classificação de dados (V1) e evoluiu para uma arquitetura incremental persistente (V2), focada em operação contínua, reconstrução de estado e redução de retrabalho humano.

---

# Objetivo

Automatizar o recebimento, processamento e organização de inscrições do Camping dos Artistas do festival Universo Paralello.

O sistema busca facilitar:

* classificação operacional;
* visualização contínua;
* persistência local;
* exportação offline;
* auditoria básica;
* reconstrução de dados.

---

# Evolução do Projeto

## V1 — Automação inicial

A primeira versão foi criada com foco em:

* leitura de dados do Google Sheets;
* limpeza e classificação;
* exportação CSV;
* separação entre registros válidos e inválidos.

### Limitações da V1

Com o crescimento da operação surgiram alguns problemas:

* sobrescrita de dados;
* ausência de persistência real;
* dificuldade de auditoria;
* perda de histórico operacional;
* dependência excessiva de exportações manuais.

---

## V2 — Pipeline incremental persistente

A segunda versão introduziu uma arquitetura mais robusta e próxima de cenários reais de operação.

### Principais melhorias

#### Processamento incremental

O sistema passou a identificar apenas novos registros enviados pelo formulário.

---

#### Snapshot persistente

Todos os registros agora são armazenados localmente em um snapshot JSON.

Isso permite:

* reconstrução completa do estado operacional;
* recuperação de dados;
* persistência histórica;
* exportação consolidada;
* sincronização contínua.

---

#### Reconstrução automática do Google Sheets

As abas operacionais agora podem ser reconstruídas dinamicamente a partir do snapshot:

* dados_ok
* dados_ruins
* dados_duplicados

---

#### Visualização operacional contínua

O sistema exibe continuamente o estado atual da operação via terminal.

---

#### Separação de responsabilidades

A arquitetura foi reorganizada em módulos independentes:

* leitura;
* escrita;
* persistência;
* exportação;
* visualização;
* relatórios;
* gráficos.

---

# Arquitetura Atual

## Entrada

Google Forms → Google Sheets

## Pipeline

Leitura → limpeza → classificação → persistência → reconstrução → exportação

## Persistência local

* processados.json
* snapshot.json

## Saídas

* Google Sheets
* CSV consolidado
* gráficos
* logs
* relatório operacional

---

# Estrutura do Projeto

```text
config/
data/
exports/
services/
utils/
```

---

# Tecnologias Utilizadas

* Python
* Pandas
* GSpread
* Google Sheets API
* JSON
* CSV

---

# Cenário de Uso

O sistema foi pensado inicialmente para auxiliar a operação do Camping dos Artistas do festival Universo Paralello.

A proposta é permitir:

* organização operacional;
* acompanhamento de inscrições;
* classificação automatizada;
* persistência local;
* exportação offline;
* recuperação de estado.

---

# Próxima Evolução — V3

A próxima etapa do projeto pretende introduzir:

* dashboard Streamlit;
* sincronização offline/online;
* auditoria de alterações;
* resolução de conflitos humanos;
* métricas operacionais;
* painel em tempo real.

---

# Autor

Vinicius Andrade
