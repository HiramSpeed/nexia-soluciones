import React from 'react';

const MissionVision = () => {
    const sectionStyle = {
        padding: '100px 5%',
        backgroundColor: '#1E2530', // Gris oscuro/Azul profundo diferente al fondo principal
        color: '#FFFFFF',
    };

    const containerStyle = {
        maxWidth: '1200px',
        margin: '0 auto',
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
        gap: '60px',
        alignItems: 'start',
    };

    const headerStyle = {
        textAlign: 'center',
        marginBottom: '60px',
    };

    const titleStyle = {
        fontSize: '2.5rem',
        fontWeight: '700',
        textTransform: 'uppercase',
        letterSpacing: '1px',
        color: '#FFFFFF',
        marginBottom: '20px',
        fontFamily: 'var(--font-heading)',
    };

    const cardStyle = {
        display: 'flex',
        flexDirection: 'column',
        gap: '20px',
    };

    const cardTitleStyle = {
        fontSize: '1.8rem',
        fontWeight: '700',
        color: 'var(--primary-color)',
        fontFamily: 'var(--font-heading)',
        borderBottom: '2px solid rgba(0, 163, 255, 0.3)',
        paddingBottom: '10px',
        display: 'inline-block',
        width: 'fit-content',
    };

    const textStyle = {
        fontSize: '1.1rem',
        lineHeight: '1.8',
        color: 'var(--secondary-text-color)',
        textAlign: 'justify',
    };

    return (
        <section id="filosofia" style={sectionStyle}>
            <div style={headerStyle}>
                <h2 style={titleStyle}>Tecnología Accesible, Resultados Reales</h2>
            </div>

            <div style={containerStyle}>
                <div style={cardStyle}>
                    <h3 style={cardTitleStyle}>Nuestra Misión</h3>
                    <p style={textStyle}>
                        Democratizar la automatización inteligente y la eficiencia operativa en México. Transformamos desde pequeños negocios hasta plantas industriales, integrando Agentes de IA y soluciones de causa raíz accesibles que garantizan resultados financieros medibles.
                    </p>
                </div>

                <div style={cardStyle}>
                    <h3 style={cardTitleStyle}>Nuestra Visión</h3>
                    <p style={textStyle}>
                        Ser el motor de cambio tecnológico que redefine la operatividad empresarial, logrando que cualquier organización, sin importar su tamaño, compita globalmente gracias a la fusión estratégica de ingeniería de procesos e Inteligencia Artificial.
                    </p>
                </div>
            </div>
        </section>
    );
};

export default MissionVision;
