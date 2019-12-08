class Factorial{
  public static void main(String[] a){
		System.out.println(new Fac().ComputeFac(50, 60));
  }
}

class Fac {
	public int ComputeFac(int x, int y){
		if (x == y)
			x = 3 + (20 * 5);
		else
			x =  y * 10 + this.somar(x, y);
			x = x - this.teste_loop(y);
		return x;
	}

	public int somar(int a, int b) {
		return a + b;
	}

	public int teste_loop(int x) {
		while (x < 100) {
			x = x + 10;
		}
		System.out.println(x);
		return x;
	}

}