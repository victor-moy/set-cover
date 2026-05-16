# Set Cover — Problema da Cobertura de Conjuntos

Trabalho da disciplina de **Algoritmos Avançados**.

**Equipe:** Jhessica Alves, Laíza Silva e Victor Moy

## Pré-requisitos

- Python 3.8 ou superior
- Nenhuma biblioteca externa necessária (usa apenas `itertools` da biblioteca padrão)

## Como Executar

```bash
python set_cover.py
```

## O que o código demonstra

**Exemplo 1 — Instância pequena:**
Universo com 7 elementos e 6 subconjuntos disponíveis.
Compara a solução exata (força bruta) com a heurística gulosa.

**Exemplo 2 — Aplicação real:**
Montagem de equipe mínima que cobre todas as habilidades necessárias em um projeto.

**Crescimento exponencial:**
Tabela mostrando por que a força bruta se torna inviável à medida que o número de subconjuntos cresce.

## Saída esperada

```
=======================================================
EXEMPLO 1 — Instância Pequena (Força Bruta + Gulosa)
=======================================================

Universo: [1, 2, 3, 4, 5, 6, 7]
Subconjuntos disponíveis:
  A = [1, 2, 3]
  B = [2, 4]
  C = [3, 4, 5]
  D = [5, 6, 7]
  E = [1, 6]
  F = [4, 7]

[Força Bruta] Cobertura mínima (2 subconjuntos):
  A = [1, 2, 3]
  ...

[Gulosa]      Cobertura encontrada (X subconjuntos):
  ...
```
