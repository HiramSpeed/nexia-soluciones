import React from 'react';
import { Link } from 'react-router-dom';
import Button from './Button';

const ProductsTeaser = () => {
    const sectionStyle = {
        padding: '100px 5%',
        textAlign: 'center',
        backgroundColor: 'var(--background-color)',
    };

    const titleStyle = {
        fontSize: '2.5rem',
        marginBottom: '60px',
        color: 'var(--text-color)',
        textTransform: 'uppercase',
    };

    const iconsContainerStyle = {
        display: 'flex',
        justifyContent: 'center',
        gap: '60px',
        marginBottom: '60px',
        flexWrap: 'wrap',
    };

    const iconBoxStyle = {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        gap: '20px',
    };

    const iconCircleStyle = {
        width: '80px',
        height: '80px',
        borderRadius: '50%',
        backgroundColor: 'rgba(0, 163, 255, 0.1)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        color: 'var(--primary-color)',
    };

    return (
        <section style={sectionStyle}>
            <h2 style={titleStyle}>Ecosistema de Soluciones</h2>
            <p style={{ color: '#CBD5E0', maxWidth: '42rem', margin: '0 auto 60px', lineHeight: '1.6', fontSize: '1.1rem' }}>
                Integramos seguridad, administración y automatización en una sola suite tecnológica. Nuestras herramientas no son islas aisladas; son módulos conectados que comparten datos para blindar tu operación y acelerar tu crecimiento.
            </p>

            <div style={iconsContainerStyle}>
                <div style={iconBoxStyle}>
                    <div style={iconCircleStyle}>
                        <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                    </div>
                    <span style={{ color: 'var(--secondary-text-color)', fontWeight: '600' }}>Seguridad</span>
                </div>
                <div style={iconBoxStyle}>
                    <div style={iconCircleStyle}>
                        <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>
                    </div>
                    <span style={{ color: 'var(--secondary-text-color)', fontWeight: '600' }}>Gestión</span>
                </div>
                <div style={iconBoxStyle}>
                    <div style={iconCircleStyle}>
                        <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><line x1="12" y1="2" x2="12" y2="6"></line><line x1="12" y1="18" x2="12" y2="22"></line><line x1="4.93" y1="4.93" x2="7.76" y2="7.76"></line><line x1="16.24" y1="16.24" x2="19.07" y2="19.07"></line><line x1="2" y1="12" x2="6" y2="12"></line><line x1="18" y1="12" x2="22" y2="12"></line><line x1="4.93" y1="19.07" x2="7.76" y2="16.24"></line><line x1="16.24" y1="7.76" x2="19.07" y2="4.93"></line></svg>
                    </div>
                    <span style={{ color: 'var(--secondary-text-color)', fontWeight: '600' }}>Automation</span>
                </div>
            </div>

            <Link to="/productos">
                <Button variant="primary" style={{ padding: '15px 40px', fontSize: '1.1rem' }}>
                    VER CATÁLOGO DE APPS
                </Button>
            </Link>
        </section>
    );
};

export default ProductsTeaser;
