/* File: conditional.java
 * Name: D.Saravanan
 * Date: 24/06/2020
 * Comt: Conditional statements in Java
*/

public class conditional {

		public static void main(String args[]) {

				/* if, else if, else condition */

				int x = 20;
				int y = 18;

				if (x > y) {
						System.out.println("x is greater than y");
				}

				else if (x < y) {
						System.out.println("x is lesser than y");
				}

				else {
						System.out.println("x is equal to y");
				}

				if (true) {
						System.out.println("Learning Java");
				}

				else {
						System.out.println("Not learning Java");
				}


				/* switch statement */

				int day = 6;

				switch (day) {

						case 1:
								System.out.println("Sunday");
								break;

						case 2:
								System.out.println("Monday");
								break;

						case 3:
								System.out.println("Tuesday");
								break;

						case 4:
								System.out.println("Wednesday");
								break;

						case 5:
								System.out.println("Thursday");
								break;

						case 6:
								System.out.println("Friday");
								break;

						default:
								System.out.println("Saturday");
				}
		}
}	
