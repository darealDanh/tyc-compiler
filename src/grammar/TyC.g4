grammar TyC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

// ========== PARSER RULES ==========

program: declaration* EOF;

declaration: structDeclaration | functionDeclaration;

// Struct declaration
structDeclaration: STRUCT ID LBRACE structMemberList? RBRACE SEMI;
structMemberList: structMember+;
structMember: typ ID SEMI;

// Function declaration
functionDeclaration: (typ | /* inferred */) ID LPAREN parameterList? RPAREN blockStatement;
parameterList: parameter (COMMA parameter)*;
parameter: typ ID;

// Type specification
typ: primitiveType | ID;
primitiveType: INT | FLOAT | STRING | VOID;

// Statements
statement
    : varDeclaration
    | blockStatement
    | ifStatement
    | whileStatement
    | forStatement
    | switchStatement
    | breakStatement
    | continueStatement
    | returnStatement
    | expressionStatement
    ;

varDeclaration: (AUTO | typ) ID (ASSIGN expression)? SEMI;

blockStatement: LBRACE (varDeclaration | statement)* RBRACE;

ifStatement: IF LPAREN expression RPAREN statement (ELSE statement)?;

whileStatement: WHILE LPAREN expression RPAREN statement;

forStatement: FOR LPAREN forInit? SEMI expression? SEMI forUpdate? RPAREN statement;
forInit: forVarDeclaration | expression;
forVarDeclaration: (AUTO | typ) ID (ASSIGN expression)?;
forUpdate: expression;

switchStatement: SWITCH LPAREN expression RPAREN LBRACE caseClause* RBRACE;
caseClause: (CASE expression COLON statement*) | (DEFAULT COLON statement*);

breakStatement: BREAK SEMI;


expression: assignmentExpression;



assignmentExpression: logicalOrExpression (ASSIGN assignmentExpression)?;

continueStatement: CONTINUE SEMI;
returnStatement: RETURN expression? SEMI;
expressionStatement: expression SEMI;

logicalOrExpression: logicalAndExpression (OR logicalAndExpression)*;

logicalAndExpression: equalityExpression (AND equalityExpression)*;

equalityExpression: relationalExpression ((EQUAL | NOTEQUAL) relationalExpression)*;

unaryExpression
    : PLUS unaryExpression
    | MINUS unaryExpression
    | NOT unaryExpression
    | INCR unaryExpression
    | DECR unaryExpression
    | postfixExpression
    ;

postfixExpression
    : primaryExpression (postfixOp)*
    ;

postfixOp
    : DOT ID                      // member access
    | INCR                        // postfix increment
    | DECR                        // postfix decrement
    | LPAREN argumentList? RPAREN // function call
    ;

primaryExpression
    : ID
    | INTLIT
    | FLOATLIT
    | STRINGLIT
    | LPAREN expression RPAREN
    | structLiteral
    ;

structLiteral: LBRACE argumentList? RBRACE;

relationalExpression: additiveExpression ((LT | GT | LTE | GTE) additiveExpression)*;

additiveExpression: multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*;

multiplicativeExpression: unaryExpression ((MULT | DIV | MOD) unaryExpression)*;


argumentList: expression (COMMA expression)*;


AUTO: 'auto';
BREAK: 'break';
CASE: 'case';
CONTINUE: 'continue';
DEFAULT: 'default';
ELSE: 'else';
FLOAT: 'float';
FOR: 'for';
IF: 'if';
INT: 'int';
RETURN: 'return';
STRING: 'string';
STRUCT: 'struct';
SWITCH: 'switch';
VOID: 'void';
WHILE: 'while';

// Operators
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%';
EQUAL: '==';
NOTEQUAL: '!=';
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';
OR: '||';
AND: '&&';
NOT: '!';
INCR: '++';
DECR: '--';
ASSIGN: '=';
DOT: '.';

// Separators
LBRACE: '{';
RBRACE: '}';
LPAREN: '(';
RPAREN: ')';
SEMI: ';';
COMMA: ',';
COLON: ':';

// Identifiers (after keywords)
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Literals
INTLIT: [0-9]+;

FLOATLIT
    : [0-9]+ '.' [0-9]* ([eE][+\-]?[0-9]+)?  // 123.456, 123., 123.456e10
    | '.' [0-9]+ ([eE][+\-]?[0-9]+)?          // .456, .456e10
    | [0-9]+ [eE][+\-]?[0-9]+                 // 123e10
    ;

STRINGLIT: '"' STR_CHAR* '"' {self.text = self.text[1:-1]};

fragment STR_CHAR
    : ~[\r\n"\\]           // any character except newline, quote, backslash
    | '\\' [bfrnt"\\]      // valid escape sequences
    ;

// Comments
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;

// Whitespace
WS: [ \t\r\n\f]+ -> skip;

// Error tokens (must be at the end)
ILLEGAL_ESCAPE: '"' STR_CHAR* '\\' ~[bfrnt"\\] {self.text = self.text[1:]};

UNCLOSE_STRING: '"' STR_CHAR* ([\r\n] | EOF) {self.text = self.text[1:]};

ERROR_CHAR: . {self.text = self.text};
