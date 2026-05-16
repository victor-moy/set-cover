"""
Set Cover - Problema da Cobertura de Conjuntos
Disciplina: Algoritmos e Complexidade Computacional

Duas abordagens implementadas:
  1. Força bruta (solução exata, viável apenas para entradas pequenas)
  2. Heurística gulosa (solução aproximada, eficiente para entradas maiores)
"""

from itertools import combinations


# ─────────────────────────────────────────────
# Força Bruta — solução exata
# ─────────────────────────────────────────────

def set_cover_brute_force(universe, subsets):
    """
    Testa todas as combinações possíveis de subconjuntos e retorna
    a menor cobertura que cobre todos os elementos do universo.

    Complexidade: O(2^m * n), onde m = número de subconjuntos e n = tamanho do universo.
    Inviável para entradas grandes — demonstra por que o problema é difícil.
    """
    n_subsets = len(subsets)

    # Testa combinações de tamanho crescente (1, 2, 3, ...) até encontrar cobertura
    for size in range(1, n_subsets + 1):
        for combination in combinations(range(n_subsets), size):
            # Reúne todos os elementos cobertos pelos subconjuntos escolhidos
            covered = set()
            for idx in combination:
                covered |= subsets[idx]

            # Verifica se todos os elementos do universo foram cobertos
            if universe.issubset(covered):
                chosen = [subsets[idx] for idx in combination]
                return chosen  # Retorna a menor cobertura encontrada

    return []  # Sem cobertura possível (não deve ocorrer se a entrada for válida)


# ─────────────────────────────────────────────
# Heurística Gulosa — solução aproximada
# ─────────────────────────────────────────────

def set_cover_greedy(universe, subsets):
    """
    A cada passo, escolhe o subconjunto que cobre o maior número de
    elementos ainda não cobertos. Repete até cobrir o universo inteiro.

    Complexidade: O(n * m^2)
    Garante cobertura com no máximo ln(n) + 1 vezes o tamanho ótimo.
    """
    uncovered = set(universe)   # Elementos que ainda precisam ser cobertos
    chosen = []                  # Subconjuntos selecionados

    remaining = list(subsets)   # Subconjuntos disponíveis

    while uncovered:
        # Encontra o subconjunto que cobre mais elementos ainda descobertos
        best = max(remaining, key=lambda s: len(s & uncovered))

        # Adiciona o melhor subconjunto à cobertura
        chosen.append(best)

        # Remove os elementos que agora estão cobertos
        uncovered -= best

        # Remove o subconjunto escolhido da lista de disponíveis
        remaining.remove(best)

    return chosen


# ─────────────────────────────────────────────
# Exemplo 1 — instância pequena (força bruta + gulosa)
# ─────────────────────────────────────────────

def exemplo_pequeno():
    print("=" * 55)
    print("EXEMPLO 1 — Instância Pequena (Força Bruta + Gulosa)")
    print("=" * 55)

    # Universo: todos os elementos que precisam ser cobertos
    universe = {1, 2, 3, 4, 5, 6, 7}

    # Subconjuntos disponíveis (cada um cobre parte dos elementos)
    subsets = [
        {1, 2, 3},      # Subconjunto A
        {2, 4},         # Subconjunto B
        {3, 4, 5},      # Subconjunto C
        {5, 6, 7},      # Subconjunto D
        {1, 6},         # Subconjunto E
        {4, 7},         # Subconjunto F
    ]

    labels = ["A", "B", "C", "D", "E", "F"]

    print(f"\nUniverso: {sorted(universe)}")
    print("Subconjuntos disponíveis:")
    for label, s in zip(labels, subsets):
        print(f"  {label} = {sorted(s)}")

    # Força bruta
    resultado_bf = set_cover_brute_force(set(universe), subsets)
    print(f"\n[Força Bruta] Cobertura mínima ({len(resultado_bf)} subconjuntos):")
    for s in resultado_bf:
        idx = subsets.index(s)
        print(f"  {labels[idx]} = {sorted(s)}")

    # Gulosa
    resultado_greedy = set_cover_greedy(set(universe), subsets)
    print(f"\n[Gulosa]      Cobertura encontrada ({len(resultado_greedy)} subconjuntos):")
    for s in resultado_greedy:
        idx = subsets.index(s)
        print(f"  {labels[idx]} = {sorted(s)}")


# ─────────────────────────────────────────────
# Exemplo 2 — aplicação real: cobertura de habilidades em uma equipe
# ─────────────────────────────────────────────

def exemplo_equipe():
    print("\n" + "=" * 55)
    print("EXEMPLO 2 — Aplicação Real: Montagem de Equipe")
    print("=" * 55)

    # Habilidades necessárias no projeto
    habilidades_necessarias = {
        "backend", "frontend", "banco_de_dados",
        "segurança", "devops", "mobile"
    }

    # Candidatos disponíveis e suas habilidades
    candidatos = {
        "Alice":   {"backend", "banco_de_dados", "segurança"},
        "Bruno":   {"frontend", "mobile"},
        "Carla":   {"devops", "backend"},
        "Diego":   {"frontend", "segurança"},
        "Elena":   {"mobile", "devops", "banco_de_dados"},
    }

    print("\nHabilidades necessárias:")
    print(" ", sorted(habilidades_necessarias))

    print("\nCandidatos e suas habilidades:")
    for nome, skills in candidatos.items():
        print(f"  {nome}: {sorted(skills)}")

    # Converte para o formato esperado pelo algoritmo
    subsets = list(candidatos.values())
    nomes = list(candidatos.keys())

    resultado = set_cover_greedy(habilidades_necessarias, subsets)

    print(f"\n[Gulosa] Equipe mínima ({len(resultado)} pessoas) para cobrir todas as habilidades:")
    for s in resultado:
        idx = subsets.index(s)
        print(f"  {nomes[idx]}: {sorted(s)}")

    # Confirma cobertura completa
    cobertura_total = set()
    for s in resultado:
        cobertura_total |= s
    faltando = habilidades_necessarias - cobertura_total
    if not faltando:
        print("\n  Todas as habilidades cobertas!")
    else:
        print(f"\n  ATENÇÃO: habilidades não cobertas: {faltando}")


# ─────────────────────────────────────────────
# Demonstração de crescimento exponencial
# ─────────────────────────────────────────────

def demonstrar_crescimento():
    print("\n" + "=" * 55)
    print("POR QUE O PROBLEMA FICA DIFÍCIL?")
    print("Número de combinações possíveis (força bruta: 2^m)")
    print("=" * 55)

    for m in [5, 10, 20, 30, 50, 100]:
        combinacoes = 2 ** m
        print(f"  {m:>3} subconjuntos → {combinacoes:>35,} combinações")


# ─────────────────────────────────────────────
# Ponto de entrada
# ─────────────────────────────────────────────

if __name__ == "__main__":
    exemplo_pequeno()
    exemplo_equipe()
    demonstrar_crescimento()
