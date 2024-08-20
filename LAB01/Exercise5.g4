grammar Ex5Lexer;

start: expr EOF;

expr: term ( (PLUS | MINUS) term )* ;
term: factor ( (MULT | DIV) factor )* ;
factor: NUMBER | LPAREN expr RPAREN ;

NUMBER: DIGIT+;
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
LPAREN: '(';
RPAREN: ')';

fragment DIGIT: [0-9];

WS: [ \t\r\n]+ -> skip;