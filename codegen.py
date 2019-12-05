def cgen(node):
  if not node:
    return
  if isinstance(node, tuple):
    if len(node) == 2:
      try:
        vizinhos = node[1]
        if node[0] == 'cmd':
          if (vizinhos[0] == 'if'):
            if_handler(node)
          else:
            for v in vizinhos:
              cgen(v)

        # EXP : EXP && REXP
        elif node[0] == 'exp':
          exp(node)
        elif node[0] == 'aexp': # soma ou subtracao
          aexp(node)
        elif node[0] == 'mexp': # multiplicacao
          mexp(node)
        elif node[0] == 'sexp':
          sexp(node)
        else:
          for v in vizinhos:
            cgen(v)
      except:
        print('erro em:', node)

# ('CMD', ['if', '(', EXP, ')', CMD]
# vai comparar o que está no acumulador com $zero
# se o acumulador for diferente de zero eh verdadeiro
def if_handler(node):
  cgen(node[1][2])
  if len(node[1]) == 7: # if else
    print('beq $a0 $zero false_branch')
    cgen(node[1][4])
    print('B end_if')
    # else
    print('false_branch:')
    cgen(node[1][6])
    print('end_if:')
  else: # somente o if
    print('beq $a0 $zero end_if')
    cgen(node[1][4])
    print('end_if:')

# EXP : EXP && REXP
def exp(node):
  if (len(node[1]) == 1):
    cgen(node[1][0])
    return

  cgen(node[1][0])
  print('SW $a0 0($sp)')
  print('ADDIU $sp $sp -4')
  cgen(node[1][2])
  print('LW $t1 4($sp)')
  print('ADDIU $sp $sp 4')
  print('AND $a0 $t1 $a0')

def aexp(node):
  if (len(node[1]) == 1):
    cgen(node[1][0])
    return

  cgen(node[1][0])
  print('SW $a0 0($sp)')
  print('ADDIU $sp $sp -4')
  cgen(node[1][2])
  print('LW $t1 4($sp)')
  print('ADDIU $sp $sp 4')
  if node[1][1] == '+':
    print('ADD $a0 $t1 $a0')
  else:
    print('SUB $a0 $t1 $a0')

def mexp(node):
  if (len(node[1]) == 1):
    cgen(node[1][0])
    return
  
  cgen(node[1][0])
  print('SW $a0 0($sp)')
  print('ADDIU $sp $sp -4')
  cgen(node[1][2])
  print('LW $t1 4($sp)')
  print('ADDIU $sp $sp 4')
  print('MULT $a0 $t1 $a0')

def sexp(node):
  vizinhos = node[1]
  if isinstance(vizinhos[0], int):
    print('LI $a0 ' + str(node))
  elif vizinhos[0] == 'true':
    print('LI $a0 1')
  elif vizinhos[0] == 'false' or vizinhos[0] == 'null':
    print('LI $a0 0')
  else:
    for v in vizinhos:
      cgen(v)
