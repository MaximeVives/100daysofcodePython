from prettytable import PrettyTable

table = PrettyTable()

table.title = "Pokemon Table"
table.add_column("Pokemon", ["Pikachu", "Dracaufeu", "Arceus"])
table.add_column("Type", ["Electric", "Fire", "Normal"])

print(table)

