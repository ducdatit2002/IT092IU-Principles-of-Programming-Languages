grammar Sample;

program: (expression )*;
expression: expression (Add | Sub) factor | factor;
factor: factor (Mul | Div) term | term;
Add : '+';
Sub : '-';
Mul : '*';
Div : '/';
term: Integer | Identifier ;

Integer: [0-9]+ ;
Identifier: [a-zA-Z]+ ;  // Added explicit definition for Identifier

WS: [ \t\n\r]+ -> skip ;  // Skip whitespace