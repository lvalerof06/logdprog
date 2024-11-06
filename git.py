
git add pedido_pizza.py
git commit -am "atividade pizza"
git push origin maindef calcular_valor_pizza():
    pedidos = []
    while True:
        print("Escolha o tamanho da pizza:")
        print("1 - Pequena - R$ 20")
        print("2 - Média - R$ 30")
        print("3 - Grande - R$ 40")
        tamanho = input("Digite o número correspondente ao tamanho: ")
        if tamanho == '1':
            valor_pizza = 20
        elif tamanho == '2':
            valor_pizza = 30
        elif tamanho == '3':
            valor_pizza = 40
        else:
            print("Tamanho inválido. Tente novamente.")
            continue
        valor_extras = 0
        extras = input("Deseja adicionar ingredientes extras? (sim/não): ").lower()
        if extras == 'sim':
            print("Escolha os ingredientes extras (cada um custa R$ 5):")
            print("1 - Calabresa")
            print("2 - Mussarela")
            print("3 - Tomate")
            print("4 - Cebola")
            print("5 - Bacon")
            ingredientes_escolhidos = input("Digite os números dos ingredientes separados por vírgula (ex: 1,3,5): ")
            ingredientes_escolhidos = ingredientes_escolhidos.split(',')
            valor_extras = len(ingredientes_escolhidos) * 5
        refrigerante = input("Deseja refrigerante? (sim/não): ").lower()
        valor_refrigerante = 8 if refrigerante == 'sim' else 0
        valor_total = valor_pizza + valor_extras + valor_refrigerante
        print(f"Valor total do pedido: R$ {valor_total:.2f}\n")
        pedidos.append(valor_total)
        novo_pedido = input("Deseja fazer um novo pedido? (sim/não): ").lower()
        if novo_pedido != 'sim':
            break
    if pedidos:
        print("\nResumo dos pedidos:")
        print(f"Pedido mais caro: R$ {max(pedidos):.2f}")
        print(f"Pedido mais barato: R$ {min(pedidos):.2f}")
        print(f"Quantidade de pedidos realizados: {len(pedidos)}")
    else:
        print("Nenhum pedido foi realizado.")

