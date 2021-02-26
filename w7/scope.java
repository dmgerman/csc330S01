class MyClass {

    void methodA() {
        System.out.println("in method A");
        methodB();
    }

    // Public method
    void methodB() {
        i++;
        System.out.println("in method B");
        methodC();
    }

    void methodC() {
        int j = 1;
        int k = 2;
        System.out.println(j);

    }
    int i = 0;

}


public class scope {

    // Main method
    public static void main(String[] args) {

        MyClass myObj = new MyClass();
        myObj.methodA(); // Call the public method on the object

    }
}
