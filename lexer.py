# Palavras reservadas

reserved_words = {
  'boolean' : 'BOOLEAN',
  'class' : 'CLASS',
  'extends' : 'EXTENDS',
  'public' : 'PUBLIC',
  'static' : 'STATIC',
  'void' : 'VOID',
  'main' : 'MAIN',
  'String' : 'STRING',
  'return' : 'RETURN',
  'int' : 'INT',
  'if' : 'IF',
  'else' : 'ELSE',
  'while' : 'WHILE',
  'System.out.println' : 'PRINTLN',
  'length' : 'LENGTH',
  'true' : 'TRUE',
  'false' : 'FALSE',
  'this' : 'THIS',
  'new' : 'NEW',
  'null' : 'NULL'
}

# Tipos de tokens

tokens = [
  'ID',
  'NUMBER',
  'ADDOP',            # +
  'SUBOP',            # -
  'MULTOP',           # *
  'ASSIGN',           # =
  'EQUALS',           # ==
  'NOTEQUALS',        # !=
  'NOT',              # !
  'LESSTHAN',         # <
  'LESSEQUAL',        # <=
  'GREATERTHAN',      # >
  'GREATEREQUAL',     # >=
  'OPENPAREN',        # (
  'CLOSEPAREN',       # )
  'OPENBRACKET',      # [
  'CLOSEBRACKET',     # ]
  'OPENBRACER',       # {
  'CLOSEBRACER',      # }
  'COMMA',            # ,
  'SEMICOLON',        # ;
  'AND',              # &&
  'DOT'               # .
] + list(reserved_words.values())

# Expressões regulares de tokens

t_ignore = ' \t'
t_ADDOP = r'\+'
t_SUBOP = r'-'
t_MULTOP = r'\*'
t_ASSIGN = r'='
t_EQUALS = r'=='
t_NOTEQUALS = r'!='
t_NOT = r'!'
t_LESSTHAN = r'<'
t_LESSEQUAL = r'<='
t_GREATERTHAN = r'>'
t_GREATEREQUAL = r'>='
t_OPENPAREN = r'\('
t_CLOSEPAREN = r'\)'
t_OPENBRACKET = r'\['
t_CLOSEBRACKET = r'\]'
t_OPENBRACER = r'\{'
t_CLOSEBRACER = r'\}'
t_COMMA = r','
t_SEMICOLON = r';'
t_AND = r'&&'
t_DOT = r'\.'


def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def find_column(input, token):
  line_start = input.rfind('\n', 0, token.lexpos) + 1
  return (token.lexpos - line_start) + 1

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

def t_ID(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  if t.value in reserved_words:
    t.type = reserved_words[ t.value ]
  return t

def t_SINGLE_LINE_COMMENT(t):
  r'//.*'
  pass

def t_MULT_LINE_COMMENT(t):
  r'(/\*(.|\n)*?\*/)'
  pass