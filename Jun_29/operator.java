package arithmetic;

public class operator {

	public void operation(int N, String option, int num[]) {

		switch (option) {

			case "+":
				int sum = num[0]+num[1];
				System.out.println("\nSum of "+num[0] +" and "+ num[1] +" is "+ sum);
				break;

			case "-":
				int diff = num[0]-num[1];
				System.out.println("\nDifference of "+num[0] +" and "+ num[1] +" is "+ diff);
				break;

			case "*":
				int prod = num[0]*num[1];
				System.out.println("\nProduct of "+num[0] +" and "+ num[1] +" is "+ prod);
				break; 

			case "/":
				float div = (float) num[0]/num[1];
				System.out.println("\nQuotient of "+num[0]+"/"+num[1] +" is "+ div);
				break;

			case "%":
				int mod = num[0]%num[1];
				System.out.println("\nReminder of "+num[0]+"/"+num[1] +" is "+ mod);
				break;

			case "++":
				System.out.println("\nIncrement of "+num[0] +" by 1 is "+ (num[0]+1));
				System.out.println("Increment of "+num[1] +" by 1 is "+ (num[1]+1));
				break;

			case "--":
				System.out.println("\nDecrement of "+num[0] +" by 1 is "+ (num[0]-1));
				System.out.println("Decrement of "+num[1] +" by 1 is "+ (num[1]-1));
				break;

			default:
				System.out.println("\nInvalid operation, try again.");
		}
	}
}
