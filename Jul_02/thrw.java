public class thrw {

	public static void main(String args[]) {

		int age = -2;

		if (age <= 0) {

			/* throw keyword is used to create user-defined exception*/
			throw new ArithmeticException("Invalid input.");
		}

		System.out.println("Age: "+ age);
	}
}
