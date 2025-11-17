import java.util.Scanner;
public class Calculator {

    public static void main(String[] args){

        Scanner input = new Scanner(System.in);

        System.out.println("Enter first number");
        int firstNumber = input.nextInt();

        System.out.println("Enter second number");
        int secondNumber = input.nextInt();

        System.out.println("Enter An Operator (+, -, *, /)");
        String operator = input.next();

        String times = "*";
        String plus = " + ";
        String minus = "-";
        String divide = "/";

        int result = 0;

        if(operator.equals (times)) {
            result = firstNumber * secondNumber;
            System.out.printf("The result of %d %s %d= %d", firstNumber, times, secondNumber, result);
        }
    }

}



