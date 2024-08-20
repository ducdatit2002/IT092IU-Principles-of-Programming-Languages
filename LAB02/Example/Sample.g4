grammar Sample;

start: expression* ;

expression: term;

term: Integer| Id;

Integer: [0-9]+ ;
Id: [a-zA-Z_][a-zA-Z_0-9]* ;

WS : [ \t\r\n]+ -> skip ; // Skip spaces, tabs, and newlines
