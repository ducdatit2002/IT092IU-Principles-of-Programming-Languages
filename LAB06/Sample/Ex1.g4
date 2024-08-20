grammar Ex1;

program: (expression)*;

expression: Integer | Identifier;

Integer: [0-9]+ ;
Identifier: [a-z]+ ;

WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
