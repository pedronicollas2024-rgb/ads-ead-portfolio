# 🐍 Parte 04 — Operadores Relacionais e Lógicos, Estruturas de Seleção Simples e Composta

> Exercício sobre operadores lógicos (`and`, `or`) combinados com estruturas de seleção (`if` / `else`).

---

## 1️⃣ Pode Dirigir

Verifica se uma pessoa pode dirigir combinando duas condições com `and`: idade mínima e posse de carteira.

```python
Idade = int(input("Digite sua idade: "))
Carteira = input("Tem carteira? (S ou N): ")

if Idade >= 18 and Carteira == "S":
    print("Você pode dirigir!")
else:
    print("Você não pode dirigir.")
```

| Arquivo | Descrição |
|---|---|
| `ex1-pode-dirigir.py` | Código-fonte |

---

## 🧠 Aprendizados

- Operadores relacionais (`>=`, `==`) e lógicos (`and`) em Python
- Diferença de sintaxe: `and` / `or` / `not` (Python) vs `&&` / `\|\|` (outras linguagens)
- Estrutura `if` / `else` com indentação obrigatória
