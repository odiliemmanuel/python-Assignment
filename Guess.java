import java.util.Random;
import java.util.Scanner;        
    public class Guess {
        public static void main(String...Odili) {
    
        Scanner input = new Scanner(System.in);
        Random random = new Random();

    int maximum = 20;
    int minimum = 0;

    int guessNumber = random.nextInt((maximum - minimum) +1);


    int number = 0;
//    System.out.println("Guess my Number ");
//         number = input.nextInt();

    while(number  != guessNumber) {

        System.out.println("Guess my Number ");
             number = input.nextInt();

        if(number  > guessNumber){
            System.out.println("Too high, please try again");
        }

        else if(number  < guessNumber) {
            System.out.println("Too low, please try again");
        }

        else if(number  == guessNumber) {
            System.out.println("Correct guess");
        }
    
      

    }





        }
    }
