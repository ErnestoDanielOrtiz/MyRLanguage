// Tokens
MAIN: "main"
VAR: "var"
IF: "if"
ELSE: "else"
FOR: "for"
WHILE: "while"
INTT: "int"
FLOATT: "float"
STRINGT: "string"
BOOLEANT: "boolean"
PRINT: "print"
INPUT: "input"
FUNCION: "function"
RETURN: "return"
DECLARE: "declare"
VOID: "void"
TRUE: "true"
FALSE: "false"
AND: "and"
OR: "or"
NOT: "not"
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
ID: /[a-zA-Z_][a-zA-Z0-9_]*/
NUMERO: /\d+/
STRING: /\".*\"/
FLOAT: /\d+\.\d+/
WHITESPACE: (" " | /\t/ )+

%ignore WHITESPACE
%ignore NEW_LINE
%import common.ESCAPED_STRING  -> ACCION

start: globales main

globales: funciones globales | varglobales globales |

funciones: funcionvoid | funcion
funcionvoid: FUNCION ID np_func_id LEFTPARENTHESIS funcvars RIGHTPARENTHESIS COLON VOID bloque np_end_func
funcion: FUNCION ID np_func_id LEFTPARENTHESIS funcvars RIGHTPARENTHESIS COLON type bloquefunc np_end_func

varglobales: simpleglobal | compuestoglobal
simpleglobal: DECLARE ID COLON type EQUAL expresion SEMICOLON np_asignacion | DECLARE ID SEMICOLON type SEMICOLON
compuestoglobal: DECLARE ID LEFTBRACKET NUMERO RIGHTBRACKET SEMICOLON type EQUAL expresion SEMICOLON | DECLARE ID LEFTBRACKET NUMERO RIGHTBRACKET COLON type SEMICOLON
funcvars: ID COLON type funcvarsx |
funcvarsx: COMA funcvars |

main: MAIN LEFTPARENTHESIS RIGHTPARENTHESIS bloque end
np_main:
np_func_id:
np_end_func:

bloque: LEFTKEY bloq bloqx RIGHTKEY
bloq: estatuto | declaracion
bloqx: bloq bloqx |
bloquefunc: LEFTKEY bloq bloqx RETURN expresion SEMICOLON np_func_result RIGHTKEY
np_func_result:

estatuto: asignacion | escritura | read | llamadavoid | ciclos | condicion |returnv
returnv: RETURN expresion SEMICOLON np_func_result np_goto_end
np_goto_end:
declaraciones: declaracion declaracionesx
declaracionesx: declaraciones |
declaracion: simple | compuesta
simple: simpledeclaracion | simpleasignacion
simpledeclaracion: VAR ID np_is_var_false COLON type SEMICOLON
simpleasignacion: VAR ID np_is_var_false COLON type EQUAL expresion SEMICOLON np_asignacion_2
compuesta: compuestadeclaracion | compuestaasignacion
compuestadeclaracion: VAR ID LEFTBRACKET NUMERO RIGHTBRACKET COLON type SEMICOLON
compuestaasignacion: VAR ID LEFTBRACKET NUMERO RIGHTBRACKET COLON type EQUAL LEFTBRACKET expresionasig RIGHTBRACKET SEMICOLON
expresionasig: expresion COMA expresionasig | expresion
np_asignacion_2:
np_is_var_false:

asignacion: asignacionsimple | asignacioncompleja
asignacionsimple: ID EQUAL expresion SEMICOLON np_asignacion
np_asignacion:
//np_var:
asignacioncompleja: ID LEFTBRACKET NUMERO RIGHTBRACKET EQUAL expresion SEMICOLON np_asignacion | ID LEFTBRACKET RIGHTBRACKET EQUAL np_arr expresion SEMICOLON np_asignacion | asignacionlista
asignacionlista: ID EQUAL expresionlista SEMICOLON
expresionlista: LEFTBRACKET expresion explista RIGHTBRACKET
explista: COMA expresion explista |
np_arr:

escritura: PRINT LEFTPARENTHESIS escriturax RIGHTPARENTHESIS SEMICOLON
escriturax: ID LEFTBRACKET NUMERO RIGHTBRACKET escrituray | ID LEFTBRACKET ID RIGHTBRACKET escrituray | expresion escrituray
escrituray: np_escritura COMA escriturax | np_escritura
np_escritura:

read: INPUT LEFTPARENTHESIS ID RIGHTPARENTHESIS SEMICOLON

ciclos: ciclofor | ciclowhile

ciclofor: FOR np_for LEFTPARENTHESIS asignacionfor np_for_false contador SEMICOLON expresion RIGHTPARENTHESIS bloque np_for_2
contador: contadorsimple | contadorcomplejo
contadorsimple: ID contadorhelpersimple
contadorhelpersimple: PLUSPLUS | MINUSMINUS
contadorcomplejo: ID contadorhelpercomplejo NUMERO
contadorhelpercomplejo: MULTEQUAL | DIVEQUAL | PLUSEQUAL | MINUSEQUAL
asignacionfor: ID EQUAL expresion SEMICOLON
np_for:
np_for_2:
np_for_false:

ciclowhile: WHILE LEFTPARENTHESIS np_while_3 expresion np_while RIGHTPARENTHESIS bloque np_while_2
np_while:
np_while_2:
np_while_3:

condicion: IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS np_if bloque condicionx
condicionx: np_if_3 ELSE bloque np_if_2 | np_if_2
np_if:
np_if_2:
np_if_3:

llamadavoid: ID LEFTPARENTHESIS voidvars np_func_vars RIGHTPARENTHESIS SEMICOLON
llamadafunc: ID LEFTPARENTHESIS voidvars np_func_vars RIGHTPARENTHESIS
voidvars: exp vvars |
vvars: COMA exp vvars |
np_func_vars:

expresion: exp expresionx
expresionx: logicos exp np_logico_2 |
logicos: MORETHAN -> np_logico | LESSTHAN -> np_logico | LESSEQUAL -> np_logico | MOREEQUAL -> np_logico | NOTEQUAL -> np_logico | ISEQUAL -> np_logico | AND -> np_logico | OR -> np_logico | NOT -> np_logico
np_logico:
np_logico_2:

exp: termino expx
expx: expy exp cuadruplo_sr |
expy: ADDITION | SUBTRACTION
cuadruplo_sr:

termino: factor terminox
terminox: terminoy termino cuadruplo_md |
terminoy: MULTIPLICATION | DIVISION
cuadruplo_md:

factor: LEFTPARENTHESIS expresion RIGHTPARENTHESIS | factorx varcte | varcte
factorx: ADDITION | SUBTRACTION

varcte: id | int | boolean | llamadafunc | LEFTBRACKET exp RIGHTBRACKET | float | string | arreglo
id: ID -> guardar_id
int: NUMERO -> guardar_int
float: FLOAT -> guardar_float
string: STRING -> guardar_string
arreglo: ID LEFTBRACKET NUMERO RIGHTBRACKET | ID LEFTBRACKET ID RIGHTBRACKET

type: NUMERO | FLOATT | STRINGT | BOOLEANT
boolean: TRUE -> guardar_boolean | FALSE -> guardar_boolean

end: