import java.util.Scanner;
import java.util.Random;

public class password {

	static int generate(int n) {

		Random rand = new Random();

		for (int i=1; i<=n; i++) {

			int x = rand.nextInt(9);
			return x;
		}

		return 0;
	}


	public static void main(String args[]) {

		Scanner nuser = new Scanner(System.in);
		Scanner nleng = new Scanner(System.in);

		System.out.println("\nEnter number of users:");
		int users = nuser.nextInt();

		System.out.println("\nEnter length of password:");
		int length = nleng.nextInt();

		System.out.println("\nRandomly generated OTP:");

		for (int i=1; i <= users; i++) {

			int value = generate(length);

			System.out.println("User "+ i +" : "+ value);
		}

	}
}
