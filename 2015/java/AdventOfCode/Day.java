package AdventOfCode;
import java.util.*;
import java.util.stream.*;
import java.nio.file.*;

public class Day  {
    private List<String> lineas = new ArrayList<>();

    public List<String> getLineas() {
		return lineas;
	}

	public void setLineas(List<String> lineas) {
		this.lineas = lineas;
	}

	void readInput(String file) {
        String fileName = "../input/"+file+".txt";

        try {
            Stream<String> stream = Files.lines(Paths.get(fileName));
            lineas = stream.collect(Collectors.toList());
            stream.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }

}