/* File: arrays.java
 * Name: D.Saravanan
 * Date: 24/06/2020
 * Comt: One dimensional and Multidimensional array in java
*/

public class arrays {

		public static void main(String args[]) {

				/* one dimensional array */

				int integers[] = {-4, -3, -2, -1, 0, 1, 2, 3, 4};

				System.out.println("Length: "+ integers.length);

				for (int value:integers) {

						System.out.println(value);
				}

				/* multidimensional array */

				int numbers[][] = { {1,2,3,4}, {5,6,7} };

				System.out.println("\nLength: "+ numbers.length);
				System.out.println("Length of array1: "+ numbers[0].length);
				System.out.println("Length of array2: "+ numbers[1].length);

				for (int m = 0; m < numbers.length; ++m) {
					for (int n = 0; n < numbers[m].length; ++n) {

							System.out.println(numbers[m][n]);
						}
				}
		}
}
