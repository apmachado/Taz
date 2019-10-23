from lexer import tokens

def p_prog(p):
  'prog : main {class}'

def p_main(p):
  'main : CLASS ID OPENBRACER PUBLIC STATIC VOID MAIN OPENPAREN STRING OPENBRACKET CLOSEBRACKET ID OPENPAREN OPENBRACER cmd CLOSEBRACER CLOSEBRACER'

def p_classe(p):
  'class : CLASS ID [EXTENDS ID] OPENBRACER {var} {method} CLOSEBRACER'

def p_var(p):
  'var : type ID SEMICOLON'

def p_method(p):
  'method : PUBLIC type ID OPENPAREN [params] CLOSEPAREN OPENBRACER {var} {cmd} RETURN exp SEMICOLON CLOSEBRACER'

def p_params(p):
  'params : type ID {COMMA type ID}'

def p_type(p):
  '''type : int OPENBRACKET CLOSEBRACKET
          | BOOLEAN
          | INT
          | ID'''
def p_cmd(p):
  '''cmd : OPENBRACER {cmd} CLOSEBRACER
         | IF OPENPAREN exp CLOSEPAREN cmd
         | IF OPENPAREN exp CLOSEPAREN cmd ELSE cmd
         | WHILE OPENPAREN exp CLOSEPAREN cmd
         | PRINTLN OPENPAREN exp CLOSEPAREN SEMICOLON
         | ID ASSIGN exp SEMICOLON
         | ID OPENBRACKET exp CLOSEBRACKET ASSIGN exp SEMICOLON'''

def p_exp(p):
  '''exp : exp AND rexp
         | rexp'''

def p_rexp(p):
  '''rexp : rexp LESSTHAN aexp
          | rexp EQUALS aexp
          | rexp NOTEQUALS aexp
          | aexp'''

def p_aexp(p):
  '''aexp : aexp ADDOP mexp
          | aexp SUBOP mexp
          | mexp'''


def p_sexp(p):
  '''sexp : NOT sexp
          | SUBOP sexp
          | TRUE
          | FALSE
          | NUMBER
          | NULL
          | NEW INT OPENBRACKET exp CLOSEBRACKET
          | pexp DOT LENGTH
          | pexp OPENBRACKET exp CLOSEBRACKET
          | pexp'''

def p_pexp(p):
  '''pexp : ID
          | THIS
          | NEW ID OPENPAREN CLOSEPAREN
          | OPENPAREN exp CLOSEPAREN
          | pexp DOT ID
          | pexp DOT ID OPENPAREN [exps] CLOSEPAREN'''
def p_exps(p):# llex = []
  'exps : exp {COMMA exp}'

def p_error(p):
  if p:
    print("Syntax error at '%s'" % p.value)
  else:
    print("Syntax error at EOF")