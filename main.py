import lexer
import parser
import ply.lex as lex
import ply.yacc as yacc


def print_tree(node, prof=0):
  if not node:
    return
  if isinstance(node, tuple):
    print('  ' * prof, '<', node[0], '>')
    if len(node) == 2:
      vizinhos = node[1]
      for v in vizinhos:
        print_tree(v, prof + 1)
  else:
    print('  ' * prof, node)

prog = '''
class Factorial{
  public static void main(String[] a){
    System.out.println(new Fac().ComputeFac(10));
  }
}

class Fac {
  public int ComputeFac(int num){
  int num_aux;
  if (num < 1)
    num_aux = 1;
  else
    num_aux = num * (this.ComputeFac(num-1));
  return num_aux ;
  }
}
'''

scanner = lex.lex(module=lexer)
scanner.input(prog)


# for token in scanner:
#   print(token)

par = yacc.yacc(module=parser)
result = par.parse(prog)
print_tree(result)
