package ar.edu.itba.ss.tpe2;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;

public class Main {
	
	private static long startTime;
	
	public static void main(String[] args) {
		Configuration.requestMode();
		
		if(Configuration.isSingleRunMode()) {
			executeSingleRun();
		} else if(Configuration.isCommonTestMode()) {
			runMultipleTests();
		}
		
		long endTime = System.nanoTime();
		System.out.println("Process done in " + TimeUnit.NANOSECONDS.toMillis(endTime - startTime) + " ms.");
	}
	
	private static void executeSingleRun() {
		Configuration.requestParameters();
		startTime = System.nanoTime();
		List<Particle> particles = Configuration.generateRandomInputFilesAndParseConfiguration();
		Grid grid = new Grid(particles);
		// ALGO
		Configuration.writeOvitoOutputFile(0, particles); // BORRAR
	}
	
	private static void runMultipleTests() {
		Configuration.requestParameters();
		startTime = System.nanoTime();
		for(int i = 0; i < Configuration.TEST_CYCLES; i++) {
			List<Particle> particles = Configuration.generateRandomInputFilesAndParseConfiguration();
			Grid grid = new Grid(particles);
			// ALGO
		}
	}

}
