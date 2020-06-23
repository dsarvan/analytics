/* File: program.java
 * Name: D.Saravanan
 * Date: 23/06/2020
 * Comt: Java program to get user name and age and display it
*/

import java.util.Scanner;

public class program {

		public static void main(String args[]) {

				Scanner uname = new Scanner(System.in);
				Scanner uage = new Scanner(System.in);

				System.out.println("\nEnter Name: ");
				String name = uname.nextLine();
				System.out.println("\nEnter Age: ");
				byte age = uage.nextByte();
				
				System.out.println("\nName: "+ name.toUpperCase());
				System.out.println("Half-Age: "+ (byte) age/2);
		}
}
