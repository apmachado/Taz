import traceback

# para criar nomes de labels distintos
# ex: branch_true_2
# cada label criada ela deve ser incrementada
label_count = 0

global_context = []
curr_context = []

def get_label_name(name):
  global label_count
  name = name + '_' + str(label_count)
  label_count = label_count + 1
  return name

def cgen(node):
  if not node:
    return
  if isinstance(node, tuple):
    if len(node) == 2:
      try:
        vizinhos = node[1]
        if node[0] == 'main':
          main(node)
        elif node[0] == 'method':
          metodo_handler(node)
        elif node[0] == 'params':
          params(node)
        elif node[0] == 'type_aux':
          type_aux(node)
        # CMD
        elif node[0] == 'cmd':
          if vizinhos[0] == 'if':
            if_handler(node)
          elif vizinhos[0] == 'while':
            while_handler(node)
          elif vizinhos[0] == 'System.out.println':
            print_handler(node)
          elif vizinhos[0] in curr_context:
            atribuicao(node)
          else:
            for v in vizinhos:
              cgen(v)

        elif node[0] == 'exp':
          exp(node)
        elif node[0] == 'rexp':
          rexp(node)
        elif node[0] == 'aexp': # soma ou subtracao
          aexp(node)
        elif node[0] == 'mexp': # multiplicacao
          mexp(node)
        elif node[0] == 'sexp':
          sexp(node)
        elif node[0] == 'pexp':
          pexp(node)
        elif node[0] == 'exps': # parametros da chamada de função
          exps(node) 
        elif node[0] == 'exp_aux': # parametros da chamada de função
          exp_aux(node)
        else:
          for v in vizinhos:
            cgen(v)
      except Exception:
        print('erro em:', node)
        traceback.print_exc()
# codigo da main
# MAIN : class id '{' public static void main '(' String '[' ']' id ')' '{' CMD '}' '}'
def main(node):
  vizinhos = node[1]
  print('.data')
  print('newline: .asciiz "\\n"')
  print('.text\n')
  print('main:')
  cgen(vizinhos[14]) # CMD
  print('\nexit: ')
  print('LI $v0, 10')
  print('syscall')
  # print('\n# funcoes')


# METODO : public TIPO id '(' PARAMS ')' '{' VAR_AUX CMD_AUX return EXP ; '}'
#        | public TIPO id '(' ')' '{' VAR_AUX CMD_AUX return EXP ; '}'
def metodo_handler(node):
  global curr_context
  vizinhos = node[1]
  num_parametros = 0
  context = []
  curr_context = context
  # se existir parametros chama cgen para eles
  if len(vizinhos) == 13:
    cgen(vizinhos[4])

  print('\nf_' + vizinhos[2] + ':')
  print('MOVE $fp $sp')
  print('SW $ra 0($sp)')
  print('ADDIU $sp $sp -4')
  if len(vizinhos) == 13:
    cgen(vizinhos[7])
    cgen(vizinhos[8])
    cgen(vizinhos[10])
  else:
    cgen(vizinhos[6])
    cgen(vizinhos[7])
    cgen(vizinhos[9])
  num_parametros = len(curr_context)
  print('LW $ra 4($sp)')
  print('ADDIU $sp $sp ' + str((num_parametros * 4) + 8) + ' # desempilha a funcao')
  print('LW $fp 0($sp)')
  print('JR $ra')

# PARAMS : TIPO id TIPO_AUX

# TIPO_AUX : TIPO_AUX , TIPO id
#          | epsilon
def params(node):
  vizinhos = node[1]
  curr_context.append(node[1][1])
  cgen(node[1][2])

def type_aux(node):
  if len(node[1]) == 1 and node[1][0] == None:
    return
  vizinhos = node[1]
  curr_context.append(node[1][3])
  if vizinhos[0] != None:
    cgen(node[1][0])

# ('CMD', ['if', '(', EXP, ')', CMD]
# vai comparar o que está no acumulador com $zero
# se o acumulador for diferente de zero eh verdadeiro
def if_handler(node):
  branch_true = get_label_name('branch_true')
  end_if = get_label_name('end_if')
  cgen(node[1][2])
  if len(node[1]) == 7: # if else
    branch_false = get_label_name('branch_false')
    print('BEQ $a0 $zero ' + branch_false)
    cgen(node[1][4])
    print('B ' + end_if)
    # else
    print(branch_false + ':')
    cgen(node[1][6])
    print(end_if + ':')
  else: # somente o if
    print('BEQ $a0 $zero ' + end_if)
    cgen(node[1][4])
    print(end_if + ':')

def while_handler(node):
  vizinhos = node[1]
  loop_label = get_label_name('loop')
  exit_label = get_label_name('exit')
  print(loop_label + ':')
  cgen(vizinhos[2])
  # print('LI $v0, 1')
  # print('syscall')
  print('BEQ $a0 $zero ' + exit_label) # se for falso sai do loop
  cgen(vizinhos[4])
  print('B ' + loop_label)
  print(exit_label + ':')

def print_handler(node):
  cgen(node[1][2])
  print('LI $v0, 1')
  print('syscall')
  print('LI $v0, 4')
  print('LA $a0, newline')
  print('syscall')

def atribuicao(node):
  vizinhos = node[1]
  if len(vizinhos) == 4:
    cgen(vizinhos[2])
    z = (curr_context.index(vizinhos[0]) + 1) * 4
    print('SW $a0 %i($fp) ' %z, end ='')
    print('# %s <- $a0' % vizinhos[0])
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

def rexp(node):
  if len(node[1]) == 1:
    cgen(node[1][0])
    return
  op = node[1][1]

  if op == '!==' or op == '==':
    branch_true = get_label_name('branch_true')
    end_if = get_label_name('end_if')
    cgen(node[1][0])
    print('SW $a0 0($sp)')
    print('ADDIU $sp $sp -4')
    cgen(node[1][2])
    print('LW $t1 4($sp)')
    print('ADDIU $sp $sp 4')
    if op == '!==':
      print('BNE $a0 $t1 ' + branch_true)
    else:
      print('BEQ $a0 $t1 ' + branch_true)
    print('LI $a0 0')
    print('B ' + end_if)
    print(branch_true + ':')
    print('LI $a0 1')
    print(end_if + ':')
  elif op == '<':
    cgen(node[1][0])
    print('SW $a0 0($sp)')
    print('ADDIU $sp $sp -4')
    cgen(node[1][2])
    print('LW $t1 4($sp)')
    print('ADDIU $sp $sp 4')
    print('SLT $a0, $t1, $a0')

def aexp(node):
  if len(node[1]) == 1:
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
  if len(node[1]) == 1:
    cgen(node[1][0])
    return
  
  cgen(node[1][0])
  print('SW $a0 0($sp)')
  print('ADDIU $sp $sp -4')
  cgen(node[1][2])
  print('LW $t1 4($sp)')
  print('ADDIU $sp $sp 4')
  print('MUL $a0 $t1 $a0')

def sexp(node):
  vizinhos = node[1]
  if isinstance(vizinhos[0], int):
    print('LI $a0 ' + str(vizinhos[0]))
  elif vizinhos[0] == 'true':
    print('LI $a0 1')
  elif vizinhos[0] == 'false' or vizinhos[0] == 'null':
    print('LI $a0 0')
  else:
    for v in vizinhos:
      cgen(v)

def pexp(node):
  vizinhos = node[1]
  if vizinhos[0] in curr_context:
    z = (curr_context.index(vizinhos[0]) + 1) * 4 # calcular z
    print('LW $a0 %i($fp) ' %z, end = '')
    print('# $a0 <- %s' % vizinhos[0])
  elif len(vizinhos) >= 5: # se eh uma chamada de funcao
    print('SW $fp 0($sp)')
    print('ADDIU $sp $sp -4')
    if len(vizinhos) == 6:
      cgen(vizinhos[4])
    print('JAL f_' + vizinhos[2])
  else:
    for v in vizinhos:
      cgen(v)

# EXPS : EXP EXP_AUX
def exps(node):
  cgen(node[1][1])
  cgen(node[1][0]) # ultimo parametro
  print('SW $a0 0($sp)')
  print('ADDIU $sp $sp -4')

# EXP_AUX : EXP_AUX , EXP
# para passagem de parametros
def exp_aux(node):
  if len(node[1]) == 1 and node[1][0] == None:
    return
  cgen(node[1][0])
  cgen(node[1][2])
  print('SW $a0 0($sp)')
  print('ADDIU $sp $sp -4')
    