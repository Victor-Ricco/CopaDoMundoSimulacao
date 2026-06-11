# Simulador de Copa do Mundo - Python + SQLite

## 📖 Sobre o Projeto

Este projeto consiste em um simulador de torneio eliminatório inspirado na Copa do Mundo, desenvolvido em Python utilizando SQLite para persistência dos dados.

O sistema realiza a simulação automática das partidas, gera resultados aleatórios, registra estatísticas das equipes e armazena todas as informações em um banco de dados local.

---

## 🚀 Funcionalidades

* Simulação de partidas com placares aleatórios.
* Critério de desempate automático em caso de empate.
* Armazenamento das partidas no banco SQLite.
* Registro dos vencedores e eliminados.
* Controle de gols pró e gols contra das equipes.
* Avanço automático entre as fases do torneio.
* Consultas estatísticas ao final da competição.

---

## 🏆 Fases do Torneio

O sistema suporta um torneio eliminatório com:

* Fase 16 avos
* Oitavas de Final
* Quartas de Final
* Semifinais
* Final

Cada partida gera automaticamente um classificado para a próxima fase.

---

## 🗄️ Estrutura do Banco de Dados

### Tabela `equipes`

| Campo       | Tipo      |
| ----------- | --------- |
| nome_time   | TEXT (PK) |
| gols_pro    | INTEGER   |
| gols_contra | INTEGER   |

---

### Tabela `partidas`

| Campo | Tipo         |
| ----- | ------------ |
| id    | INTEGER (PK) |
| fase  | TEXT         |

---

### Tabela `equipe_partidas`

| Campo       | Tipo         |
| ----------- | ------------ |
| id          | INTEGER (PK) |
| equipe_nome | TEXT (FK)    |
| partida_id  | INTEGER (FK) |


---

### Tabela `resultados`

| Campo         | Tipo         |
| ------------- | ------------ |
| id            | INTEGER (PK) |
| partida_id    | INTEGER (FK) |
| ganhador_nome | TEXT (FK)    |
| perdedor_nome | TEXT (FK)    |


---

## 📂 Estrutura do Projeto

```text
├── banco.db
src/
│
├── main.py
├── MainDb.py
│
└── model/
    ├── partidas.py

```

---

## ⚙️ Tecnologias Utilizadas

* Python
* SQLite3
* Random (biblioteca padrão)

---

## ▶️ Como Executar

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
```

2. Entre na pasta do projeto:

```bash
cd projeto
```

3. Execute:

```bash
python main.py
```

O banco de dados será criado automaticamente caso não exista.

---

## 📊 Consultas Automaticas

### Equipe(s) com mais gols

Retorna todas as equipes empatadas na liderança de gols marcados.

### Melhor defesa

Retorna todas as equipes que sofreram menos gols.

### Quantidade de partidas por fase

Exibe quantas partidas ocorreram em cada fase do torneio.

---

## 🎲 Regras da Simulação

* Cada equipe pode marcar entre 0 e 10 gols por partida.
* Em caso de empate, o vencedor é escolhido aleatoriamente.
* Os gols marcados e sofridos são acumulados durante toda a competição.
* Todos os resultados são persistidos no banco SQLite.

---

## 👨‍💻 Autor

Victor Ricco
