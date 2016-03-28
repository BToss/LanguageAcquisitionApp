/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

public class BarkDifferenceTest {
    //This java program needs to be given values as formant 1, 2 and 3
    //Or it could take it as farray[]
    static double[] zarray = new double[3];
 
    static double[] farray = new double[3];
    static double x;
    static double y;
    
    public static void main(String[] args) {
    	for (int j = 0; j<(3*5);j+=3){
    		farray[0] = Double.parseDouble(args[j]);
    		farray[1] = Double.parseDouble(args[j+1]);
    		farray[2] = Double.parseDouble(args[j+2]);
    		
         for(int i = 0; i < 3; i++){
            zarray[i] = (26.81/(1+ (1960/ farray[i])))-0.53;
        }
        x = zarray[2] - zarray[1];
        y = zarray[2] - zarray[0];
        
        System.out.println(j + "   "+x + "," + y);
    	}
    }
    
}