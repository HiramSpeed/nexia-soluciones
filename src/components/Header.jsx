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
            <img src={logo} alt="NexIA Soluciones" className="header-logo" />

            {/* Desktop Navigation */}
            <nav className="nav-desktop">
                <a href="#benefits" className="nav-link">Beneficios</a>
                <a href="#products" className="nav-link">Productos</a>
                <a href="#consulting" className="nav-link">Consultoría</a>
                <a href="#academy" className="nav-link">Academia</a>
                <Button variant="primary" onClick={() => openModal('Auditoría Gratuita - Header')}>Auditoría Gratuita</Button>
            </nav>

            {/* Mobile Menu Button */}
            <button className="mobile-menu-btn" onClick={toggleMenu} aria-label="Menu">
                {isMenuOpen ? '✕' : '☰'}
            </button>

            {/* Mobile Navigation Overlay */}
            <div className={`nav-mobile ${isMenuOpen ? 'open' : ''}`}>
                <nav className="nav-mobile-links">
                    <a href="#benefits" className="nav-link-mobile" onClick={closeMenu}>Beneficios</a>
                    <a href="#products" className="nav-link-mobile" onClick={closeMenu}>Productos</a>
                    <a href="#consulting" className="nav-link-mobile" onClick={closeMenu}>Consultoría</a>
                    <a href="#academy" className="nav-link-mobile" onClick={closeMenu}>Academia</a>
                    <Button variant="primary" onClick={() => { openModal('Auditoría Gratuita - Mobile'); closeMenu(); }} style={{ marginTop: '20px', width: '100%' }}>
                        Auditoría Gratuita
                    </Button>
                </nav>
            </div>
        </header>
    );
};

export default Header;
