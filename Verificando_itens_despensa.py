import unicodedata

def sem_acento(palavra):
    return ''.join(i for i in unicodedata.normalize("NFD", palavra) if unicodedata.category(i) != 'Mn')

despensa = ['arroz', 'feijão', 'óleo']
item = (input("Escreva o que quer verificar:"))

despensa_formatada = [sem_acento(i).lower() for i in despensa]
item_formatado = sem_acento(item).lower()

if item_formatado in despensa_formatada:
    print(f"O item {item} já está disponível na despensa.")
else:
    print(f"O item {item} precisa ser comprado.")
print(despensa)




