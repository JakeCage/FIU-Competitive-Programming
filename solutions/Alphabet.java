/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package alphabet;

import java.util.Scanner;

/**
 *
 * @author me
 */
public class Alphabet {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Alphabet program = new Alphabet();
        program.run();
    }
    public void run(){
        Scanner in = new Scanner(System.in);
        
        char[] s = in.next().toCharArray();
        int n = s.length;
        Pair[] chars = new Pair[n];
        
        for(int i = 0; i < n-1;i++){
            chars[i] = new Pair(s[i], 1);
        }
        chars[n-1] = new Pair(s[n-1],0);
        
        for (int i = n-2; i >= 0; i--){
            for(int j = i+1; j<n; j++){
                if(chars[i].c >= chars[j].c){
                } else {
                    if (chars[i].length <= chars[j].length){
                        chars[i].length = chars[j].length+1;
                        chars[i].next = j;
                    }
                }     
            }
        }
        int max = 0;
        for (int i = 0; i < n; i++){
            if (chars[i].length > max){
                max = chars[i].length;
            }
        }
    }
    }

class Pair{
    char c;
    int next;
    int length;
    
    public Pair(char a, int y){
        c = a;
        next = y;
        length = 1;
    }
    
}