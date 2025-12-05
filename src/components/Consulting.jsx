import React from 'react';
import Button from './Button';

const Consulting = ({ openModal }) => {
    const sectionStyle = {
        padding: '100px 5%',
        backgroundColor: 'var(--background-color)',
        textAlign: 'center',
    };

    const titleStyle = {
        fontSize: '2.5rem',
        fontWeight: '700',
        marginBottom: '20px',
        color: 'var(--text-color)',
        textTransform: 'uppercase',
        letterSpacing: '1px',
    };

    const subtitleStyle = {
        fontSize: '1.2rem',
        color: 'var(--secondary-text-color)',
        marginBottom: '60px',
        maxWidth: '800px',
        marginLeft: 'auto',
        marginRight: 'auto',
    };

    const servicesStyle = {
        display: 'flex',
        flexWrap: 'wrap',
        justifyContent: 'center',
        gap: '20px',
        marginBottom: '60px',
    };

    const tagStyle = {
        padding: '10px 20px',
        backgroundColor: 'rgba(0, 163, 255, 0.1)',
        borderRadius: '50px',
        color: 'var(--primary-color)',
        fontWeight: '600',
        fontSize: '0.9rem',
        border: '1px solid var(--primary-color)',
    };

    return (
        <section id="consulting" style={sectionStyle}>
            <h2 style={titleStyle}>¿Necesitas más que una App? Diseñamos tu IA a Medida.</h2>
            <p style={subtitleStyle}>
                Desarrollamos soluciones personalizadas para optimizar tus procesos específicos.
            </p>

            <div style={servicesStyle}>
                <span style={tagStyle}>Optimización de cadenas de suministro</span>
                <span style={tagStyle}>Predicción de demanda</span>
                <span style={tagStyle}>Integración con ERP/CRM</span>
                <span style={tagStyle}>Automatización de flujos de trabajo</span>
                <span style={tagStyle}>Análisis predictivo</span>
            </div>

            <Button variant="primary" onClick={() => openModal('Llamada Estratégica')}>Solicitar una Llamada Estratégica</Button>
        </section>
    );
};

export default Consulting;
