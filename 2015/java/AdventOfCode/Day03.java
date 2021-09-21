package AdventOfCode;

import java.util.ArrayList;
import java.util.List;

public class Day03 extends Day {

	public Day03() {
		readInput("input03");
	}
	
	public void part1() {
		String comandos = getLineas().get(0);
		int [] ejes = {0,0};		
		List<String> casas = new ArrayList<>();
		casas.add(ejes[0]+" "+ejes[1]);
		
		for (int i=0; i< comandos.length(); i++) {
			switch (comandos.charAt(i)) {
				case '^':
					ejes[0]++;
					break;
				case 'v':
					ejes[0]--;
					break;
				case '<':
					ejes[1]--;
					break;
				case '>':
					ejes[1]++;
					break;
	
				default:
					break;
			}
			
			if(!casas.contains(ejes[0]+" "+ejes[1])) {
				casas.add(ejes[0]+" "+ejes[1]);
			}
		}
		
		System.out.println("Solucion: " + casas.size());
	}
	
	
	public void part2() {
		String comandos = getLineas().get(0);
		int [] santa = {0,0};
		int [] robot = {0,0};
		List<String> casas = new ArrayList<>();
		casas.add(santa[0]+" "+santa[1]);
		
		for (int i=0; i< comandos.length(); i++) {
			int [] ejes = {0,0};

			if (i % 2 == 0) {
				ejes = santa;
			} else {
				ejes = robot;
			}
			
			switch (comandos.charAt(i)) {
				case '^':
					ejes[0]++;
					break;
				case 'v':
					ejes[0]--;
					break;
				case '<':
					ejes[1]--;
					break;
				case '>':
					ejes[1]++;
					break;
	
				default:
					break;
			}
			
			if(!casas.contains(ejes[0]+" "+ejes[1])) {
				casas.add(ejes[0]+" "+ejes[1]);
			}
			
			if (i % 2 == 0) {
				santa = ejes;
			} else {
				robot = ejes;
			}
			
		}
		
		System.out.println("Solucion: " + casas.size());
	}
	
	public static void main(String[] args) {
	      Day03 day = new Day03();
	      day.part1();
	      day.part2();
	}

}
