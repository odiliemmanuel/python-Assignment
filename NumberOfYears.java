// prompt the user to enter the age of father
// store as a variable
// prompt the user to enter the age of the son
// store as a variable
// multiply son's age by two
// subtract fathers age by the sons age times two
//print result







    import java.util.Scanner;
        public class AgeInput {
            public static void main(String[] args) {

    Scanner input = new Scanner(System.in);

        
    System.out.println("Enter The Current Age Of Father");
        int fathersAge = input.nextInt();

    System.out.println("Enter The Current Age Of The Son");
        int sonsAge = input.nextInt();

        sonsAge = sonsAge * 2;

        fathersAge = fathersAge - sonsAge * 2;

        System.out.println("The father will be" + fathersAge);

            }
        } 
