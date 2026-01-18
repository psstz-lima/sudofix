---
title: "Corrigir AssertionError: assert 1 == 2..."
description: "Aprenda como resolver o AssertionError em Python. Falha de alegação. Verifique sua suposição...."
pubDate: "2026-01-17"
tags: ["python", "assertionerror", "depuração"]
---

# O Erro: AssertionError

Um `AssertionError` no Python é levantado quando uma instrução `assert` falha. A instrução `assert` é usada para testar se uma condição é verdadeira em um ponto específico do programa. Se a condição avaliar como `False`, um `AssertionError` é levantado, indicando que uma suposição feita no código está incorreta. Isso geralmente usado como um auxílio de depuração para detectar erros cedo no ciclo de desenvolvimento.

## Por que ocorre

Um `AssertionError` normalmente ocorre quando a condição especificada na instrução `assert` não é verdadeira. Os principais causas incluem:

- Assumções incorretas sobre os valores ou estados das variáveis.
- Erros lógicos no código que levam a resultados inesperados.
- Desentendimentos sobre os tipos de dados ou estruturas sendo usadas.
- Alterações na codificação que afetam as suposições anteriores sem serem atualizadas.

## Exemplo de Código

Considere o seguinte trecho de código que ilustra como um `AssertionError` pode ocorrer:

```python
def check_value(x):
    assert x == 2, "x deve ser igual a 2"
    print("Valor está correto.")

check_value(1)  # Isso irá levantar um AssertionError
```

Neste exemplo, a função `check_value` faz uma asserção que o valor da variável `x` deve ser igual a `2`. Quando a função é chamada com `1`, a asserção falha, resultando em:

```
AssertionError: x deve ser igual a 2
```

Isso indica que a suposição (que `x` deve ser `2`) não foi atendida.

## Como Corrigir

Para resolver um `AssertionError`, siga essas etapas:

1. **Identifique a Asserção**: Localize a instrução `assert` que gera o erro. No exemplo acima, é `assert x == 2`.

2. **Revise a Lógica**: Revise a lógica que leva à asserção. Determine por que a condição não está sendo atendida. Neste caso, o valor passado para a função é `1`, que claramente não é igual a `2`.

3. **Modifique o Entrada**: Se o valor de entrada estiver incorreto, certifique-se de que o valor correto seja passado para a função. Por exemplo:

    ```python
    check_value(2)  # Isso irá funcionar corretamente
    ```

4. **Atualize a Asserção**: Se a expectativa for incorreta com base na lógica do seu programa, considere atualizar a asserção ou a lógica de acordo. Por exemplo, se a função deve aceitar valores menores ou iguais a `2`:

    ```python
    def check_value(x):
        assert x <= 2, "x deve ser menor que ou igual a 2"
        print("Valor está correto.")
    
    check_value(1)  # Isso agora irá funcionar corretamente
    ```

5. **Teste as Alterações**: Após fazer ajustes, teste o código com vários valores para garantir que a asserção funcione conforme esperado.

## Boas Práticas

Para evitar `AssertionError` no futuro, considere as seguintes boas práticas:

- **Use Asserções Deveriamente**: Use asserções apenas para verificar condições que nunca devem falhar em um programa corretamente funcionando. Elas servem como verificações de integridade.

- **Documente Suposições**: Claramente documente as suposições feitas no seu código, especialmente quando usadas asserções. Isso ajudará a outros a entender o intuito por trás delas.

- **Validar Entrada**: Realize validação de entrada antes das asserções para garantir que o seu programa lide com entradas inesperadas de forma suave, em vez de depender exclusivamente das asserções.

- **Use Tratamento de Exceções**: Em vez de depender apenas das asserções, implemente tratamento de exceções para gerenciar situações inesperadas no código de produção. Isso pode evitar que o programa pare e permitir uma degradação suave.

- **Revisar Código Regularmente**: Realize revisões de código regularmente para detectar erros lógicos cedo, especialmente em seções onde asserções são usadas para enfatizar suposições.

Por seguir essas diretrizes, você pode minimizar a ocorrência de `AssertionError` e melhorar a robustez do seu código Python.