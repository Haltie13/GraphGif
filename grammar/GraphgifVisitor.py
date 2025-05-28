# Generated from Graphgif.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GraphgifParser import GraphgifParser
else:
    from GraphgifParser import GraphgifParser

# This class defines a complete generic visitor for a parse tree produced by GraphgifParser.

class GraphgifVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GraphgifParser#program.
    def visitProgram(self, ctx:GraphgifParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphgifParser#varDecl.
    def visitVarDecl(self, ctx:GraphgifParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphgifParser#varType.
    def visitVarType(self, ctx:GraphgifParser.VarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphgifParser#varValue.
    def visitVarValue(self, ctx:GraphgifParser.VarValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphgifParser#graphDecl.
    def visitGraphDecl(self, ctx:GraphgifParser.GraphDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphgifParser#globalAttrDecl.
    def visitGlobalAttrDecl(self, ctx:GraphgifParser.GlobalAttrDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphgifParser#statement.
    def visitStatement(self, ctx:GraphgifParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphgifParser#nodeDecl.
    def visitNodeDecl(self, ctx:GraphgifParser.NodeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphgifParser#edgeDecl.
    def visitEdgeDecl(self, ctx:GraphgifParser.EdgeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphgifParser#edgeOp.
    def visitEdgeOp(self, ctx:GraphgifParser.EdgeOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphgifParser#nodeList.
    def visitNodeList(self, ctx:GraphgifParser.NodeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphgifParser#edgeList.
    def visitEdgeList(self, ctx:GraphgifParser.EdgeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphgifParser#attrList.
    def visitAttrList(self, ctx:GraphgifParser.AttrListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphgifParser#attribute.
    def visitAttribute(self, ctx:GraphgifParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphgifParser#value.
    def visitValue(self, ctx:GraphgifParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphgifParser#nodeVarRef.
    def visitNodeVarRef(self, ctx:GraphgifParser.NodeVarRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphgifParser#edgeVarRef.
    def visitEdgeVarRef(self, ctx:GraphgifParser.EdgeVarRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphgifParser#attrVarRef.
    def visitAttrVarRef(self, ctx:GraphgifParser.AttrVarRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphgifParser#command.
    def visitCommand(self, ctx:GraphgifParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphgifParser#argList.
    def visitArgList(self, ctx:GraphgifParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphgifParser#argument.
    def visitArgument(self, ctx:GraphgifParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphgifParser#path.
    def visitPath(self, ctx:GraphgifParser.PathContext):
        return self.visitChildren(ctx)



del GraphgifParser