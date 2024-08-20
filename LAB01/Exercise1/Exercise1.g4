grammar Exercise1;

language : LOWERCASE (LOWERCASE | DIGIT)* ;
LOWERCASE : [a-z] ;
DIGIT : [0-9] ;
WS : [ \t\r\n]+ -> skip ;

