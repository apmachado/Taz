def cgen(node):
  if not node:
    return
  if isinstance(node, tuple):
    if len(node) == 2:
      try:
        vizinhos = node[1]
        # operacoes binarias
        if len(vizinhos) == 3:
          if node[0] == 'aexp': # soma ou subtracao
            aexp(node)
          elif node[0] == 'mexp': # multiplicacao
            mexp(node)
          elif node[0] == 'sexp':
            sexp(node)
          else:
            for v in vizinhos:
              cgen(v)
        else:
          for v in vizinhos:
            cgen(v)
      except:
        print('erro em:', node)
  else:
    if isinstance(node, int) or isinstance(node, float):
      # valores numéricos
      # li $a0 num
      print('LI $ao ' + str(node))
    else:
      pass
      # if (not node in ['(', ')']):
      #   print('token', node)


def aexp(node):
  cgen(node[1][0])
  print('SW $ao 0($sp)')
  print('ADDIU $sp $sp -4')
  cgen(node[1][2])
  print('LW $t1 4($sp)')
  print('ADDIU $sp $sp 4')
  if node[1][1] == '+':
    print('ADD $a0 $t1 $ao')
  else:
    print('SUB $a0 $t1 $ao')

def mexp(node):
  cgen(node[1][0])
  print('SW $ao 0($sp)')
  print('ADDIU $sp $sp -4')
  cgen(node[1][2])
  print('LW $t1 4($sp)')
  print('ADDIU $sp $sp 4')
  print('MULT $a0 $t1 $ao')

def sexp(node):
  if len(node) == 1:
    valor = node[1][0]
    if isinstance(valor, int) or isinstance(valor, float):
      print('li $ao ' + str(node))
    else:
      cgen(valor)
  else:
    vizinhos = node[1]
    for v in vizinhos:
      cgen(v)
