import React from 'react';
import Button from './Button';
import logo from '../assets/logo.png';

const Hero = ({ openModal }) => {
    const sectionStyle = {
        minHeight: '100vh',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        textAlign: 'center',
        padding: '120px 20px 60px',
        background: 'radial-gradient(circle at 50% 50%, #2d3748 0%, #1a202c 100%)',
        position: 'relative',
        overflow: 'hidden',
    };

    const logoStyle = {
        width: '320px',
        height: 'auto',
        marginBottom: '50px',
        filter: 'drop-shadow(0 0 30px rgba(0, 163, 255, 0.5))',
        animation: 'float 6s ease-in-out infinite',
    };

    const titleStyle = {
        fontSize: '4rem',
        fontWeight: '700',
        lineHeight: '1.1',
        marginBottom: '24px',
        maxWidth: '900px',
        color: 'var(--text-color)',
        textTransform: 'uppercase',
        letterSpacing: '2px',
    };

    const subtitleStyle = {
        fontSize: '1.25rem',
        color: 'var(--secondary-text-color)',
        marginBottom: '40px',
        maxWidth: '600px',
        lineHeight: '1.6',
    };

    const highlightStyle = {
        color: 'var(--primary-color)',
        textShadow: '0 0 20px rgba(0, 163, 255, 0.5)',
    };

    return (
        <section style={sectionStyle}>
            <style>
                {`
          @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0px); }
          }
        `}
            </style>

            <img src={logo} alt="NexIA Soluciones Logo" style={logoStyle} />

            <h1 style={titleStyle}>
                Automatiza lo Aburrido. <br />
                <span style={highlightStyle}>Enfócate en Crecer.</span>
            </h1>
            <p style={subtitleStyle}>
                Implementamos soluciones de IA que trabajan para ti, no al revés.
            </p>
            <Button variant="primary" style={{ padding: '16px 32px', fontSize: '1.1rem' }} onClick={() => openModal('Auditoría Gratuita - Hero')}>
                Quiero mi Auditoría Gratuita de IA
            </Button>

            {/* Abstract Background Element */}
            <div style={{
                position: 'absolute',
                top: '50%',
                left: '50%',
                transform: 'translate(-50%, -50%)',
                width: '800px',
                height: '800px',
                background: 'radial-gradient(circle, rgba(0, 163, 255, 0.1) 0%, rgba(26, 32, 44, 0) 70%)',
                zIndex: 0,
                pointerEvents: 'none',
            }} />
        </section>
    );
};

export default Hero;
