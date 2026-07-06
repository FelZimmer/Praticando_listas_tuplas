pedidos = input("Pedidos feitos (separados por vírgula): ").split(",")
print(pedidos)
pedidos.pop()
print(f"Pedidos finais: {pedidos}")
