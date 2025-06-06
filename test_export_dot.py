from parsing.ast_builder import parse_graphgif_file
from generators import DOTGenerator

_, graph_model = parse_graphgif_file("examples/example4.gg")

dot_gen = DOTGenerator()
dot_dict = dot_gen.generate_dot(graph_model)

for name, dot_str in dot_dict.items():
    output_path = f"{name}.dot"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(dot_str)
    print(f"Zapisano {output_path}")

