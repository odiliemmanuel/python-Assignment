import random
maximum = 12

minimum = 1

    int randomNumber = random.nextInt((maximum - minimum) + 1);

   

        int number = 0;


        while(number != randomNumber){
         
    System.out.println("Enter and guess my number ");
         number = input.nextInt();
        

        if(number > randomNumber){
            System.out.println("Too high, guess again");
        }
        if(number < randomNumber) {
            System.out.println("Too low, guess again");

    }
        if(number == randomNumber) {
            System.out.println("Congrats Ugo, play again sometime 😊️");
        }
       
    
        }
}
    }
