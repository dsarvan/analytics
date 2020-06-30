import java.util.Scanner;
import arithmetic.operator;

public class program {

	static String selection() {

		Scanner select = new Scanner(System.in);

		System.out.println("\nSelect Mathematical Operation:");

		String operation[] = {"+  = Additon", "-  = Subtraction", "*  = Multiplication",
		   			"/  = Division", "%  = Modulus", "++ = Increment", "-- = Decrement"};

		for (String text: operation) {

			System.out.println(text);
		}

		System.out.println("\nEnter operation:");
		String option = select.nextLine();

		return option;
	}

	public static void main(String args[]) {

		Scanner noperand = new Scanner(System.in);
		Scanner value = new Scanner(System.in);

		String option = selection();

		int num[] = new int[2];

		for (int n = 1; n <= 2; n++) {

			System.out.println("\nEnter integer value "+ n +":");
			num[n-1] = value.nextInt();
		}

		operator math = new operator();
		math.operation(2, option, num);

	}
}
