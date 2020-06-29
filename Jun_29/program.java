import java.util.Scanner;





public class program {

	static void selection() {

		System.out.println("\nSelect Mathematical Operation:");

		String operation[] = {"+  = Additon", "-  = Subtraction", "*  = Multiplication",
		   			"/  = Division", "%  = Modulus", "++ = Increment", "-- = Decrement"};

		for (String text: operation) {

			System.out.println(text);
		}
	}

	public static void main(String args[]) {

		Scanner noperand = new Scanner(System.in);
		Scanner value = new Scanner(System.in);

		selection();

		System.out.println("\nEnter number of operand: ");
		int N = noperand.nextInt();

		float num[] = new float[N];

		for (int n = 1; n <= N; n++) {

			System.out.println("\nEnter value "+ n +":");
			num[n-1] = value.nextFloat();
		}

		for (int n = 1; n <= N; n++) {

			System.out.println("None");
		}
	}
}
