class GraphVisitor:
    def __init__(self, error_listener, tokens):
        self.error_listener = error_listener
        self.tokens = tokens

    def visit(self, graph):
        if getattr(graph, "directed", False):
            for token in self.tokens:
                if token.text == '--':
                    self.error_listener.report_graph_direction_error(
                        line=getattr(token, 'line', 0),
                        column=getattr(token, 'column', 0),
                        message="Undirected edge '--' used in a directed graph.",
                        context_line=None
                    )