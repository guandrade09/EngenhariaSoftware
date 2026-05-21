import time

print("🏋️ GymTrack — Validador de Treino")
print("=" * 40)

# --- DADOS DO TREINO (mude os valores para testar!) ---
exercicio = "Supino Reto"
peso_kg   = 80
repeticoes = 10

# -------------------------------------------------------
# RF01 — O sistema deve validar o nome do exercício
# (não pode ser vazio)
# -------------------------------------------------------

if exercicio != "":
    print(f"✅ [RF01] Exercício válido: '{exercicio}'")
else:
    print(f"❌ [RF01] Nome do exercício não pode ser vazio!")

# -------------------------------------------------------
# RF02 — O peso deve estar entre 1 e 300 kg
# -------------------------------------------------------

if peso_kg >= 1 and peso_kg <=300 :
    print(f"✅ [RF02] Peso válido: {peso_kg}kg")
else:
    print(f"❌ [RF02] Peso inválido: {peso_kg}kg ← deve estar entre 1 e 300kg")

# -------------------------------------------------------
# RF03 — As repetições devem estar entre 1 e 50
# -------------------------------------------------------

if 1 <= repeticoes <= 50:
    print(f"✅ [RF03] Repetições válidas: {repeticoes}")
else:
    print(f"❌ [RF03] Repetições inválidas: {repeticoes} ← deve estar entre 1 e 50")

# -------------------------------------------------------
# RNF01 — O registro deve ocorrer em menos de 200ms
# -------------------------------------------------------

inicio = time.time()
# Simula o registro no banco de dados
time.sleep(0.05)
print(f"✅ Série registrada: {exercicio} | {peso_kg}kg x {repeticoes} reps")
fim = time.time()
tempo_ms = (fim - inicio) * 1000
if tempo_ms < 200:
    print(f"✅ [RNF01] Tempo de registro: {tempo_ms:.0f}ms ← dentro do limite!")
else:
    print(f"❌ [RNF01] Lento demais: {tempo_ms:.0f}ms ← limite é 200ms")

# REFLEXÃO:
# 1. Qual a diferença entre RF e RNF que você percebeu na prática?
# R: RF define o que o sistema deve fazer, como a regra de negócio, e RNF define como o sistema deve fazer, como foco em performance.

# 2. O que aconteceria se esquecêssemos o RNF de performance?
# R: O sistema funcionaria perfeitamente na fase de desenvolvimento e testes, mas teria problemas no uso real quando vários usuários acessam ao mesmo tempo.

# 3. Cite 1 RNF que o GymTrack deveria ter mas que você não implementou
# R: RFN de segurança, para prevenção de vazamento de dados massivos dos usuários.