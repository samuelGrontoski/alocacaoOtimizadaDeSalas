# Alocação Otimizada de Disciplinas em Salas de Aula

## Descrição

Esta aplicação em Python permite a alocação de disciplinas em salas de aula de acordo com a capacidade das salas e os horários das disciplinas. Utilizando o Tkinter para a interface gráfica, a aplicação lê os dados das disciplinas e salas a partir de arquivos .txt, processa a alocação, e exibe os resultados em uma interface intuitiva.

## Funcionalidades

- Alocação automática de disciplinas nas salas com base na capacidade e disponibilidade de horários.
- Exibição dos resultados da alocação em uma interface gráfica utilizando Tkinter.

## Estrutura do Projeto

O projeto é composto pelos seguintes componentes principais:

### Classes

- **Disciplina:** Representa uma disciplina com atributos de descrição, tamanho da turma, horário de início e término.
- **Sala:** Representa uma sala com atributos de identificação, capacidade e uma lista de disciplinas alocadas.