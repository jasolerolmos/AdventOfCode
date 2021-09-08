import java.util.*;
import java.util.stream.*;
import java.io.*;
import java.nio.file.*;

public class Day01 {
    private List<String> lineas = new ArrayList<>();

    Day01() {
        readInput();
    }

    public int Parte1() {
        int count1 = (int) lineas.get(0).codePoints().filter(ch -> ch == '(').count();
        int count2 = (int) lineas.get(0).codePoints().filter(ch -> ch == ')').count();

        return count1-count2;
    }

    public int Parte2() {
        int level = 0;
        for (int i=0; i<lineas.get(0).length(); i++){
            if (lineas.get(0).charAt(i) =='(') {
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

    private void readInput() {
        String fileName = "../input/input01.txt";

        try {
            Stream<String> stream = Files.lines(Paths.get(fileName));
            lineas = stream.collect(Collectors.toList());
        } catch (Exception e) {
            System.out.println(e);
        }
    }


   public static void main(String[] args) {
      Day01 day01 = new Day01();
      System.out.println("Solución: " + day01.Parte1());
      System.out.println("Solución: " + day01.Parte2());
   }
}