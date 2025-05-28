// Generated from /Users/jakubmikolajczyk/Studia/tkik/GraphGif/parsing/grammar/Graphgif.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link GraphgifParser}.
 */
public interface GraphgifListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link GraphgifParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(GraphgifParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link GraphgifParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(GraphgifParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link GraphgifParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void enterVarDecl(GraphgifParser.VarDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link GraphgifParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void exitVarDecl(GraphgifParser.VarDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link GraphgifParser#varType}.
	 * @param ctx the parse tree
	 */
	void enterVarType(GraphgifParser.VarTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link GraphgifParser#varType}.
	 * @param ctx the parse tree
	 */
	void exitVarType(GraphgifParser.VarTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link GraphgifParser#varValue}.
	 * @param ctx the parse tree
	 */
	void enterVarValue(GraphgifParser.VarValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link GraphgifParser#varValue}.
	 * @param ctx the parse tree
	 */
	void exitVarValue(GraphgifParser.VarValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link GraphgifParser#graphDecl}.
	 * @param ctx the parse tree
	 */
	void enterGraphDecl(GraphgifParser.GraphDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link GraphgifParser#graphDecl}.
	 * @param ctx the parse tree
	 */
	void exitGraphDecl(GraphgifParser.GraphDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link GraphgifParser#globalAttrDecl}.
	 * @param ctx the parse tree
	 */
	void enterGlobalAttrDecl(GraphgifParser.GlobalAttrDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link GraphgifParser#globalAttrDecl}.
	 * @param ctx the parse tree
	 */
	void exitGlobalAttrDecl(GraphgifParser.GlobalAttrDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link GraphgifParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(GraphgifParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link GraphgifParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(GraphgifParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link GraphgifParser#nodeDecl}.
	 * @param ctx the parse tree
	 */
	void enterNodeDecl(GraphgifParser.NodeDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link GraphgifParser#nodeDecl}.
	 * @param ctx the parse tree
	 */
	void exitNodeDecl(GraphgifParser.NodeDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link GraphgifParser#edgeDecl}.
	 * @param ctx the parse tree
	 */
	void enterEdgeDecl(GraphgifParser.EdgeDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link GraphgifParser#edgeDecl}.
	 * @param ctx the parse tree
	 */
	void exitEdgeDecl(GraphgifParser.EdgeDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link GraphgifParser#edgeOp}.
	 * @param ctx the parse tree
	 */
	void enterEdgeOp(GraphgifParser.EdgeOpContext ctx);
	/**
	 * Exit a parse tree produced by {@link GraphgifParser#edgeOp}.
	 * @param ctx the parse tree
	 */
	void exitEdgeOp(GraphgifParser.EdgeOpContext ctx);
	/**
	 * Enter a parse tree produced by {@link GraphgifParser#nodeList}.
	 * @param ctx the parse tree
	 */
	void enterNodeList(GraphgifParser.NodeListContext ctx);
	/**
	 * Exit a parse tree produced by {@link GraphgifParser#nodeList}.
	 * @param ctx the parse tree
	 */
	void exitNodeList(GraphgifParser.NodeListContext ctx);
	/**
	 * Enter a parse tree produced by {@link GraphgifParser#edgeList}.
	 * @param ctx the parse tree
	 */
	void enterEdgeList(GraphgifParser.EdgeListContext ctx);
	/**
	 * Exit a parse tree produced by {@link GraphgifParser#edgeList}.
	 * @param ctx the parse tree
	 */
	void exitEdgeList(GraphgifParser.EdgeListContext ctx);
	/**
	 * Enter a parse tree produced by {@link GraphgifParser#attrList}.
	 * @param ctx the parse tree
	 */
	void enterAttrList(GraphgifParser.AttrListContext ctx);
	/**
	 * Exit a parse tree produced by {@link GraphgifParser#attrList}.
	 * @param ctx the parse tree
	 */
	void exitAttrList(GraphgifParser.AttrListContext ctx);
	/**
	 * Enter a parse tree produced by {@link GraphgifParser#attribute}.
	 * @param ctx the parse tree
	 */
	void enterAttribute(GraphgifParser.AttributeContext ctx);
	/**
	 * Exit a parse tree produced by {@link GraphgifParser#attribute}.
	 * @param ctx the parse tree
	 */
	void exitAttribute(GraphgifParser.AttributeContext ctx);
	/**
	 * Enter a parse tree produced by {@link GraphgifParser#value}.
	 * @param ctx the parse tree
	 */
	void enterValue(GraphgifParser.ValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link GraphgifParser#value}.
	 * @param ctx the parse tree
	 */
	void exitValue(GraphgifParser.ValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link GraphgifParser#nodeVarRef}.
	 * @param ctx the parse tree
	 */
	void enterNodeVarRef(GraphgifParser.NodeVarRefContext ctx);
	/**
	 * Exit a parse tree produced by {@link GraphgifParser#nodeVarRef}.
	 * @param ctx the parse tree
	 */
	void exitNodeVarRef(GraphgifParser.NodeVarRefContext ctx);
	/**
	 * Enter a parse tree produced by {@link GraphgifParser#edgeVarRef}.
	 * @param ctx the parse tree
	 */
	void enterEdgeVarRef(GraphgifParser.EdgeVarRefContext ctx);
	/**
	 * Exit a parse tree produced by {@link GraphgifParser#edgeVarRef}.
	 * @param ctx the parse tree
	 */
	void exitEdgeVarRef(GraphgifParser.EdgeVarRefContext ctx);
	/**
	 * Enter a parse tree produced by {@link GraphgifParser#attrVarRef}.
	 * @param ctx the parse tree
	 */
	void enterAttrVarRef(GraphgifParser.AttrVarRefContext ctx);
	/**
	 * Exit a parse tree produced by {@link GraphgifParser#attrVarRef}.
	 * @param ctx the parse tree
	 */
	void exitAttrVarRef(GraphgifParser.AttrVarRefContext ctx);
	/**
	 * Enter a parse tree produced by {@link GraphgifParser#command}.
	 * @param ctx the parse tree
	 */
	void enterCommand(GraphgifParser.CommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link GraphgifParser#command}.
	 * @param ctx the parse tree
	 */
	void exitCommand(GraphgifParser.CommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link GraphgifParser#argList}.
	 * @param ctx the parse tree
	 */
	void enterArgList(GraphgifParser.ArgListContext ctx);
	/**
	 * Exit a parse tree produced by {@link GraphgifParser#argList}.
	 * @param ctx the parse tree
	 */
	void exitArgList(GraphgifParser.ArgListContext ctx);
	/**
	 * Enter a parse tree produced by {@link GraphgifParser#argument}.
	 * @param ctx the parse tree
	 */
	void enterArgument(GraphgifParser.ArgumentContext ctx);
	/**
	 * Exit a parse tree produced by {@link GraphgifParser#argument}.
	 * @param ctx the parse tree
	 */
	void exitArgument(GraphgifParser.ArgumentContext ctx);
	/**
	 * Enter a parse tree produced by {@link GraphgifParser#path}.
	 * @param ctx the parse tree
	 */
	void enterPath(GraphgifParser.PathContext ctx);
	/**
	 * Exit a parse tree produced by {@link GraphgifParser#path}.
	 * @param ctx the parse tree
	 */
	void exitPath(GraphgifParser.PathContext ctx);
}