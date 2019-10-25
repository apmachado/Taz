from lexer import tokens


precedence = (
  ('left', 'ADDOP', 'SUBOP'),
  ('left', 'MULTOP')
 )

def p_prog(p):
  'prog : main class_aux '

def p_main(p):
  'main : CLASS ID OPENBRACER PUBLIC STATIC VOID MAIN OPENPAREN STRING OPENBRACKET CLOSEBRACKET ID OPENPAREN OPENBRACER cmd CLOSEBRACER CLOSEBRACER'

def p_class_aux(p):
  '''class_aux : class_aux class
               | epsilon'''

def p_class(p):
  '''class : CLASS ID OPENBRACER var_aux method_aux CLOSEBRACER
           | CLASS ID EXTENDS ID OPENBRACER var_aux method_aux CLOSEBRACER'''

def p_var_aux(p):
  '''var_aux : var_aux var
             | epsilon'''

def p_var(p):
  'var : type ID SEMICOLON'

def p_method_aux(p):
  '''method_aux : method_aux method
                | epsilon'''

def p_method(p):
  '''method : PUBLIC type ID OPENPAREN CLOSEPAREN OPENBRACER var_aux cmd_aux RETURN exp SEMICOLON CLOSEBRACER
            | PUBLIC type ID OPENPAREN params CLOSEPAREN OPENBRACER var_aux cmd_aux RETURN exp SEMICOLON CLOSEBRACER'''

def p_params(p):
  'params : type ID type_aux'

def p_type_aux(p):
  '''type_aux : type_aux COMMA type ID 
                | epsilon'''

def p_type(p):
  '''type : INT OPENBRACKET CLOSEBRACKET
          | BOOLEAN
          | INT
          | ID'''

def p_cmd_aux(p):
  '''cmd_aux : cmd_aux cmd
             | epsilon'''

def p_cmd(p):
  '''cmd : OPENBRACER cmd_aux CLOSEBRACER
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
          | rexp LESSEQUAL aexp
          | rexp EQUALS aexp
          | rexp GREATEREQUAL aexp
          | rexp GREATERTHAN aexp
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
def p_exps(p):
  'exps : exp exp_aux'

def p_exp_aux(p):
  '''exp_aux : exp_aux COMMA exp
             | epsilon'''

def p_epsilon(p):
  'epsilon :'
  pass

def p_error(p):
  if p:
    print("Syntax error at '%s'" % p.value)
  else:
    print("Syntax error at EOF")