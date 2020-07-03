interface base {

	public void quote2();
	public void quote3();
}

class derived implements base {

	public void quote2() {

		System.out.println("There are three kinds of truths: data, data analyzed by a frequentist, and Bayesian Network statistics");
	}

	public void quote3() {

		System.out.println("If I had used Bayesian Netwoeks. I would have never gone bankrupt at the age 59 by making bad investments in the stock market.");
	}
}

public class intrface {

	public void quote1() {

		System.out.println("There are three kinds of lies: lies, damned lies, and statistics");
	}

	public static void main(String args[]) {

		intrface print1 = new intrface();
		derived print2 = new derived();

		print1.quote1();
		print2.quote2();
		print2.quote3();
	}
}
