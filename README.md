# Alocação Otimizada de Disciplinas em Salas de Aula

## Descrição

Esta aplicação em Python permite a alocação de disciplinas em salas de aula de acordo com a capacidade das salas e os horários das disciplinas. A aplicação lê os dados das disciplinas e salas a partir de arquivos .txt, processa a alocação, e exibe os resultados em uma interface gráfica intuitiva utilizando o Tkinter.

## Funcionalidades

- Alocação automática de disciplinas nas salas com base na capacidade e disponibilidade de horários.
- Exibição dos resultados da alocação em uma interface gráfica utilizando Tkinter.

## Estrutura do Projeto

O projeto é composto pelos seguintes componentes principais:

### Classes

- **Disciplina:** Representa uma disciplina com atributos de descrição, tamanho da turma, horário de início e término.
- **Sala:** Representa uma sala com atributos de identificação, capacidade e uma lista de disciplinas alocadas.

### Funções

- **ler_disciplinas(arquivo):** Lê as disciplinas a partir de um arquivo .txt e retorna uma lista de objetos Disciplina.
- **ler_salas(arquivo):** Lê as salas a partir de um arquivo .txt e retorna uma lista de objetos Sala.
- **alocar_disciplinas(disciplinas, salas):** Aloca as disciplinas nas salas utilizando método guloso com base na capacidade e horários disponíveis, retornando as salas com as disciplinas alocadas.

## Arquivos de Entrada

- **`disciplinas.txt`:** Contém as informações das disciplinas no formato: <br>
*Descrição, Tamanho da Turma, Hora de Início (HH:MM), Hora de Término (HH:MM)*

- **`salas.txt`:** Contém as informações das salas no formato: <br>
*Identificação, Capacidade*

## Interface Gráfica

A interface gráfica é construída utilizando Tkinter e apresenta uma árvore (Treeview) para exibir as salas e suas respectivas disciplinas alocadas.

## Requisitos

- Python 3.x
- Tkinter (incluído na maioria das distribuições Python)

## Instruções de Uso

1. Certifique-se de ter os arquivos disciplinas.txt e salas.txt no mesmo diretório do script Python.
2. Execute o script Python. A interface gráfica será aberta e exibirá a alocação das disciplinas nas salas.
3. Na interface, você poderá visualizar cada sala com sua capacidade e as disciplinas alocadas com seus respectivos horários e tamanhos de turma.

## Execução

Para executar a aplicação, utilize o comando: <br>
*`python algoritmo.py`*

## Observações

- Certifique-se de que os arquivos de entrada estejam no formato correto.
- A aplicação imprime mensagens de aviso no console caso não seja possível alocar uma disciplina em nenhuma sala.

Esta aplicação é útil para gestores acadêmicos que precisam organizar as disciplinas em salas de aula de forma eficiente, levando em consideração tanto a capacidade das salas quanto a disponibilidade de horários.
