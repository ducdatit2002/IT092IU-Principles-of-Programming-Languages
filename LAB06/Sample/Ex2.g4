grammar Ex2;

program: (expression)*;

expression: expression '+' term | term;

term: Integer | Identifier;

Integer: [0-9]+ ;
Identifier: [a-z]+ ;

WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
