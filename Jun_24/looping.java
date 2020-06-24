/* File: looping.java
 * Name: D.Saravanan
 * Date: 24/06/2020
 * Comt: Looping statements in Java
*/

public class looping {

		public static void main(String args[]) {

				int m = 0;

				/* while loop */

				while (m < 5) {
						System.out.println(m);
						m++;
				}

				int n = 0;

				/* do-while loop */

				do {
						System.out.println(n);
						n++;
				} while (n < 5);

				/* for loop */

				for (int i = 0; i < 5; i++) {
						System.out.println(i);
				}

				byte numbers[] = {0, 1, 2, 3, 4};

				for (int value : numbers) {
						System.out.println(value);
				}
		}
}
