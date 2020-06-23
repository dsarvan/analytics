/* File: bitwise.java
 * Name: D.Saravanan
 * Date: 23/06/2020
 * Comt: Bitwise operators in Java
*/

public class bitwise {

		public static void main(String args[]) {

				/* Performs bit by bit processing */

				byte num1 = 11;
				byte num2 = 22;

				System.out.println(num1 & num2);
				System.out.println(num1 | num2);
				System.out.println(num1 ^ num2);
				System.out.println(~ num1);
				System.out.println(num1 << 2);
		}
}
