# Generated from Graphgif.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GraphgifParser import GraphgifParser
else:
    from GraphgifParser import GraphgifParser

# This class defines a complete listener for a parse tree produced by GraphgifParser.
class GraphgifListener(ParseTreeListener):

    # Enter a parse tree produced by GraphgifParser#program.
    def enterProgram(self, ctx:GraphgifParser.ProgramContext):
        pass

    # Exit a parse tree produced by GraphgifParser#program.
    def exitProgram(self, ctx:GraphgifParser.ProgramContext):
        pass


    # Enter a parse tree produced by GraphgifParser#varDecl.
    def enterVarDecl(self, ctx:GraphgifParser.VarDeclContext):
        pass

    # Exit a parse tree produced by GraphgifParser#varDecl.
    def exitVarDecl(self, ctx:GraphgifParser.VarDeclContext):
        pass


    # Enter a parse tree produced by GraphgifParser#varType.
    def enterVarType(self, ctx:GraphgifParser.VarTypeContext):
        pass

    # Exit a parse tree produced by GraphgifParser#varType.
    def exitVarType(self, ctx:GraphgifParser.VarTypeContext):
        pass


    # Enter a parse tree produced by GraphgifParser#varValue.
    def enterVarValue(self, ctx:GraphgifParser.VarValueContext):
        pass

    # Exit a parse tree produced by GraphgifParser#varValue.
    def exitVarValue(self, ctx:GraphgifParser.VarValueContext):
        pass


    # Enter a parse tree produced by GraphgifParser#graphDecl.
    def enterGraphDecl(self, ctx:GraphgifParser.GraphDeclContext):
        pass

    # Exit a parse tree produced by GraphgifParser#graphDecl.
    def exitGraphDecl(self, ctx:GraphgifParser.GraphDeclContext):
        pass


    # Enter a parse tree produced by GraphgifParser#globalAttrDecl.
    def enterGlobalAttrDecl(self, ctx:GraphgifParser.GlobalAttrDeclContext):
        pass

    # Exit a parse tree produced by GraphgifParser#globalAttrDecl.
    def exitGlobalAttrDecl(self, ctx:GraphgifParser.GlobalAttrDeclContext):
        pass


    # Enter a parse tree produced by GraphgifParser#statement.
    def enterStatement(self, ctx:GraphgifParser.StatementContext):
        pass

    # Exit a parse tree produced by GraphgifParser#statement.
    def exitStatement(self, ctx:GraphgifParser.StatementContext):
        pass


    # Enter a parse tree produced by GraphgifParser#nodeDecl.
    def enterNodeDecl(self, ctx:GraphgifParser.NodeDeclContext):
        pass

    # Exit a parse tree produced by GraphgifParser#nodeDecl.
    def exitNodeDecl(self, ctx:GraphgifParser.NodeDeclContext):
        pass


    # Enter a parse tree produced by GraphgifParser#edgeDecl.
    def enterEdgeDecl(self, ctx:GraphgifParser.EdgeDeclContext):
        pass

    # Exit a parse tree produced by GraphgifParser#edgeDecl.
    def exitEdgeDecl(self, ctx:GraphgifParser.EdgeDeclContext):
        pass


    # Enter a parse tree produced by GraphgifParser#edgeOp.
    def enterEdgeOp(self, ctx:GraphgifParser.EdgeOpContext):
        pass

    # Exit a parse tree produced by GraphgifParser#edgeOp.
    def exitEdgeOp(self, ctx:GraphgifParser.EdgeOpContext):
        pass


    # Enter a parse tree produced by GraphgifParser#nodeList.
    def enterNodeList(self, ctx:GraphgifParser.NodeListContext):
        pass

    # Exit a parse tree produced by GraphgifParser#nodeList.
    def exitNodeList(self, ctx:GraphgifParser.NodeListContext):
        pass


    # Enter a parse tree produced by GraphgifParser#edgeList.
    def enterEdgeList(self, ctx:GraphgifParser.EdgeListContext):
        pass

    # Exit a parse tree produced by GraphgifParser#edgeList.
    def exitEdgeList(self, ctx:GraphgifParser.EdgeListContext):
        pass


    # Enter a parse tree produced by GraphgifParser#attrList.
    def enterAttrList(self, ctx:GraphgifParser.AttrListContext):
        pass

    # Exit a parse tree produced by GraphgifParser#attrList.
    def exitAttrList(self, ctx:GraphgifParser.AttrListContext):
        pass


    # Enter a parse tree produced by GraphgifParser#attribute.
    def enterAttribute(self, ctx:GraphgifParser.AttributeContext):
        pass

    # Exit a parse tree produced by GraphgifParser#attribute.
    def exitAttribute(self, ctx:GraphgifParser.AttributeContext):
        pass


    # Enter a parse tree produced by GraphgifParser#value.
    def enterValue(self, ctx:GraphgifParser.ValueContext):
        pass

    # Exit a parse tree produced by GraphgifParser#value.
    def exitValue(self, ctx:GraphgifParser.ValueContext):
        pass


    # Enter a parse tree produced by GraphgifParser#nodeVarRef.
    def enterNodeVarRef(self, ctx:GraphgifParser.NodeVarRefContext):
        pass

    # Exit a parse tree produced by GraphgifParser#nodeVarRef.
    def exitNodeVarRef(self, ctx:GraphgifParser.NodeVarRefContext):
        pass


    # Enter a parse tree produced by GraphgifParser#edgeVarRef.
    def enterEdgeVarRef(self, ctx:GraphgifParser.EdgeVarRefContext):
        pass

    # Exit a parse tree produced by GraphgifParser#edgeVarRef.
    def exitEdgeVarRef(self, ctx:GraphgifParser.EdgeVarRefContext):
        pass


    # Enter a parse tree produced by GraphgifParser#attrVarRef.
    def enterAttrVarRef(self, ctx:GraphgifParser.AttrVarRefContext):
        pass

    # Exit a parse tree produced by GraphgifParser#attrVarRef.
    def exitAttrVarRef(self, ctx:GraphgifParser.AttrVarRefContext):
        pass


    # Enter a parse tree produced by GraphgifParser#command.
    def enterCommand(self, ctx:GraphgifParser.CommandContext):
        pass

    # Exit a parse tree produced by GraphgifParser#command.
    def exitCommand(self, ctx:GraphgifParser.CommandContext):
        pass


    # Enter a parse tree produced by GraphgifParser#argList.
    def enterArgList(self, ctx:GraphgifParser.ArgListContext):
        pass

    # Exit a parse tree produced by GraphgifParser#argList.
    def exitArgList(self, ctx:GraphgifParser.ArgListContext):
        pass


    # Enter a parse tree produced by GraphgifParser#argument.
    def enterArgument(self, ctx:GraphgifParser.ArgumentContext):
        pass

    # Exit a parse tree produced by GraphgifParser#argument.
    def exitArgument(self, ctx:GraphgifParser.ArgumentContext):
        pass


    # Enter a parse tree produced by GraphgifParser#path.
    def enterPath(self, ctx:GraphgifParser.PathContext):
        pass

    # Exit a parse tree produced by GraphgifParser#path.
    def exitPath(self, ctx:GraphgifParser.PathContext):
        pass



del GraphgifParser