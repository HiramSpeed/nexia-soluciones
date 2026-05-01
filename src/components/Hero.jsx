import React from 'react';
import heroImage from '../assets/hero-nexia.jpeg';

const Hero = ({ openModal }) => {
    return (
        <section id="inicio" className="hero-section">
            <div className="hero-image-wrapper">
                <img
                    src={heroImage}
                    alt="NexIA Soluciones — Automatiza lo Aburrido"
                    className="hero-bg-image"
                />
                <div className="hero-cta-overlay">
                    <button
                        className="hero-cta-btn"
                        onClick={() => openModal('Auditoría Gratuita - Hero')}
                    >
                        AGENDAR AUDITORÍA GRATUITA
                    </button>
                </div>
            </div>
        </section>
    );
};

export default Hero;
