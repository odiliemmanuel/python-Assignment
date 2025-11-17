    import java.util.Scanner;
        public class NumberOfYears {
            public static void main(String[] args) {

    Scanner input = new Scanner(System.in);

        
    System.out.println("Enter The Current Age Of Father");
        int fathersAge = input.nextInt();

    System.out.println("Enter The Current Age Of The Son");
        int sonsAge = input.nextInt();

        int years = input.nextInt();
        sonsAnticipatedAge = 0;
            fathersPastAge = 0;
        sonsAnticipatedAge = sonsAge * 2;

        fathersPastAge = fathersAge - sonsAge;

        System.out.println("The father will be" + fathersPastAge);

            }
        } 
