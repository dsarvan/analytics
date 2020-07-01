class A {

	static void print() {

		System.out.println("\nIndia is my country. \nAll Indians are my brothers and sisters.");
	}
}

class B extends A {

	public void print() {

		printA();
		System.out.println("I love my country, and I am proud of its rich and varied heritage.");
	}
}

class C extends B {

	static void print() {

		C obj = new C();

		obj.printB();
		System.out.println("I shall always strive to be worthy of it.");
	}
}

class D extends C {

	public void print() {

		printC();
		System.out.println("I shall give respect to my parents, teachers and all the elders, and treat everyone with courtesy.");
	}
}

class E extends D {

	static void print() {

		E obj = new E();

		super.print();
		System.out.println("To my country and my people, I pledge my devotion.");
	}
}

public class pledge extends E {

	public static void main(String args[]) {

		print();
		System.out.println("In their well being and prosperity alone, lies my happiness.\n");
	}
}
