# 📘 Parte 04 — Operadores Lógicos e Estrutura de Seleção Simples e Composta

> Exercício de fixação sobre **expressões lógicas** (`AND`, `OR`, `NOT`) e **estrutura de seleção composta** (`Se... Então... Senão`).

---

## 1️⃣ Verificar se Pode Dirigir

Verifica se uma pessoa pode dirigir, com base em dois critérios combinados com **AND**: ter 18 anos ou mais **e** possuir carteira de motorista.

**Condição:** `idade >= 18 && temCarteira == "S"`

| Arquivo | Descrição |
|---|---|
| `ex1-pode-dirigir.png` | Fluxograma |
| `ex1-pode-dirigir.por` | Pseudocódigo |

### Casos testados
| idade | temCarteira | Resultado |
|:---:|:---:|---|
| 20 | S | Pode dirigir |
| 25 | N | Não pode dirigir |

---

## 🧠 Aprendizados
- Operadores lógicos `AND`, `OR` e `NOT`
- Diferença entre `=` (atribuição) e `==` (comparação)
- Estrutura de seleção composta (`se / senao`)
- Combinação de múltiplas condições numa única expressão lógica
