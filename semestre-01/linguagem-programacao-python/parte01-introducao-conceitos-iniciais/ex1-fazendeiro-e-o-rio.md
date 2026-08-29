\# Problema: O Fazendeiro e o Rio



Um homem precisa atravessar um rio levando um lobo, um bode e um repolho, usando um barco que só comporta ele + 1 item por vez.



\*\*Regras:\*\*

\- Lobo não pode ficar sozinho com o Bode (lobo come o bode)

\- Bode não pode ficar sozinho com o Repolho (bode come o repolho)

\- Repolho sozinho com o Lobo não tem problema



\## Solução (Tabela de Estados)



| Passo | Ação | Margem Leste | Margem Oeste | Seguro? |

|:---:|---|---|---|:---:|

| Início | — | Homem, Lobo, Bode, Repolho | — | ✅ |

| 1 | Leva o Bode → | Lobo, Repolho | Homem, Bode | ✅ |

| 2 | Volta sozinho ← | Homem, Lobo, Repolho | Bode | ✅ |

| 3 | Leva o Lobo → | Repolho | Homem, Lobo, Bode | ✅ |

| 4 | Traz o Bode de volta ← | Homem, Repolho, Bode | Lobo | ✅ |

| 5 | Leva o Repolho → | Bode | Homem, Lobo, Repolho | ✅ |

| 6 | Volta sozinho ← | Homem, Bode | Lobo, Repolho | ✅ |

| 7 | Leva o Bode → | — | Homem, Lobo, Bode, Repolho | ✅ |



\*\*Total: 7 travessias\*\*



\## Raciocínio

O ponto-chave do problema é que, ao levar o Lobo (passo 3), não se pode deixá-lo com o Bode sem supervisão. Por isso o Bode precisa "voltar" (passo 4) antes de o homem levar o Repolho — uma travessia extra que não é intuitiva à primeira vista.



\## Aprendizados

\- Abstração e representação de um problema em estados

\- Raciocínio lógico para resolução de problemas sem cálculo matemático

\- Importância de verificar restrições a cada passo antes de avançar



