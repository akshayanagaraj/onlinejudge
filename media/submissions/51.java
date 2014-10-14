import java.io.*;
import java.util.Scanner; 
public class Solution
{
   public static void main(String[] args) throws IOException
   {
    
	Scanner input=new Scanner (System.in);
      
      while(true){
         int i=0;
	 
         i = input.nextInt();
         
         if(i != 42)
          System.out.println(i);
         else
          break;
      }

   }
}