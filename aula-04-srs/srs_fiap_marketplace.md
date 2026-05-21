# SRS — FIAP Marketplace

**Versão:** 1.0  
**Descrição:** Plataforma de e-commerce multi-vendedor com cadastro de produtos, busca, checkout e avaliação de vendedores.

---

## Sumário

1. [Requisitos Funcionais](#requisitos-funcionais)
2. [Requisitos Não-Funcionais](#requisitos-não-funcionais)

---

## Requisitos Funcionais (3)

### RF-001 — Cadastro de Produto

| Campo          | Detalhe |
|----------------|---------|
| **Prioridade** | Alta |
| **Ator**       | Vendedor |
| **Descrição**  | O vendedor deve conseguir cadastrar um produto informando nome, descrição, preço e foto. |
| **Pré-condição** | Vendedor autenticado e com cadastro. |
| **Pós-condição** | Produto salvo no catálogo e disponível para busca em 10 segundos. |

### RF-002 — Busca por Categoria

| Campo          | Detalhe |
|----------------|---------|
| **Prioridade** | Alta |
| **Ator**       | Cliente |
| **Descrição**  | O usuário consegue filtrar produtos por categoria, intervalo de preço e nota mínima (1 a 5 estrelas), exibindo resultados paginados com até 20 itens por página e ordenados por relevância por padrão. |
| **Pré-condição** | Pelo menos 1 produto cadastrado. |
| **Pós-condição** | Lista de produtos filtrada exibida em menos de 2 segundos. |

### RF-003 — Checkout e Pagamento

| Campo          | Detalhe |
|----------------|---------|
| **Prioridade** | Alta |
| **Ator**       | Cliente |
| **Descrição**  | O cliente consegue concluir a compra selecionando entre cartão de crédito (em até 12 parcelas), PIX ou boleto bancário, sendo que o pedido é confirmado apenas após a aprovação do pagamento pelo gateway. |
| **Pré-condição** | Carrinho com ao menos 1 item. |
| **Pós-condição** | E-mail de confirmação enviado em 1 minuto. |

---

## ⚡ Requisitos Não-Funcionais (2)

| ID | Categoria | Descrição | Critério de Aceitação |
|----|-----------|-----------|----------------------|
| **RNF-001** | Disponibilidade | O sistema precisa ficar disponível 99,9% do tempo (tempo de inatividade máximo de 8,7 horas por ano), com exceção de janelas de manutenção programadas com 48 horas de antecedência. | Alertas de 1 em 1 minuto. Relatório mensal de SLA disponibilizado aos stakeholders. |
| **RNF-002** | Conformidade com LGPD | Todos os dados pessoais dos clientes devem ser coletados com consentimento explícito, armazenados com criptografia e descartados em até 30 dias após solicitação. | Auditoria semestral por DPO certificado e relatório de impacto (RIPD). |

---