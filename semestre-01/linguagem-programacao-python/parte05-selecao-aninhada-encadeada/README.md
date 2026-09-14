# 🐍 Parte 05 — Estruturas de Seleção Aninhadas e Encadeadas

> Exercício sobre seleção encadeada usando `elif`, alternativa mais enxuta a aninhar vários `if` / `else`.

---

## 1️⃣ Classificador de Nota

Classifica a nota de um aluno em conceitos (A, B, C) ou reprovação, usando `elif` para verificar múltiplas faixas.

```python
Nota = float(input("Digite a nota do aluno: "))

if Nota >= 9:
    print("Conceito A")
elif Nota >= 7:
    print("Conceito B")
elif Nota >= 5:
    print("Conceito C")
else:
    print("Reprovado")
```

| Arquivo | Descrição |
|---|---|
| `ex1-classificador-nota.py` | Código-fonte |

---

## 🧠 Aprendizados

- Diferença entre aninhar `if` / `else` e usar `elif`
- Construção de estruturas de seleção com múltiplas condições em sequência
- Operações básicas com strings (concatenação `+`, repetição `*`, comparação)
