import React, { useState, useEffect } from 'react';
import Button from './Button';
import logo from '../assets/logo.png';

const Header = ({ openModal }) => {
    const [scrolled, setScrolled] = useState(false);

    useEffect(() => {
        const handleScroll = () => {
            setScrolled(window.scrollY > 50);
        };
        window.addEventListener('scroll', handleScroll);
        return () => window.removeEventListener('scroll', handleScroll);
    }, []);

    const headerStyle = {
        position: 'fixed',
        top: 0,
        left: 0,
        width: '100%',
        padding: '15px 5%',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        backgroundColor: scrolled ? 'rgba(26, 32, 44, 0.95)' : 'transparent',
        backdropFilter: scrolled ? 'blur(10px)' : 'none',
        boxShadow: scrolled ? '0 2px 10px rgba(0,0,0,0.3)' : 'none',
        zIndex: 1000,
        transition: 'all 0.3s ease',
        borderBottom: scrolled ? '1px solid rgba(255,255,255,0.05)' : 'none',
    };

    const logoStyle = {
        height: '65px',
        width: 'auto',
        transition: 'transform 0.3s ease',
    };

    const navStyle = {
        display: 'flex',
        gap: '30px',
        alignItems: 'center',
    };

    const linkStyle = {
        fontWeight: '500',
        fontSize: '0.95rem',
        color: 'var(--secondary-text-color)',
        transition: 'color 0.2s',
        cursor: 'pointer',
    };

    return (
        <header style={headerStyle}>
            <img src={logo} alt="NexIA Soluciones" style={logoStyle} />
            <nav style={navStyle}>
                <a href="#benefits" style={linkStyle} onMouseEnter={(e) => e.target.style.color = 'var(--primary-color)'} onMouseLeave={(e) => e.target.style.color = 'var(--secondary-text-color)'}>Beneficios</a>
                <a href="#products" style={linkStyle} onMouseEnter={(e) => e.target.style.color = 'var(--primary-color)'} onMouseLeave={(e) => e.target.style.color = 'var(--secondary-text-color)'}>Productos</a>
                <a href="#consulting" style={linkStyle} onMouseEnter={(e) => e.target.style.color = 'var(--primary-color)'} onMouseLeave={(e) => e.target.style.color = 'var(--secondary-text-color)'}>Consultoría</a>
                <a href="#academy" style={linkStyle} onMouseEnter={(e) => e.target.style.color = 'var(--primary-color)'} onMouseLeave={(e) => e.target.style.color = 'var(--secondary-text-color)'}>Academia</a>
                <Button variant="primary" onClick={() => openModal('Auditoría Gratuita - Header')}>Auditoría Gratuita</Button>
            </nav>
        </header>
    );
};

export default Header;
