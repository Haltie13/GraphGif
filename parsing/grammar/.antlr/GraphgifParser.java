// Generated from /Users/jakubmikolajczyk/Studia/tkik/GraphGif/parsing/grammar/Graphgif.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class GraphgifParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		ID=25, NUMBER=26, STRING=27, WS=28, COMMENT=29;
	public static final int
		RULE_program = 0, RULE_varDecl = 1, RULE_varType = 2, RULE_varValue = 3, 
		RULE_graphDecl = 4, RULE_globalAttrDecl = 5, RULE_statement = 6, RULE_nodeDecl = 7, 
		RULE_edgeDecl = 8, RULE_edgeOp = 9, RULE_nodeList = 10, RULE_edgeList = 11, 
		RULE_attrList = 12, RULE_attribute = 13, RULE_value = 14, RULE_nodeVarRef = 15, 
		RULE_edgeVarRef = 16, RULE_attrVarRef = 17, RULE_command = 18, RULE_argList = 19, 
		RULE_argument = 20, RULE_path = 21;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "varDecl", "varType", "varValue", "graphDecl", "globalAttrDecl", 
			"statement", "nodeDecl", "edgeDecl", "edgeOp", "nodeList", "edgeList", 
			"attrList", "attribute", "value", "nodeVarRef", "edgeVarRef", "attrVarRef", 
			"command", "argList", "argument", "path"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'var'", "'='", "'node'", "'edge'", "'attributes'", "'directed'", 
			"'undirected'", "'graph'", "'{'", "'}'", "'--'", "'->'", "'<-'", "','", 
			"'['", "']'", "':'", "'$'", "'run'", "'with'", "'('", "')'", "'.'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, "ID", "NUMBER", "STRING", "WS", "COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Graphgif.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public GraphgifParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(GraphgifParser.EOF, 0); }
		public List<VarDeclContext> varDecl() {
			return getRuleContexts(VarDeclContext.class);
		}
		public VarDeclContext varDecl(int i) {
			return getRuleContext(VarDeclContext.class,i);
		}
		public List<GraphDeclContext> graphDecl() {
			return getRuleContexts(GraphDeclContext.class);
		}
		public GraphDeclContext graphDecl(int i) {
			return getRuleContext(GraphDeclContext.class,i);
		}
		public List<CommandContext> command() {
			return getRuleContexts(CommandContext.class);
		}
		public CommandContext command(int i) {
			return getRuleContext(CommandContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(49);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__1) {
				{
				{
				setState(44);
				varDecl();
				setState(45);
				match(T__0);
				}
				}
				setState(51);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(57);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6 || _la==T__7) {
				{
				{
				setState(52);
				graphDecl();
				setState(53);
				match(T__0);
				}
				}
				setState(59);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(65);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__19) {
				{
				{
				setState(60);
				command();
				setState(61);
				match(T__0);
				}
				}
				setState(67);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(68);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarDeclContext extends ParserRuleContext {
		public VarTypeContext varType() {
			return getRuleContext(VarTypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(GraphgifParser.ID, 0); }
		public VarValueContext varValue() {
			return getRuleContext(VarValueContext.class,0);
		}
		public VarDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).enterVarDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).exitVarDecl(this);
		}
	}

	public final VarDeclContext varDecl() throws RecognitionException {
		VarDeclContext _localctx = new VarDeclContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_varDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(70);
			match(T__1);
			setState(71);
			varType();
			setState(72);
			match(ID);
			setState(73);
			match(T__2);
			setState(74);
			varValue();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarTypeContext extends ParserRuleContext {
		public VarTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varType; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).enterVarType(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).exitVarType(this);
		}
	}

	public final VarTypeContext varType() throws RecognitionException {
		VarTypeContext _localctx = new VarTypeContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_varType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 112L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarValueContext extends ParserRuleContext {
		public NodeVarRefContext nodeVarRef() {
			return getRuleContext(NodeVarRefContext.class,0);
		}
		public EdgeVarRefContext edgeVarRef() {
			return getRuleContext(EdgeVarRefContext.class,0);
		}
		public AttrVarRefContext attrVarRef() {
			return getRuleContext(AttrVarRefContext.class,0);
		}
		public NodeListContext nodeList() {
			return getRuleContext(NodeListContext.class,0);
		}
		public EdgeListContext edgeList() {
			return getRuleContext(EdgeListContext.class,0);
		}
		public AttrListContext attrList() {
			return getRuleContext(AttrListContext.class,0);
		}
		public VarValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varValue; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).enterVarValue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).exitVarValue(this);
		}
	}

	public final VarValueContext varValue() throws RecognitionException {
		VarValueContext _localctx = new VarValueContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_varValue);
		try {
			setState(84);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(78);
				nodeVarRef();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(79);
				edgeVarRef();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(80);
				attrVarRef();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(81);
				nodeList();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(82);
				edgeList();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(83);
				attrList();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GraphDeclContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(GraphgifParser.ID, 0); }
		public List<GlobalAttrDeclContext> globalAttrDecl() {
			return getRuleContexts(GlobalAttrDeclContext.class);
		}
		public GlobalAttrDeclContext globalAttrDecl(int i) {
			return getRuleContext(GlobalAttrDeclContext.class,i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public GraphDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_graphDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).enterGraphDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).exitGraphDecl(this);
		}
	}

	public final GraphDeclContext graphDecl() throws RecognitionException {
		GraphDeclContext _localctx = new GraphDeclContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_graphDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(86);
			_la = _input.LA(1);
			if ( !(_la==T__6 || _la==T__7) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			{
			setState(87);
			match(T__8);
			}
			setState(88);
			match(ID);
			setState(89);
			match(T__9);
			setState(95);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 560L) != 0)) {
				{
				{
				setState(90);
				globalAttrDecl();
				setState(91);
				match(T__0);
				}
				}
				setState(97);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(103);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__18 || _la==ID) {
				{
				{
				setState(98);
				statement();
				setState(99);
				match(T__0);
				}
				}
				setState(105);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(106);
			match(T__10);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GlobalAttrDeclContext extends ParserRuleContext {
		public AttrListContext attrList() {
			return getRuleContext(AttrListContext.class,0);
		}
		public AttrVarRefContext attrVarRef() {
			return getRuleContext(AttrVarRefContext.class,0);
		}
		public GlobalAttrDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_globalAttrDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).enterGlobalAttrDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).exitGlobalAttrDecl(this);
		}
	}

	public final GlobalAttrDeclContext globalAttrDecl() throws RecognitionException {
		GlobalAttrDeclContext _localctx = new GlobalAttrDeclContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_globalAttrDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 560L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(111);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__15:
				{
				setState(109);
				attrList();
				}
				break;
			case T__18:
				{
				setState(110);
				attrVarRef();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public NodeDeclContext nodeDecl() {
			return getRuleContext(NodeDeclContext.class,0);
		}
		public EdgeDeclContext edgeDecl() {
			return getRuleContext(EdgeDeclContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).exitStatement(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_statement);
		try {
			setState(115);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(113);
				nodeDecl();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(114);
				edgeDecl();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NodeDeclContext extends ParserRuleContext {
		public NodeListContext nodeList() {
			return getRuleContext(NodeListContext.class,0);
		}
		public NodeVarRefContext nodeVarRef() {
			return getRuleContext(NodeVarRefContext.class,0);
		}
		public AttrListContext attrList() {
			return getRuleContext(AttrListContext.class,0);
		}
		public AttrVarRefContext attrVarRef() {
			return getRuleContext(AttrVarRefContext.class,0);
		}
		public NodeDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_nodeDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).enterNodeDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).exitNodeDecl(this);
		}
	}

	public final NodeDeclContext nodeDecl() throws RecognitionException {
		NodeDeclContext _localctx = new NodeDeclContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_nodeDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(119);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				{
				setState(117);
				nodeList();
				}
				break;
			case T__18:
				{
				setState(118);
				nodeVarRef();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(123);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__15:
				{
				setState(121);
				attrList();
				}
				break;
			case T__18:
				{
				setState(122);
				attrVarRef();
				}
				break;
			case T__0:
				break;
			default:
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EdgeDeclContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(GraphgifParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(GraphgifParser.ID, i);
		}
		public EdgeOpContext edgeOp() {
			return getRuleContext(EdgeOpContext.class,0);
		}
		public AttrListContext attrList() {
			return getRuleContext(AttrListContext.class,0);
		}
		public AttrVarRefContext attrVarRef() {
			return getRuleContext(AttrVarRefContext.class,0);
		}
		public EdgeDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_edgeDecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).enterEdgeDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).exitEdgeDecl(this);
		}
	}

	public final EdgeDeclContext edgeDecl() throws RecognitionException {
		EdgeDeclContext _localctx = new EdgeDeclContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_edgeDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(125);
			match(ID);
			setState(126);
			edgeOp();
			setState(127);
			match(ID);
			setState(130);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__15:
				{
				setState(128);
				attrList();
				}
				break;
			case T__18:
				{
				setState(129);
				attrVarRef();
				}
				break;
			case T__0:
			case T__14:
				break;
			default:
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EdgeOpContext extends ParserRuleContext {
		public EdgeOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_edgeOp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).enterEdgeOp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).exitEdgeOp(this);
		}
	}

	public final EdgeOpContext edgeOp() throws RecognitionException {
		EdgeOpContext _localctx = new EdgeOpContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_edgeOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(132);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 28672L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NodeListContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(GraphgifParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(GraphgifParser.ID, i);
		}
		public NodeListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_nodeList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).enterNodeList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).exitNodeList(this);
		}
	}

	public final NodeListContext nodeList() throws RecognitionException {
		NodeListContext _localctx = new NodeListContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_nodeList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(134);
			match(ID);
			setState(139);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__14) {
				{
				{
				setState(135);
				match(T__14);
				setState(136);
				match(ID);
				}
				}
				setState(141);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EdgeListContext extends ParserRuleContext {
		public List<EdgeDeclContext> edgeDecl() {
			return getRuleContexts(EdgeDeclContext.class);
		}
		public EdgeDeclContext edgeDecl(int i) {
			return getRuleContext(EdgeDeclContext.class,i);
		}
		public EdgeListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_edgeList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).enterEdgeList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).exitEdgeList(this);
		}
	}

	public final EdgeListContext edgeList() throws RecognitionException {
		EdgeListContext _localctx = new EdgeListContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_edgeList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(142);
			edgeDecl();
			setState(147);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__14) {
				{
				{
				setState(143);
				match(T__14);
				setState(144);
				edgeDecl();
				}
				}
				setState(149);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AttrListContext extends ParserRuleContext {
		public List<AttributeContext> attribute() {
			return getRuleContexts(AttributeContext.class);
		}
		public AttributeContext attribute(int i) {
			return getRuleContext(AttributeContext.class,i);
		}
		public AttrListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attrList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).enterAttrList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).exitAttrList(this);
		}
	}

	public final AttrListContext attrList() throws RecognitionException {
		AttrListContext _localctx = new AttrListContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_attrList);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(150);
			match(T__15);
			setState(162);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(151);
				attribute();
				setState(156);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(152);
						match(T__14);
						setState(153);
						attribute();
						}
						} 
					}
					setState(158);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
				}
				setState(160);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__14) {
					{
					setState(159);
					match(T__14);
					}
				}

				}
			}

			setState(164);
			match(T__16);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AttributeContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(GraphgifParser.ID, 0); }
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public AttributeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attribute; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).enterAttribute(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).exitAttribute(this);
		}
	}

	public final AttributeContext attribute() throws RecognitionException {
		AttributeContext _localctx = new AttributeContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_attribute);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(166);
			match(ID);
			setState(167);
			_la = _input.LA(1);
			if ( !(_la==T__2 || _la==T__17) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(168);
			value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ValueContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(GraphgifParser.ID, 0); }
		public TerminalNode NUMBER() { return getToken(GraphgifParser.NUMBER, 0); }
		public TerminalNode STRING() { return getToken(GraphgifParser.STRING, 0); }
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).enterValue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).exitValue(this);
		}
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_value);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(170);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 234881024L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NodeVarRefContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(GraphgifParser.ID, 0); }
		public NodeVarRefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_nodeVarRef; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).enterNodeVarRef(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).exitNodeVarRef(this);
		}
	}

	public final NodeVarRefContext nodeVarRef() throws RecognitionException {
		NodeVarRefContext _localctx = new NodeVarRefContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_nodeVarRef);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(172);
			match(T__18);
			setState(173);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EdgeVarRefContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(GraphgifParser.ID, 0); }
		public EdgeVarRefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_edgeVarRef; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).enterEdgeVarRef(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).exitEdgeVarRef(this);
		}
	}

	public final EdgeVarRefContext edgeVarRef() throws RecognitionException {
		EdgeVarRefContext _localctx = new EdgeVarRefContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_edgeVarRef);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(175);
			match(T__18);
			setState(176);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AttrVarRefContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(GraphgifParser.ID, 0); }
		public AttrVarRefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attrVarRef; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).enterAttrVarRef(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).exitAttrVarRef(this);
		}
	}

	public final AttrVarRefContext attrVarRef() throws RecognitionException {
		AttrVarRefContext _localctx = new AttrVarRefContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_attrVarRef);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(178);
			match(T__18);
			setState(179);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CommandContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(GraphgifParser.ID, 0); }
		public ArgListContext argList() {
			return getRuleContext(ArgListContext.class,0);
		}
		public CommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_command; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).enterCommand(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).exitCommand(this);
		}
	}

	public final CommandContext command() throws RecognitionException {
		CommandContext _localctx = new CommandContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_command);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(181);
			match(T__19);
			setState(182);
			match(ID);
			setState(183);
			match(T__20);
			setState(184);
			match(T__21);
			setState(186);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(185);
				argList();
				}
			}

			setState(188);
			match(T__22);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgListContext extends ParserRuleContext {
		public List<ArgumentContext> argument() {
			return getRuleContexts(ArgumentContext.class);
		}
		public ArgumentContext argument(int i) {
			return getRuleContext(ArgumentContext.class,i);
		}
		public ArgListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).enterArgList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).exitArgList(this);
		}
	}

	public final ArgListContext argList() throws RecognitionException {
		ArgListContext _localctx = new ArgListContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_argList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(190);
			argument();
			setState(195);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__14) {
				{
				{
				setState(191);
				match(T__14);
				setState(192);
				argument();
				}
				}
				setState(197);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgumentContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(GraphgifParser.ID, 0); }
		public PathContext path() {
			return getRuleContext(PathContext.class,0);
		}
		public ArgumentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argument; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).enterArgument(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).exitArgument(this);
		}
	}

	public final ArgumentContext argument() throws RecognitionException {
		ArgumentContext _localctx = new ArgumentContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_argument);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(198);
			match(ID);
			setState(199);
			_la = _input.LA(1);
			if ( !(_la==T__2 || _la==T__17) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(200);
			path();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PathContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(GraphgifParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(GraphgifParser.ID, i);
		}
		public PathContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_path; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).enterPath(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof GraphgifListener ) ((GraphgifListener)listener).exitPath(this);
		}
	}

	public final PathContext path() throws RecognitionException {
		PathContext _localctx = new PathContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_path);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(202);
			match(ID);
			setState(207);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__23) {
				{
				{
				setState(203);
				match(T__23);
				setState(204);
				match(ID);
				}
				}
				setState(209);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u001d\u00d3\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007"+
		"\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007"+
		"\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007"+
		"\u0015\u0001\u0000\u0001\u0000\u0001\u0000\u0005\u00000\b\u0000\n\u0000"+
		"\f\u00003\t\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0005\u00008\b\u0000"+
		"\n\u0000\f\u0000;\t\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0005\u0000"+
		"@\b\u0000\n\u0000\f\u0000C\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0003\u0003U\b\u0003\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004^\b\u0004"+
		"\n\u0004\f\u0004a\t\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004"+
		"f\b\u0004\n\u0004\f\u0004i\t\u0004\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0003\u0005p\b\u0005\u0001\u0006\u0001\u0006"+
		"\u0003\u0006t\b\u0006\u0001\u0007\u0001\u0007\u0003\u0007x\b\u0007\u0001"+
		"\u0007\u0001\u0007\u0003\u0007|\b\u0007\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0003\b\u0083\b\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0005"+
		"\n\u008a\b\n\n\n\f\n\u008d\t\n\u0001\u000b\u0001\u000b\u0001\u000b\u0005"+
		"\u000b\u0092\b\u000b\n\u000b\f\u000b\u0095\t\u000b\u0001\f\u0001\f\u0001"+
		"\f\u0001\f\u0005\f\u009b\b\f\n\f\f\f\u009e\t\f\u0001\f\u0003\f\u00a1\b"+
		"\f\u0003\f\u00a3\b\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0003\u0012\u00bb\b\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0005\u0013\u00c2"+
		"\b\u0013\n\u0013\f\u0013\u00c5\t\u0013\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0005\u0015\u00ce\b\u0015"+
		"\n\u0015\f\u0015\u00d1\t\u0015\u0001\u0015\u0000\u0000\u0016\u0000\u0002"+
		"\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e"+
		" \"$&(*\u0000\u0006\u0001\u0000\u0004\u0006\u0001\u0000\u0007\b\u0002"+
		"\u0000\u0004\u0005\t\t\u0001\u0000\f\u000e\u0002\u0000\u0003\u0003\u0012"+
		"\u0012\u0001\u0000\u0019\u001b\u00d5\u00001\u0001\u0000\u0000\u0000\u0002"+
		"F\u0001\u0000\u0000\u0000\u0004L\u0001\u0000\u0000\u0000\u0006T\u0001"+
		"\u0000\u0000\u0000\bV\u0001\u0000\u0000\u0000\nl\u0001\u0000\u0000\u0000"+
		"\fs\u0001\u0000\u0000\u0000\u000ew\u0001\u0000\u0000\u0000\u0010}\u0001"+
		"\u0000\u0000\u0000\u0012\u0084\u0001\u0000\u0000\u0000\u0014\u0086\u0001"+
		"\u0000\u0000\u0000\u0016\u008e\u0001\u0000\u0000\u0000\u0018\u0096\u0001"+
		"\u0000\u0000\u0000\u001a\u00a6\u0001\u0000\u0000\u0000\u001c\u00aa\u0001"+
		"\u0000\u0000\u0000\u001e\u00ac\u0001\u0000\u0000\u0000 \u00af\u0001\u0000"+
		"\u0000\u0000\"\u00b2\u0001\u0000\u0000\u0000$\u00b5\u0001\u0000\u0000"+
		"\u0000&\u00be\u0001\u0000\u0000\u0000(\u00c6\u0001\u0000\u0000\u0000*"+
		"\u00ca\u0001\u0000\u0000\u0000,-\u0003\u0002\u0001\u0000-.\u0005\u0001"+
		"\u0000\u0000.0\u0001\u0000\u0000\u0000/,\u0001\u0000\u0000\u000003\u0001"+
		"\u0000\u0000\u00001/\u0001\u0000\u0000\u000012\u0001\u0000\u0000\u0000"+
		"29\u0001\u0000\u0000\u000031\u0001\u0000\u0000\u000045\u0003\b\u0004\u0000"+
		"56\u0005\u0001\u0000\u000068\u0001\u0000\u0000\u000074\u0001\u0000\u0000"+
		"\u00008;\u0001\u0000\u0000\u000097\u0001\u0000\u0000\u00009:\u0001\u0000"+
		"\u0000\u0000:A\u0001\u0000\u0000\u0000;9\u0001\u0000\u0000\u0000<=\u0003"+
		"$\u0012\u0000=>\u0005\u0001\u0000\u0000>@\u0001\u0000\u0000\u0000?<\u0001"+
		"\u0000\u0000\u0000@C\u0001\u0000\u0000\u0000A?\u0001\u0000\u0000\u0000"+
		"AB\u0001\u0000\u0000\u0000BD\u0001\u0000\u0000\u0000CA\u0001\u0000\u0000"+
		"\u0000DE\u0005\u0000\u0000\u0001E\u0001\u0001\u0000\u0000\u0000FG\u0005"+
		"\u0002\u0000\u0000GH\u0003\u0004\u0002\u0000HI\u0005\u0019\u0000\u0000"+
		"IJ\u0005\u0003\u0000\u0000JK\u0003\u0006\u0003\u0000K\u0003\u0001\u0000"+
		"\u0000\u0000LM\u0007\u0000\u0000\u0000M\u0005\u0001\u0000\u0000\u0000"+
		"NU\u0003\u001e\u000f\u0000OU\u0003 \u0010\u0000PU\u0003\"\u0011\u0000"+
		"QU\u0003\u0014\n\u0000RU\u0003\u0016\u000b\u0000SU\u0003\u0018\f\u0000"+
		"TN\u0001\u0000\u0000\u0000TO\u0001\u0000\u0000\u0000TP\u0001\u0000\u0000"+
		"\u0000TQ\u0001\u0000\u0000\u0000TR\u0001\u0000\u0000\u0000TS\u0001\u0000"+
		"\u0000\u0000U\u0007\u0001\u0000\u0000\u0000VW\u0007\u0001\u0000\u0000"+
		"WX\u0005\t\u0000\u0000XY\u0005\u0019\u0000\u0000Y_\u0005\n\u0000\u0000"+
		"Z[\u0003\n\u0005\u0000[\\\u0005\u0001\u0000\u0000\\^\u0001\u0000\u0000"+
		"\u0000]Z\u0001\u0000\u0000\u0000^a\u0001\u0000\u0000\u0000_]\u0001\u0000"+
		"\u0000\u0000_`\u0001\u0000\u0000\u0000`g\u0001\u0000\u0000\u0000a_\u0001"+
		"\u0000\u0000\u0000bc\u0003\f\u0006\u0000cd\u0005\u0001\u0000\u0000df\u0001"+
		"\u0000\u0000\u0000eb\u0001\u0000\u0000\u0000fi\u0001\u0000\u0000\u0000"+
		"ge\u0001\u0000\u0000\u0000gh\u0001\u0000\u0000\u0000hj\u0001\u0000\u0000"+
		"\u0000ig\u0001\u0000\u0000\u0000jk\u0005\u000b\u0000\u0000k\t\u0001\u0000"+
		"\u0000\u0000lo\u0007\u0002\u0000\u0000mp\u0003\u0018\f\u0000np\u0003\""+
		"\u0011\u0000om\u0001\u0000\u0000\u0000on\u0001\u0000\u0000\u0000p\u000b"+
		"\u0001\u0000\u0000\u0000qt\u0003\u000e\u0007\u0000rt\u0003\u0010\b\u0000"+
		"sq\u0001\u0000\u0000\u0000sr\u0001\u0000\u0000\u0000t\r\u0001\u0000\u0000"+
		"\u0000ux\u0003\u0014\n\u0000vx\u0003\u001e\u000f\u0000wu\u0001\u0000\u0000"+
		"\u0000wv\u0001\u0000\u0000\u0000x{\u0001\u0000\u0000\u0000y|\u0003\u0018"+
		"\f\u0000z|\u0003\"\u0011\u0000{y\u0001\u0000\u0000\u0000{z\u0001\u0000"+
		"\u0000\u0000{|\u0001\u0000\u0000\u0000|\u000f\u0001\u0000\u0000\u0000"+
		"}~\u0005\u0019\u0000\u0000~\u007f\u0003\u0012\t\u0000\u007f\u0082\u0005"+
		"\u0019\u0000\u0000\u0080\u0083\u0003\u0018\f\u0000\u0081\u0083\u0003\""+
		"\u0011\u0000\u0082\u0080\u0001\u0000\u0000\u0000\u0082\u0081\u0001\u0000"+
		"\u0000\u0000\u0082\u0083\u0001\u0000\u0000\u0000\u0083\u0011\u0001\u0000"+
		"\u0000\u0000\u0084\u0085\u0007\u0003\u0000\u0000\u0085\u0013\u0001\u0000"+
		"\u0000\u0000\u0086\u008b\u0005\u0019\u0000\u0000\u0087\u0088\u0005\u000f"+
		"\u0000\u0000\u0088\u008a\u0005\u0019\u0000\u0000\u0089\u0087\u0001\u0000"+
		"\u0000\u0000\u008a\u008d\u0001\u0000\u0000\u0000\u008b\u0089\u0001\u0000"+
		"\u0000\u0000\u008b\u008c\u0001\u0000\u0000\u0000\u008c\u0015\u0001\u0000"+
		"\u0000\u0000\u008d\u008b\u0001\u0000\u0000\u0000\u008e\u0093\u0003\u0010"+
		"\b\u0000\u008f\u0090\u0005\u000f\u0000\u0000\u0090\u0092\u0003\u0010\b"+
		"\u0000\u0091\u008f\u0001\u0000\u0000\u0000\u0092\u0095\u0001\u0000\u0000"+
		"\u0000\u0093\u0091\u0001\u0000\u0000\u0000\u0093\u0094\u0001\u0000\u0000"+
		"\u0000\u0094\u0017\u0001\u0000\u0000\u0000\u0095\u0093\u0001\u0000\u0000"+
		"\u0000\u0096\u00a2\u0005\u0010\u0000\u0000\u0097\u009c\u0003\u001a\r\u0000"+
		"\u0098\u0099\u0005\u000f\u0000\u0000\u0099\u009b\u0003\u001a\r\u0000\u009a"+
		"\u0098\u0001\u0000\u0000\u0000\u009b\u009e\u0001\u0000\u0000\u0000\u009c"+
		"\u009a\u0001\u0000\u0000\u0000\u009c\u009d\u0001\u0000\u0000\u0000\u009d"+
		"\u00a0\u0001\u0000\u0000\u0000\u009e\u009c\u0001\u0000\u0000\u0000\u009f"+
		"\u00a1\u0005\u000f\u0000\u0000\u00a0\u009f\u0001\u0000\u0000\u0000\u00a0"+
		"\u00a1\u0001\u0000\u0000\u0000\u00a1\u00a3\u0001\u0000\u0000\u0000\u00a2"+
		"\u0097\u0001\u0000\u0000\u0000\u00a2\u00a3\u0001\u0000\u0000\u0000\u00a3"+
		"\u00a4\u0001\u0000\u0000\u0000\u00a4\u00a5\u0005\u0011\u0000\u0000\u00a5"+
		"\u0019\u0001\u0000\u0000\u0000\u00a6\u00a7\u0005\u0019\u0000\u0000\u00a7"+
		"\u00a8\u0007\u0004\u0000\u0000\u00a8\u00a9\u0003\u001c\u000e\u0000\u00a9"+
		"\u001b\u0001\u0000\u0000\u0000\u00aa\u00ab\u0007\u0005\u0000\u0000\u00ab"+
		"\u001d\u0001\u0000\u0000\u0000\u00ac\u00ad\u0005\u0013\u0000\u0000\u00ad"+
		"\u00ae\u0005\u0019\u0000\u0000\u00ae\u001f\u0001\u0000\u0000\u0000\u00af"+
		"\u00b0\u0005\u0013\u0000\u0000\u00b0\u00b1\u0005\u0019\u0000\u0000\u00b1"+
		"!\u0001\u0000\u0000\u0000\u00b2\u00b3\u0005\u0013\u0000\u0000\u00b3\u00b4"+
		"\u0005\u0019\u0000\u0000\u00b4#\u0001\u0000\u0000\u0000\u00b5\u00b6\u0005"+
		"\u0014\u0000\u0000\u00b6\u00b7\u0005\u0019\u0000\u0000\u00b7\u00b8\u0005"+
		"\u0015\u0000\u0000\u00b8\u00ba\u0005\u0016\u0000\u0000\u00b9\u00bb\u0003"+
		"&\u0013\u0000\u00ba\u00b9\u0001\u0000\u0000\u0000\u00ba\u00bb\u0001\u0000"+
		"\u0000\u0000\u00bb\u00bc\u0001\u0000\u0000\u0000\u00bc\u00bd\u0005\u0017"+
		"\u0000\u0000\u00bd%\u0001\u0000\u0000\u0000\u00be\u00c3\u0003(\u0014\u0000"+
		"\u00bf\u00c0\u0005\u000f\u0000\u0000\u00c0\u00c2\u0003(\u0014\u0000\u00c1"+
		"\u00bf\u0001\u0000\u0000\u0000\u00c2\u00c5\u0001\u0000\u0000\u0000\u00c3"+
		"\u00c1\u0001\u0000\u0000\u0000\u00c3\u00c4\u0001\u0000\u0000\u0000\u00c4"+
		"\'\u0001\u0000\u0000\u0000\u00c5\u00c3\u0001\u0000\u0000\u0000\u00c6\u00c7"+
		"\u0005\u0019\u0000\u0000\u00c7\u00c8\u0007\u0004\u0000\u0000\u00c8\u00c9"+
		"\u0003*\u0015\u0000\u00c9)\u0001\u0000\u0000\u0000\u00ca\u00cf\u0005\u0019"+
		"\u0000\u0000\u00cb\u00cc\u0005\u0018\u0000\u0000\u00cc\u00ce\u0005\u0019"+
		"\u0000\u0000\u00cd\u00cb\u0001\u0000\u0000\u0000\u00ce\u00d1\u0001\u0000"+
		"\u0000\u0000\u00cf\u00cd\u0001\u0000\u0000\u0000\u00cf\u00d0\u0001\u0000"+
		"\u0000\u0000\u00d0+\u0001\u0000\u0000\u0000\u00d1\u00cf\u0001\u0000\u0000"+
		"\u0000\u001319AT_gosw{\u0082\u008b\u0093\u009c\u00a0\u00a2\u00ba\u00c3"+
		"\u00cf";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}