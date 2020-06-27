/* File: animal.java
 * Name: D.Saravanan
 * Date: 26/06/2020
 * Comt: Program to understand class in java
*/


public class animal {

	/* attributes are variables within a class */
	int legs = 4;

	public static void main(String args[]) {

		/* class -> animal and object -> lion */
		animal lion = new animal();
		System.out.println(lion.legs);

		/* class -> animal and object -> tiger */
		animal tiger = new animal();
		System.out.println(tiger.legs);

		/* modify attributes */
		animal human = new animal();
		System.out.println(human.legs = 2);
	}
}
