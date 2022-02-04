line_long = "#" * 9
line_short = "#\t\t#"
symbol_O = [line_long, line_short, line_short, line_short, line_long]
symbol_H = [line_short, line_short, line_long, line_short, line_short]

print(*symbol_O, sep="\n", end="\n\n")
print(*symbol_H, sep="\n")
