public class trycatch {

	public static void main(String args[]) {

		int num1 = 1;
		int num2 = 0;

		try { int divide = num1/num2; }

		catch (ArithmeticException e) {
			System.out.println("Arithmetic Exception Occured \n"+ e);
		}

		catch (Exception e) {
			System.out.println("Unknown Exception Occured \n"+ e);
		}
	}
}
