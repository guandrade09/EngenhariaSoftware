# 📋 SRS — FIAP Marketplace

**Versão:** 1.0  
**Descrição:** Plataforma de e-commerce multi-vendedor com cadastro de produtos, busca, checkout e avaliação de vendedores.

---

## 📑 Sumário

1. [Requisitos Funcionais](#requisitos-funcionais)
2. [Requisitos Não-Funcionais](#requisitos-não-funcionais)

---

## 🔧 Requisitos Funcionais (4)

### RF-001 — Cadastro de Produto

| Campo          | Detalhe |
|----------------|---------|
| **Prioridade** | Alta |
| **Ator**       | Vendedor |
| **Descrição**  | O vendedor deve poder cadastrar um produto informando nome (mínimo 3 caracteres), descrição, preço e pelo menos 1 foto. O sistema valida todos os campos antes de salvar. |
| **Pré-condição** | Vendedor autenticado e com cadastro aprovado na plataforma |
| **Pós-condição** | Produto salvo no catálogo e disponível para busca em até 30 segundos |

### RF-002 — Busca por Categoria

| Campo          | Detalhe |
|----------------|---------|
| **Prioridade** | Alta |
| **Ator**       | Cliente |
| **Descrição**  | O cliente pode filtrar produtos por categoria, faixa de preço e avaliação mínima (1 a 5 estrelas). Os resultados são paginados com até 20 itens por página e ordenados por relevância por padrão. |
| **Pré-condição** | Ao menos 1 produto cadastrado e indexado no catálogo |
| **Pós-condição** | Lista de produtos filtrada exibida em menos de 2 segundos |

### RF-003 — Checkout e Pagamento

| Campo          | Detalhe |
|----------------|---------|
| **Prioridade** | Alta |
| **Ator**       | Cliente |
| **Descrição**  | O cliente pode finalizar a compra escolhendo entre cartão de crédito (até 12 parcelas), PIX ou boleto bancário. O pedido é confirmado somente após aprovação do pagamento pela gateway. |
| **Pré-condição** | Carrinho com ao menos 1 item e cliente autenticado |
| **Pós-condição** | Pedido criado com status 'Aguardando envio' e e-mail de confirmação enviado em 1 minuto |

### RF-004 — Avaliação do Vendedor

| Campo          | Detalhe |
|----------------|---------|
| **Prioridade** | Média |
| **Ator**       | Cliente |
| **Descrição**  | Após receber o pedido, o cliente pode avaliar o vendedor com nota de 1 a 5 estrelas e comentário de até 500 caracteres. Cada cliente pode avaliar o mesmo vendedor no máximo 1 vez por pedido. |
| **Pré-condição** | Pedido com status 'Entregue' e prazo máximo de 30 dias após entrega |
| **Pós-condição** | Avaliação publicada no perfil do vendedor e média recalculada imediatamente |

---

## ⚡ Requisitos Não-Funcionais (3)

| ID | Categoria | Descrição | Critério de Aceitação |
|----|-----------|-----------|----------------------|
| **RNF-001** | Disponibilidade | A plataforma deve estar disponível 99,9% do tempo (downtime máximo de 8,7 horas/ano), exceto janelas de manutenção programadas com 48 horas de antecedência. | Monitoramento via UptimeRobot com alertas em < 1 minuto. Relatório mensal de SLA disponibilizado aos stakeholders. |
| **RNF-002** | Desempenho | O tempo de resposta da busca deve ser inferior a 2 segundos para consultas com até 10.000 produtos indexados, suportando 5.000 usuários simultâneos. | Teste de carga com k6: 5.000 usuários virtuais, p95 < 2s, taxa de erro < 0,1%. |
| **RNF-003** | Conformidade com LGPD | Todos os dados pessoais dos clientes (nome, CPF, endereço, histórico de compras) devem ser coletados com consentimento explícito, armazenados com criptografia AES-256 e excluídos em até 30 dias após solicitação. | Auditoria semestral por DPO certificado; relatório de impacto (RIPD) aprovado antes do lançamento; funcionalidade 'Excluir minha conta' testada e documentada. |

---

*Documento gerado automaticamente pelo módulo SRS · FIAP Marketplace*