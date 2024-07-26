import java.util.Random;
import java.util.Scanner;

class GussGame{
    int compGen;
    int userInp;
    int count;

    public GussGame(){
        Random random=new Random();
        compGen=random.nextInt(101);
    }
    public int userInput(){
        System.out.println("Enter Number between 0 to 100 ");
        System.out.print("Enter Number: ");
        Scanner sc=new Scanner(System.in);
        userInp=sc.nextInt();
        count++;
        return userInp;
    }
}


public class GussTheNumber {
    //Scaneer class object must be declared inside the main function
    public static void main(String[] args) {
        System.out.println("Welcome to Guss Game\n**************************");
        System.out.println("You Have 10 Gusses\n**************************");
        GussGame game=new GussGame();
        int takeInput;
        int gusses=10;
        while(gusses>0){
            takeInput=game.userInput();
            if(takeInput==game.compGen){
                System.out.println("***************************\nYou Won......");
                System.out.println("Number of Gusses: "+game.count);
                System.out.println("***************************");
                break;
            } else if (takeInput<game.compGen) {
                System.out.println("Your Input is Smaller\nThink bigger number");
            }
            else {
                System.out.println("Your Input is Bigger\nThink smaller number");
            }
            gusses--;
            if(gusses==0){
                System.out.println("*************************\nGAME OVER\n*************************");
                System.out.println("You are a Looser\n************************** !");
                break;
            }
        }
    }

}
