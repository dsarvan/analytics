import java.time.LocalDate;
import java.time.LocalTime;
import java.time.LocalDateTime;

public class datetime {

	public static void main(String args[]) {

		LocalDate date = LocalDate.now();
		System.out.println(date);

		LocalTime time = LocalTime.now();
		System.out.println(time);

		LocalDateTime dtime = LocalDateTime.now();
		System.out.println(dtime);
	}
}
