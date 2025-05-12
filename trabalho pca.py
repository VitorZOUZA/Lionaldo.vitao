def analisar_numeros(numeros):
    media = sum(numeros) / len(numeros)
    maior = max(numeros)
    menor = min(numeros)
    pares = sum(1 for num in numeros if num % 2 == 0)
    
    return {
        "média": media,
        "maior": maior,
        "menor": menor,
        "quantidade_pares": pares
    }

numeros = [10, 23, 5, 8, 12, 33, 42, 7, 19, 28, 3, 16, 9, 50, 21]
resultado = analisar_numeros(numeros)
