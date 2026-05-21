# ============================================================
# 🚀 SRS em Python — FIAP Marketplace
# Aula 04 — Engenharia de Software · FIAP
# Partes 1, 2 e 3 — Solução Completa
# ============================================================

from dataclasses import dataclass, field
from typing import List
from enum import Enum
import re


# MODELOS DE DADOS (do código original da aula)

class Prioridade(Enum):
    ALTA = "Alta"
    MEDIA = "Média"
    BAIXA = "Baixa"


@dataclass
class RequisitoFuncional:
    id: str
    nome: str
    descricao: str
    prioridade: Prioridade
    ator: str
    pre_condicao: str
    pos_condicao: str


@dataclass
class RequisitoNaoFuncional:
    id: str
    categoria: str  # Desempenho, Segurança, Usabilidade...
    descricao: str
    criterio_aceitacao: str


@dataclass
class SRS:
    projeto: str
    versao: str
    descricao: str
    requisitos_funcionais: List[RequisitoFuncional] = field(default_factory=list)
    requisitos_nao_funcionais: List[RequisitoNaoFuncional] = field(default_factory=list)

    def adicionar_rf(self, req: RequisitoFuncional):
        self.requisitos_funcionais.append(req)
        print(f"✅ RF '{req.id}' adicionado!")

    def adicionar_rnf(self, req: RequisitoNaoFuncional):
        self.requisitos_nao_funcionais.append(req)
        print(f"✅ RNF '{req.id}' adicionado!")

    def relatorio(self):
        print(f"\n{'='*50}")
        print(f"📋 SRS — {self.projeto} v{self.versao}")
        print(f"{'='*50}")
        print(f"📝 {self.descricao}\n")

        print(f"🔧 REQUISITOS FUNCIONAIS ({len(self.requisitos_funcionais)})")
        for rf in self.requisitos_funcionais:
            print(f"  [{rf.id}] {rf.nome} — Prioridade: {rf.prioridade.value}")
            print(f"       Ator: {rf.ator}")
            print(f"       📌 {rf.descricao}\n")

        print(f"⚡ REQUISITOS NÃO-FUNCIONAIS ({len(self.requisitos_nao_funcionais)})")
        for rnf in self.requisitos_nao_funcionais:
            print(f"  [{rnf.id}] {rnf.categoria}")
            print(f"       📌 {rnf.descricao}")
            print(f"       ✔️  Critério: {rnf.criterio_aceitacao}\n")

# INSTÂNCIA DO SRS — FIAP MARKETPLACE

srs = SRS(
    projeto="FIAP Marketplace",
    versao="1.0",
    descricao=(
        "Plataforma de e-commerce multi-vendedor com cadastro de produtos, "
        "busca, checkout e avaliação de vendedores."
    )
)

# PARTE 1 - Estender o código Python da aula

# Requisitos Funcionais

srs.adicionar_rf(RequisitoFuncional(
    id="RF-001",
    nome="Cadastro de Produto",
    descricao=(
        "O vendedor deve conseguir cadastrar um produto informando nome, descrição, preço e foto."
    ),
    prioridade=Prioridade.ALTA,
    ator="Vendedor",
    pre_condicao="Vendedor autenticado e com cadastro.",
    pos_condicao="Produto salvo no catálogo e disponível para busca em 10 segundos."
))

srs.adicionar_rf(RequisitoFuncional(
    id="RF-002",
    nome="Busca por Categoria",
    descricao=(
        "O usuário consegue filtrar produtos por categoria, intervalo de preço e nota mínima (1 a 5 estrelas), "
        "exibindo resultados paginados com até 20 itens por página e ordenados por relevância por padrão."
    ),
    prioridade=Prioridade.ALTA,
    ator="Cliente",
    pre_condicao="Pelo menos 1 produto cadastrado.",
    pos_condicao="Lista de produtos filtrada exibida em menos de 2 segundos."
))

srs.adicionar_rf(RequisitoFuncional(
    id="RF-003",
    nome="Checkout e Pagamento",
    descricao=(
        "O cliente consegue concluir a compra selecionando entre cartão de crédito (em até 12 parcelas), "
        "PIX ou boleto bancário, sendo que o pedido é confirmado apenas após a aprovação do pagamento pelo gateway."
    ),
    prioridade=Prioridade.ALTA,
    ator="Cliente",
    pre_condicao="Carrinho com ao menos 1 item.",
    pos_condicao="E-mail de confirmação enviado em 1 minuto."
))

# Requisitos Não-Funcionais

srs.adicionar_rnf(RequisitoNaoFuncional(
    id="RNF-001",
    categoria="Disponibilidade",
    descricao=(
        "O sistema precisa ficar disponível 99,9% do tempo (tempo de inatividade máximo de 8,7 horas por ano), "
        "com exceção de janelas de manutenção programadas com 48 horas de antecedência."
    ),
    criterio_aceitacao=(
        "Alertas de 1 em 1 minuto. Relatório mensal de SLA disponibilizado aos stakeholders."
    )
))

srs.adicionar_rnf(RequisitoNaoFuncional(
    id="RNF-002",
    categoria="Conformidade com LGPD",
    descricao=(
        "Todos os dados pessoais dos clientes devem ser coletados com consentimento explícito, "
        "armazenados com criptografia e descartados em até 30 dias após solicitação."
    ),
    criterio_aceitacao=(
        "Auditoria semestral por DPO certificado e relatório de impacto (RIPD)."
    )
))

# PARTE 2 — Função de Validação de Requisitos

def validar_requisito(rf: RequisitoFuncional) -> dict:

    resultados = {}
    avisos = []

    # Tem descrição com mais de 20 caracteres (evitar requisitos vagos)
    req_descricao = len(rf.descricao) > 20
    resultados["req_descricao"] = req_descricao
    if not req_descricao:
        avisos.append(
            f"⚠️  Descrição muito curta ({len(rf.descricao)} chars). Use mais de 20 caracteres para evitar requisitos vagos."
        )

    # Tem pré-condição definida (não vazia)
    req_pre_condicao = rf.pre_condicao.strip() != ""
    resultados["req_pre_condicao"] = req_pre_condicao
    if not req_pre_condicao:
        avisos.append("⚠️  Pré-condição não definida. Toda funcionalidade deve ter um ponto de entrada claro.")

    # Tem critério mensurável (checar se tem números na descrição)
    req_criterio = any(char.isdigit() for char in rf.descricao)
    resultados["req_criterio"] = req_criterio
    if not req_criterio:
        avisos.append(
            "⚠️  Nenhum critério mensurável encontrado na descrição. "
            "Inclua valores numéricos (tempo, tamanho, quantidade, etc.)."
        )

    # Resultado final: válido apenas se todas as três checagens passaram
    resultados["valido"] = req_descricao and req_pre_condicao and req_criterio
    resultados["avisos"] = avisos

    return resultados


def exibir_validacao(rf: RequisitoFuncional):
    """Exibe o resultado da validação de forma formatada."""
    resultado = validar_requisito(rf)
    status = "✅ VÁLIDO" if resultado["valido"] else "❌ INVÁLIDO"

    print(f"\n  [{rf.id}] {rf.nome} → {status}")
    print(f"       Descrição adequada  : {'✅' if resultado['req_descricao']    else '❌'}")
    print(f"       Pré-condição existe : {'✅' if resultado['req_pre_condicao'] else '❌'}")
    print(f"       Critério mensurável : {'✅' if resultado['req_criterio']   else '❌'}")
    for aviso in resultado["avisos"]:
        print(f"       {aviso}")

for rf in srs.requisitos_funcionais:
    exibir_validacao(rf)

srs.relatorio()

# PARTE 3 — Exportação para Markdown

def exportar_markdown(srs: SRS) -> str:

    linhas = []

    # Cabeçalho
    linhas.append(f"# SRS — {srs.projeto}")
    linhas.append(f"\n**Versão:** {srs.versao}  ")
    linhas.append(f"**Descrição:** {srs.descricao}")
    linhas.append("\n---\n")

    # Sumário
    linhas.append("## Sumário\n")
    linhas.append("1. [Requisitos Funcionais](#requisitos-funcionais)")
    linhas.append("2. [Requisitos Não-Funcionais](#requisitos-não-funcionais)")
    linhas.append("\n---\n")

    # Requisitos Funcionais
    linhas.append(f"## Requisitos Funcionais ({len(srs.requisitos_funcionais)})\n")

    for rf in srs.requisitos_funcionais:
        linhas.append(f"### {rf.id} — {rf.nome}\n")
        linhas.append(f"| Campo          | Detalhe |")
        linhas.append(f"|----------------|---------|")
        linhas.append(f"| **Prioridade** | {rf.prioridade.value} |")
        linhas.append(f"| **Ator**       | {rf.ator} |")
        linhas.append(f"| **Descrição**  | {rf.descricao} |")
        linhas.append(f"| **Pré-condição** | {rf.pre_condicao} |")
        linhas.append(f"| **Pós-condição** | {rf.pos_condicao} |")
        linhas.append("")

    linhas.append("\n---\n")

    # Requisitos Não-Funcionais
    linhas.append(f"## ⚡ Requisitos Não-Funcionais ({len(srs.requisitos_nao_funcionais)})\n")
    linhas.append("| ID | Categoria | Descrição | Critério de Aceitação |")
    linhas.append("|----|-----------|-----------|----------------------|")

    for rnf in srs.requisitos_nao_funcionais:
        linhas.append(f"| **{rnf.id}** | {rnf.categoria} | {rnf.descricao} | {rnf.criterio_aceitacao} |")

    linhas.append("\n---\n")

    return "\n".join(linhas)

print("Markdown exportado!")

markdown = exportar_markdown(srs)

# Salva em arquivo
with open("srs_fiap_marketplace.md", "w", encoding="utf-8") as f:
    f.write(markdown)

print("\n✅ Arquivo 'srs_fiap_marketplace.md' gerado com sucesso!")
print("\n--- Prévia das primeiras linhas ---\n")
print("\n".join(markdown.split("\n")[:20]))
print("...")