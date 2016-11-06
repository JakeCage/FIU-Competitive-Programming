import java.io.IOException;
import java.util.*;
//import java.math.BigInteger;


public class KattisContest {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException{
        
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int index = 0;
        int counter = 0;
        char[][] arr1 = new char [n][n];
        char[][] arr2 = new char [n][n];
        String msg;
        String line[] = new String[n+1]; 
        
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                arr2[i][j] = '0';
            }
        }
        
        for(int i = 0; i < n; i++){
            line[i] = in.next();
            for(int j = 0; j < n; j++){
                arr1[i][j] = line[i].charAt(j);
                if(arr1[i][j] == '.'){
                        counter++;
                    }
            }
        }
        msg = in.next();
        
       if((Math.ceil(n*n/4.0) != counter)){
           System.out.println("invalid grille");
           return;
       }
       
        for(int k = 0; k < 4; k++){
            for(int i = 0; i < n; i++){
                for(int j = 0; j < n; j++){
                    if(arr1[i][j] == '.'){
                        arr2[i][j] = msg.charAt(index++);
                    }
                }
            }
            rotateByNinetyToRight(arr1);
        }
         //test for invalid
        if((isValid(arr2,n) == false)){
            System.out.println("invalid grille");
        }
        else{
            print2DArr(arr2,n);
        }
        
    }//end of main
    
    public static void swapRows(char [][] m) {
        for (int  i = 0, k = m.length - 1; i < k; ++i, --k) {
            char[] x = m[i];
            m[i] = m[k];
            m[k] = x;
        }
    }
    
    private static void transpose(char [][] m) {

            for (int i = 0; i < m.length; i++) {
                for (int j = i; j < m[0].length; j++) {
                    char x = m[i][j];
                    m[i][j] = m[j][i];
                    m[j][i] = x;
                }
            }
        }

    public static void rotateByNinetyToLeft(char[][] m) {
        transpose(m);
        swapRows(m);
    }

    public static void rotateByNinetyToRight(char[][] m) {
        swapRows(m);
        transpose(m);
    }
    
    public static boolean isValid(char arr[][], int n){
        for(int i = 0; i < n; i++){
                for(int j = 0; j < n; j++){
                    if(arr[i][j] == '0'){
                        return false;
                    }
                }
            }
        return true;
    }

    private static void print2DArr(char[][] arr2,int n) {
        for(int i = 0; i < n; i++){
                for(int j = 0; j < n; j++){
                    System.out.print(arr2[i][j]);
                }
            }
            System.out.println();
    }
}
