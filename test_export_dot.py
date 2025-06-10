from parsing.ast_builder import parse_graphgif_file
from visitors.ast_to_dot import ast_to_dot

ast, _ = parse_graphgif_file("examples/example4.gg")
dot_dict = ast_to_dot(ast)

for name, dot_str in dot_dict.items():
    with open(f"{name}.dot", "w", encoding="utf-8") as f:
        f.write(dot_str)
    print(f"Zapisano {name}.dot")


