grammar Example;

// Define the start rule for the language
start : ID ; // The language must begin with an identifier

// Define the identifier rule
ID : [a-z][a-z0-9]* ; 

// Define a rule to skip whitespace
WS : [ \t\r\n]+ -> skip ; // Skip spaces, tabs, newlines

// Structure of *.g4 file

// Grammar Name: named at the beginning with the grammar keyword.
// Parser Rules: define the structure of the language
// Lexer Rules: define how to match specific sequences of characters in the input text
// Whitespace and Error Handling: 