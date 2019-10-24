from lexer import tokens

def p_epsilon(p):
  'epsilon :'
  pass

def p_prog(p):
  '''prog : prog_aux
          | epsilon'''

def p_prog_aux(p):
  '''prog_aux : prog_aux class
              | main'''

def p_main(p):
  'main : CLASS ID OPENBRACER PUBLIC STATIC VOID MAIN OPENPAREN STRING OPENBRACKET CLOSEBRACKET ID OPENPAREN OPENBRACER cmd CLOSEBRACER CLOSEBRACER'

def p_classe(p):
  '''class : classe_aux
           | epsilon'''

def p_classe_aux(p):
  '''classe_aux : CLASS ID OPENBRACER var method CLOSEBRACER
                | CLASS ID EXTENDS ID OPENBRACER var method CLOSEBRACER'''

def p_var(p):
  'var : type ID SEMICOLON'

def p_method(p):
  '''method : method_aux
            | epsilon'''

def p_method_aux(p):
  '''method_aux : PUBLIC type ID OPENPAREN CLOSEPAREN OPENBRACER var cmd RETURN exp SEMICOLON CLOSEBRACER
                | PUBLIC type ID OPENPAREN params CLOSEPAREN OPENBRACER var cmd RETURN exp SEMICOLON CLOSEBRACER'''

def p_params(p):
  '''params : params_aux
            | epsilon'''

def p_params_aux(p):
  '''params_aux : params_aux COMMA type ID
                | type ID'''

def p_type(p):
  '''type : INT OPENBRACKET CLOSEBRACKET
          | BOOLEAN
          | INT
          | ID'''

def p_cmd(p):
  '''cmd : cmd_aux
         | IF OPENPAREN exp CLOSEPAREN cmd
         | IF OPENPAREN exp CLOSEPAREN cmd ELSE cmd
         | WHILE OPENPAREN exp CLOSEPAREN cmd
         | PRINTLN OPENPAREN exp CLOSEPAREN SEMICOLON
         | ID ASSIGN exp SEMICOLON
         | ID OPENBRACKET exp CLOSEBRACKET ASSIGN exp SEMICOLON
         | epsilon'''

def p_cmd_aux(p):
  '''cmd_aux : OPENBRACER cmd_aux cmd CLOSEBRACER
             | OPENBRACER CLOSEBRACER'''

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

def p_mexp(p):
  '''mexp : mexp MULTOP sexp
          | sexp'''

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
          | pexp DOT ID OPENPAREN CLOSEPAREN
          | pexp DOT ID OPENPAREN exps CLOSEPAREN'''

def p_exps(p):# llex = []
  '''exps : exps
          | epsilon'''

def p_exps_aux(p):# llex = []
  'exps_aux : exp COMMA exp'

def p_error(p):
  if p:
    print("Syntax error at '%s'" % p.value)
  else:
    print("Syntax error at EOF")