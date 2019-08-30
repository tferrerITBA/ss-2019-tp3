package ar.edu.itba.ss.tpe3;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Objects;

public class Grid {

    private List<Particle> particles;
    private double areaBorderLength;

    public Grid(List<Particle> particles) {
        this.areaBorderLength = Configuration.AREA_BORDER_LENGTH;
        this.particles = particles;
    }

    public void updateParticles(double deltaTime) {
        List<Particle> updatedParticles = new ArrayList<>(particles.size()); // NO CLONAR, GUARDAR DOUBLES NOMAS
        for(Particle p : particles) {
            Particle updatedParticle = p.clone();
            double newPositionX = p.getPosition().getX() + p.getVelocity().getX() * deltaTime;
            double newPositionY = p.getPosition().getY() + p.getVelocity().getY() * deltaTime;
            updatedParticle.setPosition(newPositionX, newPositionY);

            updatedParticles.add(updatedParticle);
        }
        for(int i = 0; i < particles.size(); i++) {
            particles.get(i).setPosition(updatedParticles.get(i).getPosition().getX(), updatedParticles.get(i).getPosition().getY());
        }
        //setParticles(updatedParticles);
    }

    public double getDensity() {
        return particles.size() / Math.pow(areaBorderLength, 2);
    }

    public List<Particle> getParticles() {
        return Collections.unmodifiableList(particles);
    }

    public double getAreaBorderLength() {
        return areaBorderLength;
    }

    public void setParticles(List<Particle> newParticles) {
        Objects.requireNonNull(newParticles);
        particles = newParticles;
    }

}
