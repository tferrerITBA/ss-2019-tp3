package ar.edu.itba.ss.tpe2;

public abstract class Collision {
	
	protected final Particle particle;
	protected Double time;
	
	public Collision(final Particle particle) {
		this.particle = particle;
	}
	
	public abstract void updateTime();

	public Particle getParticle() {
		return particle;
	}
	
	public Double getTime() {
		return time;
	}

}
