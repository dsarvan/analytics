/* File: breakcontinue.java
 * Name: D.Saravanan
 * Date: 24/06/2020
 * Comt: Break and Continue statement in Java
*/

public class breakcontinue {

		public static void main(String args[]) {

				/* break statement */
				/* print values from 0 to 3 */

				for (int m = 0; m < 10; m++) {
						
						if (m == 4) {
								break;
						}

						System.out.println(m);
				}

				/* continue statement */
				/* print values all values from 0 to 9 but 4 */

				for (int n = 0; n < 10; n++) {

						if (n == 4) {
								continue;
						}

						System.out.println(n);
				}
		}
}
