/* File: datatypes.java
 * Name: D.Saravanan
 * Date: 23/06/2020
 * Comt: Datatypes in Java
*/

class datatypes {

		public static void main(String args[]) {

				/* byte: 1 byte: stores whole numbers from -128 to 127 */
				byte bvalue = 127;
				System.out.println("Byte: "+ bvalue);

				/* short: 2 bytes: store whole numbers from -32768 to 32767 */
				short svalue = 32767;
				System.out.println("Short: "+ svalue);

				/* int: 4 bytes: stores whole numbers from -2,147,483,648 to 2,147,483,647 */
				int integer = 2147483647;
				System.out.println("Integer: "+ integer);

				/* long: 8 bytes: stores whole numbers from -9,223,272,036,854,775,808 to 9,223,372,036,854,775,807 */
				long lvalue = 9223372036854775807l;
				System.out.println("Long: "+ lvalue);

				/* float: 4 bytes: stores fractional numbers, 6 to 7 decimal digits */
				float fvalue = 3.1415f;
				System.out.println("Float: "+ fvalue);

				/* double: 8 bytes: stores fractional numbers, 15 decimal digits */
				double dvalue = 3.1415d;
				System.out.println("Double: "+ dvalue);

				/* boolean: 1 bit: stores true or false values */
				boolean blvalue = true;
				System.out.println("Boolean: "+ blvalue);

				/* char: 2 bytes: stores a single character or ASCII values */
				char cvalue = 'F';
				System.out.println("Character: "+ cvalue);

		}
}
