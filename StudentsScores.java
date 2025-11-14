//a program that calculates the average of three scores
//prompt the user to enter scores
//store as variable
//if score is less than 90 and less than 100 print A
//f scores is less than 80 and less than 90 print B
//if scores is less than 70 and less than 80 print C
//if scores is less than 60 and less than 70 print D
//if scores is less than 0 and less than 60 print F



  import java.util.Scanner;
      public class AgeInput {
          public static void main(String[] args) {

    Scanner input = new Scanner(System.in);

        
System.out.println("Enter the First score");
    int scoreOne = input.nextInt();

System.out.println("Enter the second score");
     int scoreTwoe = input.nextInt();

System.out.println("Enter the third score");
     int scoreThree = input.nextInt();

if(scoreOne < 0 && scoreTwo < 0 && scoreThree < 0 ){
    System.out.println("Invalid Input");
}

int average = scoreOne + scoreTwo + scoreThree / 3;

if(average <= 90 && average <= 100) {
    System.out.println("A")
}

if(average <= 80 && average < 90){
    System.out.println("B");
}
if(average <= 70 && average < 80){
 }   System.out.println("C");

if(average <= 60 && average < 70){
  }  System.out.println("D");

if(average <= 0 && average < 60){
    System.out.println("F")
}
}
}
