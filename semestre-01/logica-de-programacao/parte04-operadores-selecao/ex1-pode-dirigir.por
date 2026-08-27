programa {
    funcao inicio() {
        inteiro idade
        cadeia temCarteira

        escreva("Digite a idade: ")
        leia(idade)
        escreva("Você tem carteira? (S ou N): ")
        leia(temCarteira)

        se (idade >= 18 && temCarteira == "S") 
        {
            escreva("Pode dirigir")
        } senao {
            escreva("Não pode dirigir")
        }
    }
}