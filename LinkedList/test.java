// a code to explain static methods in oops. 
// always remember that the static methods only have one reference which is that of the class.
// the other instance methods have the reference of the object.
// So if the static method needs to access anything visible to the class( which is the other static variables and methods)
// then simply use the class name which is the reference here followed by a dot and the name of the variable or method.
// Likewise, the instance methods have a reference of the object in form of the object name or this keyword, either is 
// applicable, so the instance methods can access anything available to the object this way.
public class test{
    public static void main(String[] args){
        // testing onj = new test.testing();
        // onj.changeData();
        // System.out.println(onj.data);
        // test.testing obj = new test.testing();
        test.testing.changeData();
        test.testing.intro();

    }
    public class testing{
        static int data = 3;
        public static void changeData(){
        int data = 4;
        testing.data = 5;
        System.out.println(data);
        System.out.println(testing.data);
    }
        public void intro(){
            System.out.print("hello this is to test if non static methods are visible to the class or not.");
        }
    
        
    }

}