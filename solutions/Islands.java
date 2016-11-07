/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package islands;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

/**
 *
 * @author me
 */
public class Islands {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Islands program = new Islands();
        program.run();
    }
    
    public void run(){
        Scanner in = new Scanner(System.in);
        
        int r = in.nextInt();
        int c = in.nextInt();
        
        char[][] image = new char[r][c];
        boolean[][] visited = new boolean[r][c];
        String row;
        for(int i = 0; i < r; i++){
            row = in.next();
            for(int j = 0; j < c; j++){
                image[i][j] = row.charAt(j);
                visited[i][j] = false;
            }
        }
        
        int islands = 0;
        Queue<Pair> queue = new LinkedList<>();
        Pair temp;
        for(int i = 0; i < r; i++){
            for(int j = 0; j < c; j++){
                if(image[i][j] == 'L' && !visited[i][j]){
                    queue.add(new Pair(i,j));
                    visited[i][j] = true;
                    while(!queue.isEmpty()){
                        temp = queue.poll();
                        if(temp.i+1 < r){
                            if(visited[temp.i+1][temp.j] == false && (image[temp.i+1][temp.j] == 'L' || image[temp.i+1][temp.j] == 'C')){
                                queue.add(new Pair(temp.i+1, temp.j));
                                visited[temp.i+1][temp.j] = true;
                            }
                        }
                        
                        if(temp.i-1 >= 0){
                            if(visited[temp.i-1][temp.j] == false && (image[temp.i-1][temp.j] == 'L' || image[temp.i-1][temp.j] == 'C')){
                                queue.add(new Pair(temp.i-1, temp.j));
                                visited[temp.i-1][temp.j] = true;
                            }
                        }
                        
                        if(temp.j+1 < c){
                            if(visited[temp.i][temp.j+1] == false && (image[temp.i][temp.j+1] == 'L' || image[temp.i][temp.j+1] == 'C')){
                                queue.add(new Pair(temp.i, temp.j+1));
                                visited[temp.i][temp.j+1] = true;
                            }
                        }
                        
                        if(temp.j-1 >= 0){
                            if(visited[temp.i][temp.j-1] == false && (image[temp.i][temp.j-1] == 'L' || image[temp.i][temp.j-1] == 'C')){
                                queue.add(new Pair(temp.i, temp.j-1));
                                visited[temp.i][temp.j-1] = true;
                            }
                        } 
                    }
                    islands++;
                }
            }
        }
        System.out.println(islands);
        in.close();
    }
    
}

class Pair{
    int i;
    int j;
    
    public Pair(int x, int y){
        i = x;
        j = y;
    }
}