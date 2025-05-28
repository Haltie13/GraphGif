from grammar.GraphgifParser import GraphgifParser
from grammar.GraphgifVisitor import GraphgifVisitor
import graphviz

class GraphgifVisitorImpl(GraphgifVisitor):
    def __init__(self):
        self.graphs = {}
        self.variables = {}
        self.dot = None  

    def visitProgram(self, ctx: GraphgifParser.ProgramContext):
        print("Starting visitProgram")
        for child in ctx.getChildren():
            if isinstance(child, (GraphgifParser.VarDeclContext, 
                                  GraphgifParser.GraphDeclContext,
                                  GraphgifParser.CommandContext)):
                print(f"Visiting child of type {type(child).__name__}")
                self.visit(child)
        print("Finished visitProgram")
        return self.graphs

    def visitVarDecl(self, ctx: GraphgifParser.VarDeclContext):
        var_type = ctx.varType().getText()
        var_name = ctx.ID().getText()
        var_value = self.visit(ctx.varValue())
        print(f"VarDecl: {var_type} {var_name} = {var_value}")
        if var_type == "node" or var_type == "edge":
            self.variables[var_name] = var_value if isinstance(var_value, list) else [var_value]
        elif var_type == "attributes":
            self.variables[var_name] = var_value

    def visitGraphDecl(self, ctx: GraphgifParser.GraphDeclContext):
        graph_name = ctx.ID().getText()
        directed = ctx.getChild(0).getText() == 'directed'
        print(f"Creating {'directed' if directed else 'undirected'} graph '{graph_name}'")

        self.dot = graphviz.Digraph(graph_name, strict=True) if directed else graphviz.Graph(graph_name, strict=True)

        for child in ctx.getChildren():
            print(f"Visiting child of GraphDecl: {type(child).__name__} '{child.getText()[:30]}'")
            self.visit(child)

        self.graphs[graph_name] = self.dot
        print(f"Graph '{graph_name}' created with {len(self.dot.body)} elements.")
        self.dot = None  # reset po zakończeniu

    def visitNodeDecl(self, ctx: GraphgifParser.NodeDeclContext):
        nodes = self.visit(ctx.nodeList()) if ctx.nodeList() else [ctx.nodeVarRef().ID().getText()]
        attrs = self.visit(ctx.attrList()) if ctx.attrList() else {}
        print(f"Adding nodes {nodes} with attributes {attrs}")
        for node in nodes:
            self.dot.node(node, **attrs)

    def visitEdgeDecl(self, ctx: GraphgifParser.EdgeDeclContext):
        source = ctx.ID(0).getText()
        target = ctx.ID(1).getText()
        attrs = self.visit(ctx.attrList()) if ctx.attrList() else {}
        print(f"Adding edge from '{source}' to '{target}' with attributes {attrs}")
        self.dot.edge(source, target, **attrs)

    def visitCommand(self, ctx: GraphgifParser.CommandContext):
        graph_name = ctx.ID().getText()
        args = {arg.ID().getText(): self.visit(arg.path()) for arg in ctx.argList().argument()} if ctx.argList() else {}
        print(f"Executing command on graph '{graph_name}' with args {args}")
        if graph_name in self.graphs:
            graph = self.graphs[graph_name]
            output_file = args.get('output', 'output.png')
            print(f"Rendering graph '{graph_name}' to file '{output_file}'")
            graph.render(outfile=output_file, format='png', cleanup=True)

    def visitAttrList(self, ctx: GraphgifParser.AttrListContext):
        attrs = {attr.ID().getText(): self.visit(attr.value()) for attr in ctx.attribute()}
        print(f"Attributes parsed: {attrs}")
        return attrs

    def visitValue(self, ctx: GraphgifParser.ValueContext):
        if ctx.ID():
            val = ctx.ID().getText()
            print(f"Value ID: {val}")
            return val
        elif ctx.NUMBER():
            val = ctx.NUMBER().getText()
            print(f"Value NUMBER: {val}")
            return val
        elif ctx.STRING():
            val = ctx.STRING().getText()[1:-1]
            print(f"Value STRING: {val}")
            return val

    def visitNodeList(self, ctx: GraphgifParser.NodeListContext):
        nodes = [id.getText() for id in ctx.ID()]
        print(f"Node list: {nodes}")
        return nodes

    def visitNodeVarRef(self, ctx: GraphgifParser.NodeVarRefContext):
        var_name = ctx.ID().getText()
        print(f"NodeVarRef: {var_name}")
        return self.variables.get(var_name, [])

    def visitEdgeVarRef(self, ctx: GraphgifParser.EdgeVarRefContext):
        var_name = ctx.ID().getText()
        print(f"EdgeVarRef: {var_name}")
        return self.variables.get(var_name, [])

    def visitAttrVarRef(self, ctx: GraphgifParser.AttrVarRefContext):
        var_name = ctx.ID().getText()
        print(f"AttrVarRef: {var_name}")
        return self.variables.get(var_name, {})

    def visitVarType(self, ctx: GraphgifParser.VarTypeContext):
        vt = ctx.getText()
        print(f"VarType: {vt}")
        return vt

    def visitVarValue(self, ctx: GraphgifParser.VarValueContext):
        for child in ctx.getChildren():
            val = self.visit(child)
            print(f"VarValue: {val}")
            return val

    def visitGlobalAttrDecl(self, ctx: GraphgifParser.GlobalAttrDeclContext):
        target = ctx.getChild(0).getText()
        print(f"GlobalAttrDecl target: {target}")
        if ctx.attrList():
            attrs = self.visit(ctx.attrList())
        elif ctx.attrVarRef():
            attrs = self.visit(ctx.attrVarRef())
        else:
            attrs = {}
        print(f"Applying global attributes {attrs} to {target}")
        if target == 'graph':
            self.dot.attr(**attrs)
        else:
            self.dot.attr(target, **attrs)

    def visitStatement(self, ctx: GraphgifParser.StatementContext):
        print("Visiting Statement")
        self.visit(ctx.getChild(0))

    def visitEdgeOp(self, ctx: GraphgifParser.EdgeOpContext):
        op = ctx.getText()
        print(f"EdgeOp: {op}")
        return op

    def visitEdgeList(self, ctx: GraphgifParser.EdgeListContext):
        edges = [self.visit(edgeCtx) for edgeCtx in ctx.edgeDecl()]
        print(f"EdgeList with {len(edges)} edges")
        return edges

    def visitAttribute(self, ctx: GraphgifParser.AttributeContext):
        key = ctx.ID().getText()
        value = self.visit(ctx.value())
        print(f"Attribute: {key} = {value}")
        return (key, value)

    def visitArgList(self, ctx: GraphgifParser.ArgListContext):
        args = {self.visit(arg)[0]: self.visit(arg)[1] for arg in ctx.argument()}
        print(f"ArgList: {args}")
        return args

    def visitArgument(self, ctx: GraphgifParser.ArgumentContext):
        key = ctx.ID().getText()
        value = self.visit(ctx.path())
        print(f"Argument: {key} = {value}")
        return key, value

    def visitPath(self, ctx: GraphgifParser.PathContext):
        path = '.'.join(id.getText() for id in ctx.ID())
        print(f"Path: {path}")
        return path
