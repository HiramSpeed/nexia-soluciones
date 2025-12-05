import React from 'react';
import Button from './Button';

const Academy = ({ openModal }) => {
    const sectionStyle = {
        padding: '100px 5%',
        backgroundColor: '#171923', // Darker background for contrast
        color: '#FFFFFF',
        textAlign: 'center',
    };

    const titleStyle = {
        fontSize: '2.5rem',
        fontWeight: '700',
        marginBottom: '60px',
        color: '#FFFFFF',
        textTransform: 'uppercase',
        letterSpacing: '1px',
    };

    const gridStyle = {
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
        gap: '30px',
        maxWidth: '1200px',
        margin: '0 auto 60px',
    };

    const courseCardStyle = {
        backgroundColor: 'rgba(255, 255, 255, 0.05)',
        padding: '30px',
        borderRadius: '12px',
        textAlign: 'left',
        backdropFilter: 'blur(10px)',
        border: '1px solid rgba(255, 255, 255, 0.1)',
        transition: 'transform 0.3s ease',
    };

    const courseTitleStyle = {
        fontSize: '1.25rem',
        fontWeight: '700',
        marginBottom: '10px',
        color: 'var(--primary-color)',
    };

    const courseDescStyle = {
        color: 'var(--secondary-text-color)',
        fontSize: '0.95rem',
    };

    const courses = [
        {
            title: "Fundamentos del Asistente IA",
            desc: "Aprende a configurar y utilizar asistentes virtuales para potenciar tu productividad diaria."
        },
        {
            title: "Seguridad Inteligente",
            desc: "Protege tus datos y sistemas con las últimas tecnologías de ciberseguridad impulsada por IA."
        },
        {
            title: "El Mindset del CTO Moderno",
            desc: "Estrategias de liderazgo tecnológico para la era de la automatización."
        }
    ];

    return (
        <section id="academy" style={sectionStyle}>
            <h2 style={titleStyle}>De Usuario a Arquitecto de la Automatización.</h2>

            <div style={gridStyle}>
                {courses.map((course, index) => (
                    <div
                        key={index}
                        style={courseCardStyle}
                        onMouseEnter={(e) => e.currentTarget.style.transform = 'translateY(-5px)'}
                        onMouseLeave={(e) => e.currentTarget.style.transform = 'translateY(0)'}
                    >
                        <h3 style={courseTitleStyle}>{course.title}</h3>
                        <p style={courseDescStyle}>{course.desc}</p>
                    </div>
                ))}
            </div>

            <Button variant="secondary" onClick={() => openModal('Guía Gratuita - Academia')}>
                Descargar Guía Gratuita y Recibir Novedades
            </Button>
        </section>
    );
};

export default Academy;
