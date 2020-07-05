import java.util.Scanner;

public class weird {

	public static void main(String args[]) {

		Scanner value = new Scanner(System.in);

		System.out.println("Enter a positive integer:");
		long n = value.nextLong();

		while (n > 1) {

			if (n%2 == 0) { n = n/2; }
			else { n = (n*3) + 1; }

			System.out.println(n);
		}
	}
}






