# 🐍 Parte 03 — Funções Embutidas, Entrada e Saída, Operadores e Expressões Aritméticas

> Exercícios de fixação sobre `input()`, conversão de tipos, operadores compostos (`+=`), precedência de operadores e formatação de saída com f-strings.

---

## 1️⃣ Calculadora de Gorjeta

Solicita o valor de uma conta e a porcentagem de gorjeta desejada, calculando o valor da gorjeta e o total final a pagar.

```python
Valor = float(input("O valor da conta é: "))
porcentagem = int(input("Deseja colocar uma porcentagem na gorjeta? "))
Gorjeta = Valor * (porcentagem / 100)
Final = Valor + Gorjeta

print(f"O valor da conta é {Valor}, a gorjeta é {Gorjeta} e o valor final fica {Final}")
```

| Arquivo | Descrição |
|---|---|
| `ex1-calculadora-gorjeta.py` | Código-fonte |

---

## 2️⃣ Precedência de Operadores

Avaliação manual de uma expressão com atribuição composta (`+=`), potência (`**`), divisão e multiplicação, respeitando a ordem de precedência.

**Expressão:** `s += a + b**(c-d)/e * f`
**Valores:** `a=5, b=4, c=9, d=7, e=1, f=2, s=10`

**Resolução passo a passo:**

| Etapa | Cálculo | Resultado |
|:---:|---|:---:|
| 1 | `(c - d)` = 9 - 7 | **2** |
| 2 | `b ** 2` = 4² | **16** |
| 3 | `16 / e` = 16 / 1 | **16** |
| 4 | `16 * f` = 16 × 2 | **32** |
| 5 | `a + 32` = 5 + 32 | **37** |
| 6 | `s += 37` → 10 + 37 | **47** |

**Resultado final:** `s = 47`

```python
a = 5
b = 4
c = 9
d = 7
e = 1
f = 2
s = 10

s += a + b**(c-d)/e * f
print(s)
```

| Arquivo | Descrição |
|---|---|
| `ex2-precedencia-operadores.py` | Código-fonte |

---

## 🧠 Aprendizados

- Uso de `input()` e conversão de tipos (`float()`, `int()`)
- Diferença entre `input()` (entrada) e `print()` (saída)
- Operadores de atribuição composta (`+=`)
- Precedência de operadores: parênteses → potência → multiplicação/divisão → soma
- Formatação de saída com f-strings (`f"texto {variavel}"`)
