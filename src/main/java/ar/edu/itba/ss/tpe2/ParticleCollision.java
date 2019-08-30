package ar.edu.itba.ss.tpe2;

import java.awt.geom.Point2D;

public class ParticleCollision extends Collision {

	private final Particle otherParticle;
	
	public ParticleCollision(final Particle particle, final Particle otherParticle) {
		super(particle);
		this.otherParticle = otherParticle;
		updateTime();
	}
	
	public void updateTime() {
		Point2D.Double deltaPosition = new Point2D.Double(particle.getPosition().getX() - otherParticle.getPosition().getX(),
				particle.getPosition().getY() - otherParticle.getPosition().getY());
		Point2D.Double deltaVelocity = new Point2D.Double(particle.getVelocity().getX() - otherParticle.getVelocity().getX(),
				particle.getVelocity().getY() - otherParticle.getVelocity().getY());
		
		double deltaVDeltaP = (deltaVelocity.getX() * deltaPosition.getX()) + (deltaVelocity.getY() * deltaPosition.getY());
		double deltaVDeltaV = (deltaVelocity.getX() * deltaVelocity.getX()) + (deltaVelocity.getY() * deltaVelocity.getY());
		double deltaPDeltaP = (deltaPosition.getX() * deltaPosition.getX()) + (deltaPosition.getY() * deltaPosition.getY());
		double sigma = particle.getRadius() + otherParticle.getRadius();
		
		double d = (deltaVDeltaP * deltaVDeltaP) - deltaVDeltaV * (deltaPDeltaP - (sigma * sigma));
		
		if(Double.compare(deltaVDeltaP, 0.0) >= 0 || Double.compare(d, 0.0) < 0) {
			time = Double.POSITIVE_INFINITY;
		} else {
			time = - ((deltaVDeltaP + Math.sqrt(d)) / deltaVDeltaV);
		}
	}
	
	public Particle getOtherParticle() {
		return otherParticle;
	}
	
}
