package arithmetic;

public class operator {

	public void x(int num1, int num2) {

		switch (selection) {

			case +:
				System.out.println(num1+num2);
				break;

			case -:
				System.out.println(num1-num2);
				break;

			case *:
				System.out.println(num1*num2);
				break;

			case /:
				System.out.println(num1/num2);
				break;

			case %:
				System.out.println(num1%num2);
				break;

			case ++:
				System.out.println(num1+1);
				System.out.println(num2+1);
				break;

			case --:
				System.out.println(num1-1);
				System.out.println(num2-1);
				break;

			default:
				System.out.println("None");
		}
	}
}
