/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package zigzag;

import java.util.Scanner;

/**
 *
 * @author me
 */
public class Zigzag {

    
    public static void main(String[] args) {
        Zigzag program = new Zigzag();
        program.run();
    }
    public void run(){
        Scanner in = new Scanner(System.in);
        
        int n = in.nextInt();
        int[] nums = new int[n];
        for(int i = 0; i < n; i++){
            nums[i] = in.nextInt();
        }
        
        int winner = 1;
        boolean inc = true; boolean dec = true;
        
        for(int i = 0; i < n-1; i++){
            if(nums[i] == nums[i+1]){
                continue;
            }
            if(nums[i] < nums[i+1] && inc){
                inc = false;
                dec = true;
            }
            if(nums[i] > nums[i+1] && dec){
                winner++; inc = true; dec = false;
            }
        }
        System.out.println(winner);
        in.close();
    }
    
}
