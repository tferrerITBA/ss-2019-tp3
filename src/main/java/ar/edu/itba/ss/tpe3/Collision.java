package ar.edu.itba.ss.tpe3;

public abstract class Collision {

    protected final Particle particle;
    protected Double time;

    public Collision(final Particle particle) {
        this.particle = particle;
    }

    public abstract void updateTime();

    public void updateTime(double deltaTime) {
        time -= deltaTime;
        if(time.equals(Double.NEGATIVE_INFINITY)) {
        	System.out.println("Unknown Collision - Time is -Inf: " + deltaTime);
        	throw new IllegalStateException("ERROR");
        }
    }

    public Particle getParticle() {
        return particle;
    }

    public Double getTime() {
        return time;
    }

}
