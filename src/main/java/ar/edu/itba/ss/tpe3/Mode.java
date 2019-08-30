package ar.edu.itba.ss.tpe3;

import java.util.Arrays;
import java.util.Optional;

public enum Mode {
	SINGLE_RUN (0), 
	MULTIPLE_TEST (1);
	
	private int mode;
	
	Mode(int mode) {
		this.mode = mode;
	}
	
	public int getMode() {
		return mode;
	}
	
	public static Optional<Mode> valueOf(int value) {
		return Arrays.stream(values()).filter(m -> m.getMode() == value).findFirst();
	}
}
