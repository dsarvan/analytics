/* File: user.java
 * Name: D.Saravanan
 * Date: 26/06/2020
 * Comt: Program to get N users name and age and display them
*/

import java.util.Scanner;

public class user {

	String name;
	int age;

	static void information(int n, String name, int age) {

		System.out.println("\nInformation of user "+ n +":");
		System.out.println("Name: "+ name);
		System.out.println("Age : "+ age);
	}

	public user(String text) {

		name = text;
	}

	public user(int num) {

		age = num;
	}

	public static void main(String args[]) {

		Scanner nuser = new Scanner(System.in);
		Scanner uname = new Scanner(System.in);
		Scanner uage  = new Scanner(System.in);

		System.out.println("\nEnter number of users:");
		int N = nuser.nextInt();

		String text[] = new String[N];
		int num[] = new int[N];

		for (int n = 1; n <= N; n++) {

			System.out.println("\nEnter user "+ n +" name:"); 
			text[n-1] = uname.nextLine();

			System.out.println("Enter user "+ n +" age:");
			num[n-1] = uage.nextInt();
		}

		for (int n = 0; n <= N-1; n++) {

			user u_name = new user(text[n]); 
			user u_age = new user(num[n]);

			information(n+1, u_name.name, u_age.age);
		}
	}
}
