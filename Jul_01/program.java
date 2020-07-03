import java.util.Scanner;

/* A particle starts with an initital velocity u m/s along the positive x direction and 
 * it accelerates uniformly at the rate 0.50 m/s2. (a) Find the distance travelled by it
 * in the first two seconds. (b) Find the time does it take to reach the velocity v m/s.
 * (c) How much distance will it cover in reaching the velocity v m/s ?
*/

class AAA { 

	double a = 0.50;

	public double velocity1() {

		Scanner ivelocity = new Scanner(System.in);

		System.out.println("\nInitial velocity:");
		double u = ivelocity.nextDouble();

		return u;
	}

	public double velocity2() {

		Scanner fvelocity = new Scanner(System.in);

		System.out.println("Final velocity:");
		double v = fvelocity.nextDouble();

		return v;
	}
}

interface BBB {

	public void distance(double u, double a);
}

interface CCC {

	public void time(double u, double v, double a);
}

class DDD implements BBB, CCC {

	public void distance(double u, double a) {

		int t = 2;

		double x = u*t + 0.5*a*t*t;
		System.out.println("\nDistance travelled by it in first "+t+" s is "+x+" m");
	}

	public void time(double u, double v, double a) {

		double t = (v-u)/a;
		System.out.println("Time it takes to reach velocity "+v+" m/s is "+t+" s");
	}
}

public class program extends DDD {

	static void distance(double u, double v, double a) {

		double x = (v*v - u*u)/(2*a);
		System.out.println("Distance it cover reaching velocity "+v+" m/s is "+x+" m");
	}

	public static void main(String args[]) {

		AAA value = new AAA();

		double u = value.velocity1();
		double v = value.velocity2();

		DDD result = new DDD();
		result.distance(u, value.a);
		result.time(u, v, value.a);

		distance(u, v, value.a);
	}
}
