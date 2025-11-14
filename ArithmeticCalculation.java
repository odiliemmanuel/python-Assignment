// a program that biulds a simple arithmetic calculator
// prompt the user to enter first number
// prompt the user to enter second integer
//prompt the user to enter an operator
// give operatior values
//store in variables
// display the result of the first number, the operator in the middle and the second number
//

import java.util.Scanner;
public class ArithmeticCalculation {

    public static void main(String[] args){

        Scanner input = new Scanner(System.in);

        System.out.println("Enter first number");
        int firstNumber = input.nextInt();

        System.out.println("Enter second number");
        int secondNumber = input.nextInt();

        System.out.println("Enter An Operator (+, -, *, /)");
        String operator = input.next();

        String times = "*";
        String plus = "+";
        String minus = "-";
        String divide = "/";

        int result = 0;

        if(operator.equals (times)) {
            result = firstNumber * secondNumber;
            System.out.printf("The result of %d %s %d = %d%n", firstNumber, times, secondNumber, result);
        }

        if(operator.equals(plus)) {
            result = firstNumber + secondNumber;
            System.out.printf("The result of %d %s %d = %d%n", firstNumber, plus, secondNumber, result);
        }

        if(operator.equals (minus)) {
            result = firstNumber - secondNumber;
            System.out.printf("The result of %d %s %d = %d%n", firstNumber, minus, secondNumber, result);
        }

        if(operator.equals (divide)) {
            result = firstNumber / secondNumber;
            System.out.printf("The result of %d %s %d = %d%n", firstNumber, divide, secondNumber, result);
        }
    }

}



