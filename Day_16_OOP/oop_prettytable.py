from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokémon name",["Chespin","Quilladin","Chesnaught"])
table.add_column("Type", ["Grass","Grass","Grass,Fighting"])

# 置中
# print(table.align)
# {'Pokémon name': 'c', 'Type': 'c'}

# 更改為靠左
table.align='l'

print(table)