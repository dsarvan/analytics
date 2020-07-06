import java.util.Scanner;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class program {

	static int str2int(String date) {

		int i = 0; int num = 0;

		while (i < date.length()) {
			num = num*10;
			num = num+date.charAt(i++) - '0';
		}

		return num;
	}

	static String Name() {

		Scanner uname = new Scanner(System.in);
		System.out.println("\nEnter name:");
		String name = uname.nextLine();

		try {
			if (name.length() < 3) {
				throw new ArithmeticException("Name should not be less than 3 characters.");
			}
		} catch (ArithmeticException e) { 
			System.out.print(e);
			name = Name();
	   	}

		return name;
	}

	static int Age() {

		Scanner udate = new Scanner(System.in);

		System.out.println("\nEnter D.O.B (yyyyMMdd):");
		int date = udate.nextInt();

		LocalDateTime tdate = LocalDateTime.now();
		DateTimeFormatter dmyr = DateTimeFormatter.ofPattern("yyyyMMdd");
		String fdate = tdate.format(dmyr);

		int ndate = str2int(fdate);
		int age = (ndate - date)/10000;

		try {
			if (age < 12) {
		   		throw new ArithmeticException("To apply, you must be at least 12 years old.");
			}
		} catch (ArithmeticException e) {  
			System.out.println(e); 
			System.out.println("Thanks for your consideration and understanding.");
		}

		return age;
	}

	static String Code() {

		Scanner ucode = new Scanner(System.in);
		System.out.println("\nEnter Pincode:");
		String code = ucode.nextLine();

		try {
			if (code.length() != 6) { throw new ArithmeticException("Pincode should be a 6 digit number."); }
		} catch (ArithmeticException e) {
		   	System.out.println(e);
			code = Code();
	   	}

		return code;
	}


	public static void main(String args[]) {

		Scanner ucode = new Scanner(System.in);

		String name = Name();
		int age = Age();
		String code = Code();

		System.out.println("\nApplicant's Information");
		System.out.println("Name    : "+ name);
		System.out.println("Age     : "+ age);
		System.out.println("Pincode : "+ code);
		if (age < 12) { System.out.println("Application Rejected."); }
		else { System.out.println("Application Accepted."); }
	}
}
