import React, { useState } from 'react';
import Button from './Button';
import { Link } from 'react-router-dom';
import logo from '../assets/logo.png';

const Footer = ({ openPrivacy, openModal }) => {

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

    const logoStyle = {
        height: '40px',
        width: 'auto',
        marginBottom: '10px',
        cursor: 'pointer',
    };

    const linkStyle = {
        color: 'var(--secondary-text-color)',
        textDecoration: 'none',
        transition: 'color 0.2s',
        cursor: 'pointer',
    };



    return (
        <footer style={footerStyle}>
            <div style={containerStyle}>
                <div style={columnStyle}>
                    <Link to="/" onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })} style={{ display: 'flex', alignItems: 'center', gap: '10px', textDecoration: 'none', marginBottom: '15px' }}>
                        <img src={logo} alt="NexIA Soluciones" style={{ height: '40px', width: 'auto' }} />
                        <span style={{ color: '#FFFFFF', fontWeight: '700', fontSize: '1.2rem', fontFamily: 'var(--font-heading)' }}>NexIA Soluciones</span>
                    </Link>
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
                    <Link to="/#filosofia" style={linkStyle} onMouseEnter={(e) => e.target.style.color = 'var(--primary-color)'} onMouseLeave={(e) => e.target.style.color = 'var(--secondary-text-color)'}>Filosofía</Link>
                    <Link to="/#benefits" style={linkStyle} onMouseEnter={(e) => e.target.style.color = 'var(--primary-color)'} onMouseLeave={(e) => e.target.style.color = 'var(--secondary-text-color)'}>Beneficios</Link>
                    <Link to="/productos" style={linkStyle} onMouseEnter={(e) => e.target.style.color = 'var(--primary-color)'} onMouseLeave={(e) => e.target.style.color = 'var(--secondary-text-color)'}>Productos</Link>
                    <Link to="/#consulting" style={linkStyle} onMouseEnter={(e) => e.target.style.color = 'var(--primary-color)'} onMouseLeave={(e) => e.target.style.color = 'var(--secondary-text-color)'}>Consultoría</Link>
                    <Link to="/#academy" style={linkStyle} onMouseEnter={(e) => e.target.style.color = 'var(--primary-color)'} onMouseLeave={(e) => e.target.style.color = 'var(--secondary-text-color)'}>Academia</Link>
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
                    <p style={{ color: 'var(--secondary-text-color)', fontSize: '0.95rem', lineHeight: '1.6' }}>
                        ¿Listo para optimizar tu empresa? Iniciemos una conversación sobre tus objetivos.
                    </p>
                    <Button
                        variant="primary"
                        style={{ width: '100%', marginTop: '10px' }}
                        onClick={() => openModal('Footer CTA')}
                    >
                        Iniciar Conversación
                    </Button>

                    <div style={{ marginTop: '20px' }}>
                        <h3 style={{ fontSize: '1.2rem', fontWeight: '700', marginBottom: '15px' }}>Síguenos</h3>
                        <div style={{ display: 'flex', gap: '20px' }}>
                            {/* Facebook */}
                            <a href="#" className="social-icon" style={{ color: '#E2E8F0', transition: 'color 0.3s' }}
                                onMouseEnter={(e) => e.currentTarget.style.color = 'var(--primary-color)'}
                                onMouseLeave={(e) => e.currentTarget.style.color = '#E2E8F0'}>
                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                                    <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.791-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z" />
                                </svg>
                            </a>
                            {/* LinkedIn */}
                            <a href="#" className="social-icon" style={{ color: '#E2E8F0', transition: 'color 0.3s' }}
                                onMouseEnter={(e) => e.currentTarget.style.color = 'var(--primary-color)'}
                                onMouseLeave={(e) => e.currentTarget.style.color = '#E2E8F0'}>
                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                                    <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z" />
                                </svg>
                            </a>
                            {/* Instagram */}
                            <a href="#" className="social-icon" style={{ color: '#E2E8F0', transition: 'color 0.3s' }}
                                onMouseEnter={(e) => e.currentTarget.style.color = 'var(--primary-color)'}
                                onMouseLeave={(e) => e.currentTarget.style.color = '#E2E8F0'}>
                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                                    <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.069-4.85.069-3.204 0-3.584-.012-4.849-.069-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z" />
                                </svg>
                            </a>
                        </div>
                    </div>
                </div>
            </div>

            <div style={{ borderTop: '1px solid rgba(255,255,255,0.05)', marginTop: '60px', paddingTop: '30px', textAlign: 'center', color: '#666', fontSize: '0.9rem' }}>
                © {new Date().getFullYear()} NexIA Soluciones. Todos los derechos reservados.
            </div>
        </footer>
    );
};

export default Footer;
