package AdventOfCode;

public class Day01 extends Day {

    Day01() {
        readInput("input01");
    }

    public int Parte1() {
        int count1 = (int) getLineas().get(0).codePoints().filter(ch -> ch == '(').count();
        int count2 = (int) getLineas().get(0).codePoints().filter(ch -> ch == ')').count();

        return count1-count2;
    }

    public int Parte2() {
        int level = 0;
        for (int i=0; i<getLineas().get(0).length(); i++){
            if (getLineas().get(0).charAt(i) =='(') {
                level++;
            } else {
                level--;
            }

            if (level == -1) {
                level = i + 1;
                break;
            }
        }
        return level;
    }



   public static void main(String[] args) {
      Day01 day01 = new Day01();
      System.out.println("Solución: " + day01.Parte1());
      System.out.println("Solución: " + day01.Parte2());
   }
}