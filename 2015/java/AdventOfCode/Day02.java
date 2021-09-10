package AdventOfCode;

import java.util.Arrays;

public class Day02 extends Day {
    Day02() {
        super.readInput("input02");
    }

    private int[] valores(String regalo) {
    	int[] input = {0,0,0};
    	String[] l = regalo.split("x");
    	for (int i=0; i<l.length; i++){
    		input[i] = Integer.parseInt(l[i]);
    	}
    	Arrays.sort(input);

    	int[] temp = {0,0,0};
    	temp[0] = 2*input[0] * input[1];
    	temp[1] = 2*input[0] * input[2];
    	temp[2] = 2*input[1] * input[2];
    	Arrays.sort(temp);

    	int[] sol = {0,0};
    	sol[0] = Arrays.stream(temp).sum() + temp[0]/2;
    	sol[1] = input[0]*2 + input[1]*2 + (input[0]*input[1]*input[2]);
    	
    	return sol;
    }
    
    public void parte1_2() {
        int part1 = 0;
        int part2 = 0;
        
        for (int i=0; i<getLineas().size(); i++){
        	int[] s = valores(getLineas().get(i));
        	part1 += s[0];
        	part2 += s[1];
        }

        System.out.println("Solución:\n\t" + part1 + "\n\t" + part2);
    }

   public static void main(String[] args) {
      Day02 day02 = new Day02();
      day02.parte1_2();
   }
}