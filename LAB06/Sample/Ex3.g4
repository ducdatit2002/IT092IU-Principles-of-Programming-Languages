grammar Ex3;

program: expression+ ;

expression
    : expression op=('+' | '-') factor    #BinaryExpr
    | factor                              #FactorExpr
    ;

factor
    : factor op=('*' | '/') term           #BinaryFactor
    | term                                 #TermFactor
    ;

term
    : Integer                              #IntegerTerm
    | Identifier                           #IdentifierTerm
    ;

Integer: [0-9]+ ;
Identifier: [a-zA-Z_][a-zA-Z_0-9]* ;
WS: [ \t\r\n]+ -> skip;
