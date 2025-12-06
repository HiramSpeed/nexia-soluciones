import React from 'react';
import Button from './Button';
import logo from '../assets/logo.png';

const Hero = ({ openModal }) => {
    return (
        <section className="hero-section">
            <style>
                {`
          @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0px); }
          }
        `}
            </style>

            <img src={logo} alt="NexIA Soluciones Logo" className="hero-logo" />

            <h1 className="hero-title">
                Automatiza lo Aburrido. <br />
                <span className="hero-highlight">Enfócate en Crecer.</span>
            </h1>
            <p className="hero-subtitle">
                Implementamos soluciones de IA que trabajan para ti, no al revés.
            </p>
            <Button variant="primary" style={{ padding: '16px 32px', fontSize: '1.1rem' }} onClick={() => openModal('Auditoría Gratuita - Hero')}>
                Quiero mi Auditoría Gratuita de IA
            </Button>

            {/* Abstract Background Element */}
            <div className="hero-bg-element" />
        </section>
    );
};

export default Hero;
