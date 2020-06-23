/* File: casting.java
 * Name: D.Saravanan
 * Date: 23/06/2020
 * Comt: Type Casting in Java
*/

public class casting {

		public static void main(String args[]) {

			/* Widening Casting */

			int ivalue = 3;
			double dvalue = ivalue;

			System.out.println("\nWidening Casting:");
			System.out.println("Integer: "+ ivalue);
			System.out.println("Double: "+ dvalue);

			/* Narrowing Casting */

			double fvalue = 3.1415;
			int value = (int) fvalue;

			System.out.println("\nNarrowing Casting:");
			System.out.println("Double: "+ fvalue);
			System.out.println("Integer: "+ value);

		}
}
