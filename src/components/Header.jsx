import React, { useState, useEffect } from 'react';
import Button from './Button';
import logo from '../assets/logo.png';

const Header = ({ openModal }) => {
    const [scrolled, setScrolled] = useState(false);
    const [isMenuOpen, setIsMenuOpen] = useState(false);

    useEffect(() => {
        const handleScroll = () => {
            setScrolled(window.scrollY > 50);
        };
        window.addEventListener('scroll', handleScroll);
        return () => window.removeEventListener('scroll', handleScroll);
    }, []);

    const toggleMenu = () => {
        setIsMenuOpen(!isMenuOpen);
    };

    const closeMenu = () => {
        setIsMenuOpen(false);
    };

    return (
        <header className={`header-container ${scrolled ? 'scrolled' : ''}`}>
            <a href="#inicio" className="logo-link" onClick={closeMenu} style={{ display: 'flex', alignItems: 'center', gap: '10px', textDecoration: 'none' }}>
                <img src={logo} alt="NexIA Soluciones" className="header-logo" />
                <div style={{ display: 'flex', flexDirection: 'column', gap: '2px' }}>
                    <span className="logo-text" style={{ color: '#FFFFFF', fontWeight: '700', fontSize: '1.2rem', fontFamily: 'var(--font-heading)' }}>NexIA Soluciones</span>
                </div>
            </a>

            {/* Desktop Navigation */}
            <nav className="nav-desktop">
                <a href="#inicio" className="nav-link">Inicio</a>
                <a href="#filosofia" className="nav-link">Filosofía</a>
                <a href="#productos" className="nav-link">Productos</a>
                <a href="#benefits" className="nav-link">Beneficios</a>
                <a href="#consulting" className="nav-link">Consultoría</a>
                <a href="#academy" className="nav-link">Academia</a>
                <Button variant="primary" onClick={() => openModal('Auditoría Gratuita - Header')}>Agendar Auditoría Gratuita</Button>
                <a
                    href="https://clientes.nexiasoluciones.com.mx"
                    target="_blank"
                    rel="noopener noreferrer"
                    style={{
                        backgroundColor: 'var(--primary-color)',
                        color: '#FFFFFF',
                        padding: '10px 20px',
                        borderRadius: '8px',
                        textDecoration: 'none',
                        fontWeight: '600',
                        transition: 'all 0.3s ease',
                        border: '2px solid var(--primary-color)',
                        display: 'inline-block'
                    }}
                    onMouseEnter={(e) => {
                        e.target.style.backgroundColor = 'transparent';
                        e.target.style.color = 'var(--primary-color)';
                    }}
                    onMouseLeave={(e) => {
                        e.target.style.backgroundColor = 'var(--primary-color)';
                        e.target.style.color = '#FFFFFF';
                    }}
                >
                    🔒 Portal Clientes
                </a>
            </nav>

            {/* Mobile Menu Button */}
            <button className="mobile-menu-btn" onClick={toggleMenu} aria-label="Menu">
                {isMenuOpen ? '✕' : '☰'}
            </button>

            {/* Mobile Navigation Overlay */}
            <div className={`nav-mobile ${isMenuOpen ? 'open' : ''}`}>
                <nav className="nav-mobile-links">
                    <a href="#inicio" className="nav-link-mobile" onClick={closeMenu}>Inicio</a>
                    <a href="#productos" className="nav-link-mobile" onClick={closeMenu}>Productos</a>
                    <a href="#filosofia" className="nav-link-mobile" onClick={closeMenu}>Filosofía</a>
                    <a href="#benefits" className="nav-link-mobile" onClick={closeMenu}>Beneficios</a>
                    <a href="#consulting" className="nav-link-mobile" onClick={closeMenu}>Consultoría</a>
                    <a href="#academy" className="nav-link-mobile" onClick={closeMenu}>Academia</a>
                    <Button variant="primary" onClick={() => { openModal('Auditoría Gratuita - Mobile'); closeMenu(); }} style={{ marginTop: '20px', width: '100%' }}>
                        Agendar Auditoría Gratuita
                    </Button>
                    <a
                        href="https://clientes.nexiasoluciones.com.mx"
                        target="_blank"
                        rel="noopener noreferrer"
                        onClick={closeMenu}
                        style={{
                            backgroundColor: 'var(--primary-color)',
                            color: '#FFFFFF',
                            padding: '12px 20px',
                            borderRadius: '8px',
                            textDecoration: 'none',
                            fontWeight: '600',
                            border: '2px solid var(--primary-color)',
                            display: 'block',
                            textAlign: 'center',
                            marginTop: '12px'
                        }}
                    >
                        🔒 Portal Clientes
                    </a>
                </nav>
            </div>
        </header>
    );
};

export default Header;
