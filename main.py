import sys
import lexer
import my_parser
import codegen
import ply.lex as lex
import ply.yacc as yacc



def print_tree(file, node, prof=0):
  if not node:
    return
  spaces = '  ' * prof
  if isinstance(node, tuple):
    file.write(spaces + ' <' +  node[0] + '>\n')
    if len(node) == 2:
      vizinhos = node[1]
      for v in vizinhos:
        print_tree(file, v, prof + 1)
  else:
    file.write(spaces + str(node) + '\n')

if len(sys.argv) < 2:
  print ('Informe o aquivo com o código fonte.')
  raise SystemExit

fileName = sys.argv[1]
source = open(fileName).read()
output = open(fileName.split('.')[0] + '.txt', 'w')
# generated_code = open(fileName.split('.')[0] + 'bin.txt', 'w')

scanner = lex.lex(module=lexer)
par = yacc.yacc(module=my_parser)

# analise lexica
scanner.input(source)
# analise sintatica
result = par.parse(source)

print_tree(output, result)
output.close()

# geracao de codigo
codegen.cgen(result)