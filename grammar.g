// Tokens
%import common.CNAME
%import common.INT
%import common.FLOAT
%import common.ESCAPED_STRING
%import common.WS
%ignore WS

MAIN: "main"
VAR: "var"
IF: "if"
ELSE: "else"
FOR: "for"
WHILE: "while"
INTT: "int"
STRINGT: "string"
BOOLEANT: "boolean"
PRINT: "print"
INPUT: "input"
FUNCTION: "function"
RETURN: "return"
DECLARE: "declare"
VOID: "void"
TRUE: "true"
FALSE: "false"
COLON: ":"
SEMICOLON: ";"
COMA: ","
ADDITION: "+"
SUBTRACTION: "-"
MULTIPLICATION: "*"
DIVISION: "/"
PLUSPLUS: "++"
MINUSMINUS: "--"
PLUSEQUAL: "+="
MINUSEQUAL: "-="
MULTEQUAL: "*="
DIVEQUAL: "/="
LEFTPARENTHESIS: "("
RIGHTPARENTHESIS: ")"
LEFTBRACKET: "["
RIGHTBRACKET: "]"
LEFTKEY: "{"
RIGHTKEY: "}"
MORETHAN: ">"
MOREEQUAL: ">="
LESSTHAN: "<"
LESSEQUAL: "<="
NOTEQUAL: "!="
ISEQUAL: "=="
EQUAL: "="
NEW_LINE: /\n+/
ID: CNAME
NUMBER: INT | FLOAT
STRING: ESCAPED_STRING
FLOATT: "float"
WHITESPACE: (" " | /\t/ )+

%ignore WHITESPACE
%ignore NEW_LINE

start: globales main

globales: funciones globales | varglobales globales |
funciones: funcionvoid | funcion
funcionvoid: FUNCTION ID LEFTPARENTHESIS funcvars RIGHTPARENTHESIS COLON VOID bloque
funcion: FUNCTION ID LEFTPARENTHESIS funcvars RIGHTPARENTHESIS COLON tipo bloquefunc
varglobales: DECLARE ID EQUAL expresion SEMICOLON | DECLARE ID LEFTBRACKET INT RIGHTBRACKET EQUAL expresion SEMICOLON
funcvars: ID COLON tipo funcvarsx |
funcvarsx: COMA funcvars |
main: MAIN LEFTPARENTHESIS RIGHTPARENTHESIS bloque

bloque: LEFTKEY bloq bloqx RIGHTKEY
bloq: estatuto
bloqx: bloq bloqx |
bloquefunc: LEFTKEY bloq bloqx RETURN expresion SEMICOLON RIGHTKEY
estatuto: asignacion | escritura | read | llamadavoid | ciclos | condicion

asignacion: asignacionsimple | asignacioncompleja
asignacionsimple: ID EQUAL expresion SEMICOLON
asignacioncompleja: ID LEFTBRACKET INT RIGHTBRACKET EQUAL expresion SEMICOLON | asignacionlista
asignacionlista: ID EQUAL expresionlista SEMICOLON
expresionlista: LEFTBRACKET expresion explista RIGHTBRACKET
explista: COMA expresion explista |

escritura: PRINT LEFTPARENTHESIS escriturax RIGHTPARENTHESIS SEMICOLON
//escriturax: expresion escrituray  | STRING escrituray
escriturax: expresion escrituray
escrituray: COMA escriturax |

read: INPUT LEFTPARENTHESIS ID RIGHTPARENTHESIS SEMICOLON

ciclos: ciclofor | ciclowhile
ciclofor: FOR LEFTPARENTHESIS asignacionsimple expresion SEMICOLON contador RIGHTPARENTHESIS bloque
contador: contadorsimple | contadorcomplejo
contadorsimple: ID contadorhelpersimple
contadorhelpersimple: PLUSPLUS | MINUSMINUS
contadorcomplejo: ID contadorhelpercomplejo INT
contadorhelpercomplejo: MULTEQUAL | DIVEQUAL | PLUSEQUAL | MINUSEQUAL
ciclowhile: WHILE LEFTPARENTHESIS expresion RIGHTPARENTHESIS bloque

condicion: IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS bloque condicionx
condicionx: ELSE bloque |

llamadavoid: ID LEFTPARENTHESIS voidvars RIGHTPARENTHESIS SEMICOLON
llamadafunc: ID LEFTPARENTHESIS voidvars RIGHTPARENTHESIS
voidvars: exp vvars |
vvars: COMA exp vvars |

expresion: exp expresionx
expresionx: logicos exp |
logicos: MORETHAN | LESSTHAN | LESSEQUAL | MOREEQUAL | NOTEQUAL | ISEQUAL
exp: termino expx
expx: expy exp |
expy: ADDITION | SUBTRACTION
termino: factor terminox
terminox: terminoy termino |
terminoy: MULTIPLICATION | DIVISION
factor: LEFTPARENTHESIS expresion RIGHTPARENTHESIS | factorx varcte | varcte
factorx: ADDITION | SUBTRACTION
varcte: ID | INT | boolean | llamadafunc | LEFTBRACKET exp RIGHTBRACKET | FLOAT | STRING | arreglo
arreglo: ID LEFTBRACKET INT RIGHTBRACKET | ID LEFTBRACKET ID RIGHTBRACKET

tipo: INTT | FLOATT | STRINGT | BOOLEANT
boolean: TRUE | FALSE
// Tokens
%import common.CNAME
%import common.INT
%import common.FLOAT
%import common.ESCAPED_STRING
%import common.WS
%ignore WS

MAIN: "main"
VAR: "var"
IF: "if"
ELSE: "else"
FOR: "for"
WHILE: "while"
INTT: "int"
STRINGT: "string"
BOOLEANT: "boolean"
PRINT: "print"
INPUT: "input"
FUNCTION: "function"
RETURN: "return"
DECLARE: "declare"
VOID: "void"
TRUE: "true"
FALSE: "false"
COLON: ":"
SEMICOLON: ";"
COMA: ","
ADDITION: "+"
SUBTRACTION: "-"
MULTIPLICATION: "*"
DIVISION: "/"
PLUSPLUS: "++"
MINUSMINUS: "--"
PLUSEQUAL: "+="
MINUSEQUAL: "-="
MULTEQUAL: "*="
DIVEQUAL: "/="
LEFTPARENTHESIS: "("
RIGHTPARENTHESIS: ")"
LEFTBRACKET: "["
RIGHTBRACKET: "]"
LEFTKEY: "{"
RIGHTKEY: "}"
MORETHAN: ">"
MOREEQUAL: ">="
LESSTHAN: "<"
LESSEQUAL: "<="
NOTEQUAL: "!="
ISEQUAL: "=="
EQUAL: "="
NEW_LINE: /\n+/
ID: CNAME
NUMBER: INT | FLOAT
STRING: ESCAPED_STRING
FLOATT: "float"
WHITESPACE: (" " | /\t/ )+
%ignore WHITESPACE
%ignore NEW_LINE

start: globales main

globales: funciones globales | varglobales globales |
funciones: funcionvoid | funcion
funcionvoid: FUNCTION ID LEFTPARENTHESIS funcvars RIGHTPARENTHESIS COLON VOID bloque
funcion: FUNCTION ID LEFTPARENTHESIS funcvars RIGHTPARENTHESIS COLON tipo bloquefunc
varglobales: DECLARE ID EQUAL expresion SEMICOLON | DECLARE ID LEFTBRACKET INT RIGHTBRACKET EQUAL expresion SEMICOLON
funcvars: ID COLON tipo funcvarsx |
funcvarsx: COMA funcvars |
main: MAIN LEFTPARENTHESIS RIGHTPARENTHESIS bloque

bloque: LEFTKEY bloq bloqx RIGHTKEY
bloq: estatuto
bloqx: bloq bloqx |
bloquefunc: LEFTKEY bloq bloqx RETURN expresion SEMICOLON RIGHTKEY
estatuto: asignacion | escritura | read | llamadavoid | ciclos | condicion

asignacion: asignacionsimple | asignacioncompleja
asignacionsimple: ID EQUAL expresion SEMICOLON
asignacioncompleja: ID LEFTBRACKET INT RIGHTBRACKET EQUAL expresion SEMICOLON | asignacionlista
asignacionlista: ID EQUAL expresionlista SEMICOLON
expresionlista: LEFTBRACKET expresion explista RIGHTBRACKET
explista: COMA expresion explista |

escritura: PRINT LEFTPARENTHESIS escriturax RIGHTPARENTHESIS SEMICOLON
//escriturax: expresion escrituray  | STRING escrituray
escriturax: expresion escrituray
escrituray: COMA escriturax |

read: INPUT LEFTPARENTHESIS ID RIGHTPARENTHESIS SEMICOLON

ciclos: ciclofor | ciclowhile
ciclofor: FOR LEFTPARENTHESIS asignacionsimple expresion SEMICOLON contador RIGHTPARENTHESIS bloque
contador: contadorsimple | contadorcomplejo
contadorsimple: ID contadorhelpersimple
contadorhelpersimple: PLUSPLUS | MINUSMINUS
contadorcomplejo: ID contadorhelpercomplejo INT
contadorhelpercomplejo: MULTEQUAL | DIVEQUAL | PLUSEQUAL | MINUSEQUAL
ciclowhile: WHILE LEFTPARENTHESIS expresion RIGHTPARENTHESIS bloque

condicion: IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS bloque condicionx
condicionx: ELSE bloque |

llamadavoid: ID LEFTPARENTHESIS voidvars RIGHTPARENTHESIS SEMICOLON
llamadafunc: ID LEFTPARENTHESIS voidvars RIGHTPARENTHESIS
voidvars: exp vvars |
vvars: COMA exp vvars |

expresion: exp expresionx
expresionx: logicos exp |
logicos: MORETHAN | LESSTHAN | LESSEQUAL | MOREEQUAL | NOTEQUAL | ISEQUAL
exp: termino expx
expx: expy exp |
expy: ADDITION | SUBTRACTION
termino: factor terminox
terminox: terminoy termino |
terminoy: MULTIPLICATION | DIVISION
factor: LEFTPARENTHESIS expresion RIGHTPARENTHESIS | factorx varcte | varcte
factorx: ADDITION | SUBTRACTION
varcte: ID | INT | boolean | llamadafunc | LEFTBRACKET exp RIGHTBRACKET | FLOAT | STRING | arreglo
arreglo: ID LEFTBRACKET INT RIGHTBRACKET | ID LEFTBRACKET ID RIGHTBRACKET

tipo: INTT | FLOATT | STRINGT | BOOLEANT
boolean: TRUE | FALSE
