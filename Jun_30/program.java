class A {

	static void printA() {

		System.out.println("\nShe walks in beauty, like the night");
 	 }
}

class B extends A {

	public void printB() {

		printA();
		System.out.println("  Of cloudless climes and starry skies;");
 	 }
}

class C extends B {

	static void printC() {

		C obj = new C();

		obj.printB();
		System.out.println("And all that's best of dark and bright");
	}
}

class D extends C {

	public void printD() {

		printC();
		System.out.println("  Meet in her aspect and her eyes:");
	}
}

class E extends D {

	static void printE() {

		E obj = new E();

		obj.printD();
		System.out.println("Thus mellowed to that tender light");
	}
}

public class program extends E {

	public static void main(String args[]) {

		printE();
		System.out.println("  Which heaven to gaudy day denies.\n");
	}
}
