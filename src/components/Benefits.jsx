import React from 'react';

const Benefits = () => {
    const sectionStyle = {
        padding: '100px 5%',
        backgroundColor: 'var(--background-color)',
        textAlign: 'center',
    };

    const titleStyle = {
        fontSize: '2.5rem',
        fontWeight: '700',
        marginBottom: '60px',
        color: 'var(--text-color)',
        textTransform: 'uppercase',
        letterSpacing: '1px',
    };

    const gridStyle = {
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
        gap: '40px',
        maxWidth: '1200px',
        margin: '0 auto',
    };

    const cardStyle = {
        padding: '40px',
        borderRadius: '16px',
        backgroundColor: 'var(--card-background)',
        transition: 'all 0.3s ease',
        cursor: 'default',
        textAlign: 'left',
        border: '1px solid rgba(255, 255, 255, 0.05)',
    };

    const iconStyle = {
        fontSize: '2rem',
        color: 'var(--primary-color)',
        marginBottom: '20px',
        display: 'block',
        textShadow: '0 0 10px rgba(0, 163, 255, 0.4)',
    };

    const cardTitleStyle = {
        fontSize: '1.5rem',
        fontWeight: '700',
        marginBottom: '16px',
        color: 'var(--text-color)',
    };

    const cardTextStyle = {
        color: 'var(--secondary-text-color)',
        lineHeight: '1.6',
    };

    const benefits = [
        {
            title: "Reducción de Costos",
            desc: "Automatiza hasta el 70% del tiempo administrativo. Deja que la IA maneje lo repetitivo.",
            icon: "📉"
        },
        {
            title: "Implementación Simple",
            desc: "Integración completa en menos de 7 días. Sin interrupciones prolongadas en tu operación.",
            icon: "⚡"
        },
        {
            title: "Ingeniería vs. Teoría",
            desc: "Soluciones probadas y prácticas. No vendemos humo, vendemos eficiencia medible.",
            icon: "⚙️"
        }
    ];

    return (
        <section id="benefits" style={sectionStyle}>
            <h2 style={titleStyle}>Transformamos Datos en Crecimiento Neto.</h2>
            <div style={gridStyle}>
                {benefits.map((item, index) => (
                    <div
                        key={index}
                        style={cardStyle}
                        onMouseEnter={(e) => {
                            e.currentTarget.style.transform = 'translateY(-10px)';
                            e.currentTarget.style.borderColor = 'var(--primary-color)';
                            e.currentTarget.style.boxShadow = '0 10px 30px rgba(0,0,0,0.3)';
                        }}
                        onMouseLeave={(e) => {
                            e.currentTarget.style.transform = 'translateY(0)';
                            e.currentTarget.style.borderColor = 'rgba(255, 255, 255, 0.05)';
                            e.currentTarget.style.boxShadow = 'none';
                        }}
                    >
                        <span style={iconStyle}>{item.icon}</span>
                        <h3 style={cardTitleStyle}>{item.title}</h3>
                        <p style={cardTextStyle}>{item.desc}</p>
                    </div>
                ))}
            </div>
        </section>
    );
};

export default Benefits;
