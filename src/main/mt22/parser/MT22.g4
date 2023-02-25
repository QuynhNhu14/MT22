grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: declarations EOF ;

declarations
    :   declaration+
    ;

declaration
    :   variableDeclaration
    |   functionDeclaration
    ;

variableDeclaration
    :   (shortDeclaration | longDeclaration) Semi
    ;

shortDeclaration
    :   identifiers Colon typeName
    ;

longDeclaration
    :   Identifier Colon typeName Assign initializer
    |   Identifier Comma longDeclaration Comma initializer
    ;

initializer
    :   expression
    |   LeftBrace initializer+ RightBrace
    ;

identifiers
    :   Identifier (Comma Identifier)*
    ;

typeName
    :   atomicType
    |   Void
    |   Auto
    |   arrayType
    ;

atomicType
    :   Boolean
    |   Integer
    |   Float
    |   String
    ;

arrayType
    :   Array LeftBracket IntegerConstant (Comma IntegerConstant)* RightBracket Of atomicType
    ;

parameter
    :   Inherit? Out? Identifier Colon typeName
    ;

functionDeclaration
    :   functionPrototype blockStatement
    ;

functionPrototype
    :   Identifier Colon Function typeName LeftParen parameters RightParen (Inherit Identifier)?
    ;

parameters
    :   parameter*
    ;

blockStatement
    :   LeftBracket (statements | variableDeclaration)* RightBracket
    ;

statements
    :   statement+
    ;

statement
    :   assignmentStatement
    |   ifStatement
    |   forStatement
    |   whileStatement
    |   do_whileStatement
    |   breakStatement
    |   continueStatement
    |   returnStatement
    |   callStatement
    |   blockStatement
    ;

assignmentStatement
    : expressions Semi
    ;

ifStatement
    : If LeftParen expressions RightParen statements (Else statements)?
    ;

forStatement
    : For LeftParen identifiers RightParen
    ;

whileStatement
    :   While LeftParen expressions RightParen
    ;

do_whileStatement
    :   Do blockStatement While LeftParen expressions RightParen
    ;

breakStatement
    :   Break Semi
    ;

continueStatement
    :   Continue Semi
    ;

returnStatement
    :   Return expressions? Semi
    ;

callStatement
    :    functionCall Semi
    ;

expressions
    :   expression (Comma expression)*
    ;

expression
    :   unaryExpression Assign expression
    |   stringExpression
    ;

stringExpression
    :   relationalExpression ColonColon relationalExpression
    |   relationalExpression
    ;

relationalExpression
    :   logicalExpression (Equal | NotEqual | Less | Greater | LessEqual | GreaterEqual) logicalExpression
    |   logicalExpression
    ;

logicalExpression
    :   logicalExpression (AndAnd | OrOr) additiveExpression
    |   additiveExpression
    ;

additiveExpression
    :   additiveExpression (Plus | Minus) multiplicativeExpression
    |   multiplicativeExpression
    ;

multiplicativeExpression
    :   multiplicativeExpression (Star | Div | Mod) unaryExpression
    |   unaryExpression
    ;

unaryExpression
    :   Not unaryExpression
    | signExpression
    ;

signExpression
    :   Minus signExpression
    |   postfixExpression
    ;

postfixExpression
    :   postfixExpression LeftBracket expressions RightBracket
    |   primaryExpression
    ;

primaryExpression
    :   Literal
    |   Identifier
    |   functionCall
    |   LeftParen expressions RightParen
    ;

functionCall
    :   Identifier LeftParen expressions? RightParen
    ;





//COMMENT
BlockComment
    :   '/*' .*? '*/'
        -> skip
    ;

LineComment
    :   '//' ~[\r\n]*
        -> skip
    ;

//LITERALS
Literal
    :   (IntegerConstant (Under IntegerConstant)*
    |   FloatingConstant) {self.text=self.text.replace("_","")}
    ;

IntegerConstant
    :   DecimalConstant
    ;

fragment
DecimalConstant
    :   NonzeroDigit Digit*
    ;

fragment
NonzeroDigit
    :   [1-9]
    ;

FloatingConstant
    :   DecimalFloatingConstant
    ;

fragment
DecimalFloatingConstant
    :   FractionalConstant ExponentPart?
    |   DigitSequence ExponentPart
    ;

fragment
FractionalConstant
    :   DigitSequence? (Under DigitSequence)* '.' DigitSequence
    |   DigitSequence (Under DigitSequence)*  '.'
    ;

fragment
ExponentPart
    :   [eE] Sign? DigitSequence
    ;
fragment
Sign
    :   [+-]
    ;

DigitSequence
    :   Digit+
    ;

fragment
CChar
    :   ~['\\\r\n]
    |   EscapeSequence
    ;

fragment
EscapeSequence
    :   SimpleEscapeSequence
    ;

fragment
SimpleEscapeSequence
    :   '\\' ['"?abfnrtv\\]
    ;


StringLiteral
    :   '"' SCharSequence? '"'
    ;

fragment
SCharSequence
    :   SChar+
    ;

fragment
SChar
    :   ~["\\\r\n]
    |   EscapeSequence
    |   '\\\n'   // Added line
    |   '\\\r\n' // Added line
    ;

//BOOLEAN
Boolean: True_ | False_;

//KEYWORDS
Auto: 'auto' ;
False_: 'false';
Integer: 'integer';
While: 'while';
Of: 'of';
Break: 'break';
Float: 'float';
Return: 'return';
Void: 'void';
Inherit: 'inherit';
Boolean_: 'boolean';
For: 'for';
String: 'string';
Function: 'function';
Do: 'do';
True_: 'true';
Out: 'out';
Else: 'else';
If: 'if';
Continue: 'continue';
Array: 'array';

//OPERATORS
Plus:'+'; Minus: '-'; Star: '*'; Div: '/'; Mod: '%';
Not: '!'; AndAnd: '&&'; OrOr: '||'; Equal: '==';
NotEqual: '!='; Less: '<'; LessEqual: '<='; Greater: '>'; GreaterEqual: '>=';
ColonColon :'::';

//SEPERATORS
LeftParen : '(';
RightParen : ')';
LeftBracket : '[';
RightBracket : ']';
LeftBrace : '{';
RightBrace : '}';
Dot: '.'; Comma: ','; Semi: ';'; Colon: ':'; Assign: '=';
Under:'_';

//IDENTIFIERS
Identifier
    :   IdentifierNondigit
        (   IdentifierNondigit
        |   Digit
        )*
    ;

fragment
IdentifierNondigit
    :   Nondigit
    ;

fragment
Nondigit
    :   [a-zA-Z_]
    ;

fragment
Digit
    :   [0-9]
    ;


WS : [ \b\f\t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;