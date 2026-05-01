import React from 'react';

const Testimonials = () => {
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
        maxWidth: '1000px',
        margin: '0 auto',
    };

    const cardStyle = {
        backgroundColor: 'var(--card-background)',
        padding: '40px',
        borderRadius: '16px',
        boxShadow: '0 10px 30px rgba(0,0,0,0.2)',
        textAlign: 'left',
        position: 'relative',
        border: '1px solid rgba(255, 255, 255, 0.05)',
    };

    const quoteStyle = {
        fontSize: '1.1rem',
        color: 'var(--secondary-text-color)',
        fontStyle: 'italic',
        marginBottom: '20px',
        lineHeight: '1.6',
    };

    const authorStyle = {
        fontWeight: '700',
        color: 'var(--primary-color)',
    };

    const roleStyle = {
        fontSize: '0.9rem',
        color: 'var(--secondary-text-color)',
        opacity: 0.8,
    };

    const testimonials = [
        {
            quote: "La implementación de NexIA redujo nuestros tiempos de respuesta en un 60%. Es impresionante ver cómo la IA maneja tareas que antes nos tomaban horas.",
            author: "Carlos Rodríguez",
            role: "Director de Operaciones, TechFlow"
        },
        {
            quote: "No solo es software, es una consultoría estratégica. Entendieron nuestro negocio y diseñaron una solución que se pagó sola en 3 meses.",
            author: "Ana Martínez",
            role: "CEO, Innova Retail"
        }
    ];

    return (
        <section id="testimonials" style={sectionStyle}>
            <h2 style={titleStyle}>Nuestros Clientes lo Confirman.</h2>
            <div style={gridStyle}>
                {testimonials.map((item, index) => (
                    <div key={index} style={cardStyle}>
                        <p style={quoteStyle}>"{item.quote}"</p>
                        <div>
                            <div style={authorStyle}>{item.author}</div>
                            <div style={roleStyle}>{item.role}</div>
                        </div>
                    </div>
                ))}
            </div>
        </section>
    );
};

export default Testimonials;
