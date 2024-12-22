def quadrado_perfeito_mais_proximo(index: int, radicand: float) -> list[int]:
    incremente = 1
    k = incremente
    numIteracao = 0
    while (k ** index) < radicand:
        k += incremente
        incremente += 1
        numIteracao += 1
    while (k ** index) > radicand:
        k -= 1

    # # Comparamos os dois quadrados perfeitos mais próximos: k^2 e (k-1)^2
    # menor_quadrado = (k - 1) ** 2
    # maior_quadrado = k ** 2

    print(numIteracao)
    return [k, k+1]
    # Verificamos qual dos dois está mais próximo de n
    # if abs(n - menor_quadrado) < abs(n - maior_quadrado):
    #     return menor_quadrado
    # else:
    #     return maior_quadrado


# numero = 1690
# fun: quadrado_perfeito_mais_proximo = quadrado_perfeito_mais_proximo
# print(f"O quadrado perfeito mais próximo de {numero} é {fun(2, numero)}.")


def testSympify():
    from sympy import Symbol, sympify

    # Definindo a função root
    def root(n, x):
        """Calcula a raiz n-ésima de x."""
        return x**(1/n)
    # Definindo o contexto
    context = {
        'root': root,  # Adicionando a função root
        'x': Symbol('x')  # Registrando a variável x
    }

    # Testando a expressão
    expStr = 'root(2, x)'  # Exemplo de raiz quadrada
    exp = sympify(expStr, locals=context)

    # Imprimindo a expressão simbólica
    print("Expressão simbólica:", exp)

    # Calculando o valor para x=4
    value = exp.evalf(subs={'x': 4})
    print("Valor da expressão quando x=4:", value)
