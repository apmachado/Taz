class Factorial{
    public static void main(String[] a){
	System.out.println(new Fac().ComputeFac(50, 50));
    }
}

class Fac {
    public int ComputeFac(int x, int y){
			if (x == y)
				x = 3 + (20 * 5);
			else
				x =  y * 10;
			return x;
    }

}