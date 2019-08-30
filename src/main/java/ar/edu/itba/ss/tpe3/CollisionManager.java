package ar.edu.itba.ss.tpe3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Stream;

public class CollisionManager {
	
	private final Grid grid;
	private final List<Collision> particleCollisions;
	private final List<Collision> borderCollisions;
	
	public CollisionManager(final Grid grid) {
		this.grid = grid;
		this.particleCollisions = new ArrayList<>();
		this.borderCollisions = new ArrayList<>();
	}
	
	public void executeAlgorithm() {
		initializeCollisions();
		for(int i = 0; i < Configuration.getTimeLimit(); i++) {
			if(Configuration.isSingleRunMode())
				Configuration.writeOvitoOutputFile(i, grid.getParticles());
			
			Collision firstCollision = getFirstCollision();
			grid.updateParticles(firstCollision.getTime());
			
			updateCollisionVelocities(firstCollision);
			
			for(Collision c : particleCollisions) {
				// SI NO INTERFIERE RESTAR TIEMPO
				// SINO CALCULAR NUEVO TIEMPO
			}
			for(Collision c : borderCollisions) {
				// SI NO INTERFIERE RESTAR TIEMPO
				// SINO CALCULAR NUEVO TIEMPO
			}
		}
	}

	private void initializeCollisions() {
		for(int i = 0; i < grid.getParticles().size(); i++) {
			Particle p1 = grid.getParticles().get(i);
			for(int j = i + 1; j < grid.getParticles().size(); j++) {
				Particle p2 = grid.getParticles().get(j);
				initializeParticleCollision(p1, p2);
			}
			initializeBorderCollisions(p1);
		}
	}
	
	private void initializeParticleCollision(Particle particle, Particle otherParticle) {
		particleCollisions.add(new ParticleCollision(particle, otherParticle));
	}

	private void initializeBorderCollisions(Particle particle) {
		borderCollisions.addAll(Arrays.asList(
				new BorderCollision(particle, Border.HORIZONTAL, grid.getAreaBorderLength()), 
				new BorderCollision(particle, Border.VERTICAL, grid.getAreaBorderLength())
			));
	}
	
	private Collision getFirstCollision() {
		return Stream.of(particleCollisions, borderCollisions).flatMap(c -> c.stream())
				.min(Comparator.comparing(Collision::getTime)).get();
	}
	
	private void updateCollisionVelocities(Collision collision) {
		Particle collisionParticle = collision.getParticle();
		if(collision instanceof ParticleCollision) {
			ParticleCollision particleCollision = (ParticleCollision) collision;
			Particle collisionOtherParticle = particleCollision.getOtherParticle();
			// TO-DO
		} else if(collision instanceof BorderCollision) {
			BorderCollision borderCollision = (BorderCollision) collision;
			if(borderCollision.getBorder().equals(Border.VERTICAL)) {
				collisionParticle.setVelocity(- collisionParticle.getVelocity().getX(), collisionParticle.getVelocity().getY());
			} else {
				collisionParticle.setVelocity(collisionParticle.getVelocity().getX(), - collisionParticle.getVelocity().getY());
			}
		}
	}

}
