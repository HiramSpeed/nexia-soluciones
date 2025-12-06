import React from 'react';
import Button from './Button';

const Footer = ({ openPrivacy }) => {
    const footerStyle = {
        backgroundColor: '#111319', // Very dark footer
        color: '#FFFFFF',
        padding: '80px 5% 40px',
        borderTop: '1px solid rgba(255, 255, 255, 0.05)',
    };

    const containerStyle = {
        maxWidth: '1200px',
        margin: '0 auto',
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
        gap: '60px',
    };

    const columnStyle = {
        display: 'flex',
        flexDirection: 'column',
        gap: '20px',
    };

    const titleStyle = {
        fontSize: '1.5rem',
        fontWeight: '700',
        marginBottom: '10px',
        color: '#FFFFFF',
        fontFamily: 'var(--font-heading)',
        letterSpacing: '1px',
    };

    const linkStyle = {
        color: 'var(--secondary-text-color)',
        textDecoration: 'none',
        transition: 'color 0.2s',
        cursor: 'pointer',
    };

    const formStyle = {
        display: 'flex',
        flexDirection: 'column',
        gap: '15px',
    };

    const inputStyle = {
        padding: '12px',
        borderRadius: '8px',
        border: '1px solid #333',
        backgroundColor: '#1A1A1A',
        color: '#FFFFFF',
        fontFamily: 'inherit',
        outline: 'none',
    };

    return (
        <footer style={footerStyle}>
            <div style={containerStyle}>
                <div style={columnStyle}>
                    <div style={titleStyle}>NexIA Soluciones</div>
                    <p style={{ color: 'var(--secondary-text-color)', lineHeight: '1.6' }}>
                        Automatiza lo Aburrido. Enfócate en Crecer.<br />
                        Soluciones de IA para empresas visionarias.
                    </p>
                    <div style={{ marginTop: '20px', display: 'flex', flexDirection: 'column', gap: '12px' }}>
                        <div>
                            <div style={{ fontSize: '0.85rem', color: 'var(--secondary-text-color)', marginBottom: '4px' }}>Consultas Generales</div>
                            <a href="mailto:info@nexiasoluciones.com.mx" style={{ ...linkStyle, color: 'var(--primary-color)' }}>
                                info@nexiasoluciones.com.mx
                            </a>
                        </div>
                        <div>
                            <div style={{ fontSize: '0.85rem', color: 'var(--secondary-text-color)', marginBottom: '4px' }}>Ventas y Cotizaciones</div>
                            <a href="mailto:ventas@nexiasoluciones.com.mx" style={{ ...linkStyle, color: 'var(--primary-color)' }}>
                                ventas@nexiasoluciones.com.mx
                            </a>
                            <div style={{ fontSize: '0.9rem', color: 'var(--text-color)', marginTop: '4px' }}>
                                <a href="tel:+524611807955" style={{ ...linkStyle, color: 'var(--primary-color)' }}>+(52) 461 180 7955</a>
                            </div>
                        </div>
                        <div>
                            <div style={{ fontSize: '0.85rem', color: 'var(--secondary-text-color)', marginBottom: '4px' }}>Soporte Técnico</div>
                            <a href="mailto:soporte@nexiasoluciones.com.mx" style={{ ...linkStyle, color: 'var(--primary-color)' }}>
                                soporte@nexiasoluciones.com.mx
                            </a>
                        </div>
                    </div>
                </div>

                <div style={columnStyle}>
                    <h3 style={{ fontSize: '1.2rem', fontWeight: '700' }}>Enlaces Rápidos</h3>
                    <a href="#benefits" style={linkStyle} onMouseEnter={(e) => e.target.style.color = 'var(--primary-color)'} onMouseLeave={(e) => e.target.style.color = 'var(--secondary-text-color)'}>Beneficios</a>
                    <a href="#products" style={linkStyle} onMouseEnter={(e) => e.target.style.color = 'var(--primary-color)'} onMouseLeave={(e) => e.target.style.color = 'var(--secondary-text-color)'}>Productos</a>
                    <a href="#consulting" style={linkStyle} onMouseEnter={(e) => e.target.style.color = 'var(--primary-color)'} onMouseLeave={(e) => e.target.style.color = 'var(--secondary-text-color)'}>Consultoría</a>
                    <a href="#academy" style={linkStyle} onMouseEnter={(e) => e.target.style.color = 'var(--primary-color)'} onMouseLeave={(e) => e.target.style.color = 'var(--secondary-text-color)'}>Academia</a>
                    <button
                        onClick={openPrivacy}
                        style={{
                            ...linkStyle,
                            background: 'none',
                            border: 'none',
                            padding: 0,
                            fontFamily: 'inherit',
                            fontSize: 'inherit',
                            textAlign: 'left',
                            cursor: 'pointer'
                        }}
                        onMouseEnter={(e) => e.target.style.color = 'var(--primary-color)'}
                        onMouseLeave={(e) => e.target.style.color = 'var(--secondary-text-color)'}
                    >
                        Aviso de Privacidad
                    </button>
                </div>

                <div style={columnStyle}>
                    <h3 style={{ fontSize: '1.2rem', fontWeight: '700' }}>Contáctanos</h3>
                    <form style={formStyle} onSubmit={(e) => e.preventDefault()}>
                        <input
                            type="text"
                            placeholder="Nombre"
                            style={inputStyle}
                            onFocus={(e) => e.target.style.borderColor = 'var(--primary-color)'}
                            onBlur={(e) => e.target.style.borderColor = '#333'}
                        />
                        <input
                            type="email"
                            placeholder="Correo Electrónico"
                            style={inputStyle}
                            onFocus={(e) => e.target.style.borderColor = 'var(--primary-color)'}
                            onBlur={(e) => e.target.style.borderColor = '#333'}
                        />
                        <input
                            type="tel"
                            placeholder="Celular"
                            style={inputStyle}
                            onFocus={(e) => e.target.style.borderColor = 'var(--primary-color)'}
                            onBlur={(e) => e.target.style.borderColor = '#333'}
                        />
                        <textarea
                            placeholder="Mensaje"
                            rows="3"
                            style={inputStyle}
                            onFocus={(e) => e.target.style.borderColor = 'var(--primary-color)'}
                            onBlur={(e) => e.target.style.borderColor = '#333'}
                        ></textarea>
                        <Button variant="primary" style={{ width: '100%' }}>Enviar Mensaje</Button>
                    </form>
                </div>
            </div>

            <div style={{ borderTop: '1px solid rgba(255,255,255,0.05)', marginTop: '60px', paddingTop: '30px', textAlign: 'center', color: '#666', fontSize: '0.9rem' }}>
                © {new Date().getFullYear()} NexIA Soluciones. Todos los derechos reservados.
            </div>
        </footer>
    );
};

export default Footer;
