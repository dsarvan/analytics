/* File: password.java
 * Name: D.Saravanan
 * Date: 25/06/2020
 * Comt: Program to generate password with numbers
*/

import java.util.Scanner;
import java.util.Random;

public class password {

	static int values(int num) {

		int count = 0;

		while (num != 0) {

			num /= 10;
			count++;
		}

		return count;
	}

	static int generate(int n) {

		Random rand = new Random();

		int num = 1; int nvalue; int result = 0;

		for (int i=1; i<=n; i++) {

			int x = rand.nextInt(9);
			num += x * Math.pow(10,i-1);

			nvalue = values(num);

			if (nvalue == n) {

				result = num;
			}

			else {

				result = (int) (Math.pow(10,n-1)) + num;
			}
		}

		return result;
	}

	public static void main(String args[]) {

		Scanner nuser = new Scanner(System.in);
		Scanner nleng = new Scanner(System.in);

		System.out.println("\nEnter number of users:");
		int users = nuser.nextInt();

		System.out.println("\nEnter length of password:");
		int length = nleng.nextInt();

		System.out.println("\nRandomly generated OTP:");

		for (int i=1; i<=users; i++) {

			int value = generate(length);

			System.out.println("User "+ i +" : "+ value);
		}
	}
}
