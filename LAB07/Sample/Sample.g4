grammar Sample;

program: expression;

expression: expression (Add | Sub) term | term;

term: term (Mul | Div | Mod) factor | factor;

factor: factor Exp atom | atom;

atom: Integer;

Add : '+';
Sub : '-';
Mul : '*';
Div : '/';
Mod : '%';
Exp : '^';

Integer: [0-9]+ ;

WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
