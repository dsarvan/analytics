abstract class base {

	abstract void method1();

	static void method2() {

		System.out.println("There are three kinds of truths: data, data analyzed by a frequentist, and Bayesian Network statistics.");
	}

	public void method3() {

		System.out.println("If I had used Bayesian Networks. I would have never gone bankrupt at the age 59 by making bad investments in the stock market.");
	}
}

class derived extends base {

	public void method1() {

		System.out.println("There are three kinds of lies: lies, damned lies, and statistics.");
	}
}

public class abstrct {

	public static void main(String args[]) {

		derived print = new derived();

		print.method1();
		print.method2();
		print.method3();
	}
}
