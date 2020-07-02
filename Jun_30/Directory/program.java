class A {

	public void print() {

		System.out.println("\nShe walks in beauty, like the night");
	}
}

class B extends A {

	public void print() {

		super.print();
		System.out.println("  Of cloudless climes and starry skies;");
	}
}

class C extends B {

	public void print() {

		super.print();
		System.out.println("And all that's best of dark and bright");
	}
}

class D extends C {

	public void print() {

		super.print();
		System.out.println("  Meet in her aspect and her eyes:");
	}
}

class E extends D {

	public void print() {

		super.print();
		System.out.println("Thus mellowed to that tender light");
	}
}

public class program extends E {

	public static void main(String args[]) {

		program obj = new program();

		obj.print();
		System.out.println("  Which heaven to gaudy day denies.\n");
	}
}
