import java.util.Random;
import java.util.Scanner;        
    public class GuessTwo {
        public static void main(String...Odili) {
    
        Scanner input = new Scanner(System.in);
        Random random = new Random();

    int maximum = 20;
    int minimum = 0;
    int numberOfTimes = 3;
    int guessNumber = random.nextInt((maximum - minimum) +1);


        int max = 6;
        int min = 0;
        int guessNum = random.nextInt((max - min)+1);
        int anotherGuesss = 0;

        for(int count = 0; count <= 2; count ++) {

            if(guessNum != anotherGuesss) {
            System.out.println("Try guessing this one ");
               anotherGuesss = input.nextInt();

            }

             if(anotherGuesss  > guessNum){
            System.out.println("Too high, please try again");
           }

            else if(anotherGuesss  < guessNum) {
                System.out.println("Too low, please try again");
            }

            else if(anotherGuesss  == guessNum) {
                System.out.println("Correct guess");
            }

            else if(anotherGuesss <= count){
                        System.out.println("Exceeded trial limit");
            
                    
               }

               
        }


        }
    }





























