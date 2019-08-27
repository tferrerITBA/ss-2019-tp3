package ar.edu.itba.ss.tpe2;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Objects;
import java.util.Random;

public class Grid {
	
	private List<Particle> particles;
	private double areaBorderLength;
	
	public Grid(List<Particle> particles) {
		this.areaBorderLength = Configuration.AREA_BORDER_LENGTH;
		this.particles = particles;
	}
	
	/*public void executeOffLatice() {
		for(int i = 0; i < Configuration.getTimeLimit(); i++) {
			List<Particle> updatedParticles = new ArrayList<>(Configuration.getParticleCount());
			calculateAllParticlesNeighbors();
			if(Configuration.isSingleRunMode())
				Configuration.writeOvitoOutputFile(i, particles);
			updateParticles(updatedParticles);
			setParticles(updatedParticles);
			updateGridSections();
		}
	}
	
	private void updateParticles(List<Particle> updatedParticles) {
		for(Particle p : particles) {
			Particle updatedParticle = p.clone();
			double newPositionX = p.getPosition().getX() + p.getVelocity().getX() * 1;
			if(newPositionX < 0 || newPositionX > areaBorderLength)
				newPositionX = (newPositionX + areaBorderLength) % areaBorderLength;
			double newPositionY = p.getPosition().getY() + p.getVelocity().getY() * 1;
			if(newPositionY < 0 || newPositionY > areaBorderLength)
				newPositionY = (newPositionY + areaBorderLength) % areaBorderLength;
			updatedParticle.setPosition(newPositionX, newPositionY);
			
			double accumVelocityX = p.getVelocity().getX();
			double accumVelocityY = p.getVelocity().getY();
			for(Particle n : p.getNeighbors()) {
				accumVelocityX += n.getVelocity().getX();
				accumVelocityY += n.getVelocity().getY();
			}
			double eta = Configuration.getEta();
			Random r = new Random();
			double newAngle = Math.atan2(accumVelocityY / (p.getNeighbors().size() + 1), accumVelocityX / (p.getNeighbors().size() + 1))
					+ (-eta/2 + r.nextDouble() * eta);
			double newVelocityX = Math.cos(newAngle) * Configuration.getVelocity();
			double newVelocityY = Math.sin(newAngle) * Configuration.getVelocity();
			updatedParticle.setVelocity(newVelocityX, newVelocityY);
			
			updatedParticles.add(updatedParticle);
		}
	}*/
	
	public double getDensity() {
		return particles.size() / Math.pow(areaBorderLength, 2);
	}
	
	public List<Particle> getParticles() {
		return Collections.unmodifiableList(particles);
	}
	
	public void setParticles(List<Particle> newParticles) {
		Objects.requireNonNull(newParticles);
		particles = newParticles;
	}
	
}
