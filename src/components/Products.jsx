import React from 'react';
import Button from './Button';
import nexguardMockup from '../assets/nexguard-mockup.png';
import nexadminMockup from '../assets/nexadmin-mockup.png';

const Products = ({ openModal }) => {
    const sectionStyle = {
        padding: '100px 5%',
        backgroundColor: '#232936', // Slightly lighter than main background
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
        gridTemplateColumns: 'repeat(auto-fit, minmax(350px, 1fr))',
        gap: '40px',
        maxWidth: '1000px',
        margin: '0 auto 60px',
    };

    const productCardStyle = {
        backgroundColor: 'var(--card-background)',
        borderRadius: '20px',
        overflow: 'hidden',
        boxShadow: '0 4px 6px rgba(0,0,0,0.2)',
        transition: 'transform 0.3s ease',
        border: '1px solid rgba(255, 255, 255, 0.05)',
    };

    const imagePlaceholderStyle = {
        height: '200px',
        backgroundColor: 'var(--secondary-color)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        color: '#FFFFFF',
        fontSize: '1.5rem',
        fontWeight: '700',
        opacity: '0.9',
    };

    const contentStyle = {
        padding: '30px',
        textAlign: 'left',
    };

    const productNameStyle = {
        fontSize: '1.75rem',
        fontWeight: '700',
        marginBottom: '10px',
        color: 'var(--text-color)',
    };

    const productDescStyle = {
        color: 'var(--secondary-text-color)',
        marginBottom: '20px',
    };

    return (
        <section id="products" className="products-section" style={{ backgroundColor: '#232936' }}>
            <h2 className="section-title">Software que Trabaja 24/7 para tu Rentabilidad.</h2>

            <div className="products-grid">
                <div style={productCardStyle} className="product-card">
                    <img src={nexguardMockup} alt="NexGuard App Mockup" style={{ width: '100%', height: '300px', objectFit: 'cover' }} />
                    <div style={contentStyle}>
                        <h3 style={productNameStyle}>NexGuard</h3>
                        <p style={{ ...productDescStyle, fontWeight: '600', fontSize: '1.1rem', marginBottom: '12px' }}>
                            Control de Acceso Inteligente, Seguridad Automatizada para tus Instalaciones.
                        </p>
                        <p style={productDescStyle}>
                            Digitaliza la seguridad y la logística de tu fraccionamiento. Utilizamos tecnología QR y reconocimiento móvil para eliminar cuellos de botella y errores humanos. Ofrece a tus residentes y personal la forma más rápida y segura de gestionar accesos, notificaciones de visitantes en tiempo real y registro histórico blindado.
                        </p>
                    </div>
                </div>

                <div style={productCardStyle} className="product-card">
                    <img src={nexadminMockup} alt="NexAdmin App Mockup" style={{ width: '100%', height: '300px', objectFit: 'cover' }} />
                    <div style={contentStyle}>
                        <h3 style={productNameStyle}>NexAdmin</h3>
                        <p style={{ ...productDescStyle, fontWeight: '600', fontSize: '1.1rem', marginBottom: '12px' }}>
                            Gestión de Gastos Automatizada. Olvídate de las hojas de cálculo manuales.
                        </p>
                        <p style={productDescStyle}>
                            Tu asistente contable impulsado por IA. Simplifica la carga administrativa de tu negocio. Simplemente sube fotos de tus tickets o archivos PDF/XML y nuestra IA lee, categoriza y exporta los datos de tus facturas automáticamente a hoja de calculo o a tu sistema contable (ERP/CRM). Ahorra hasta 10 horas semanales en captura manual.
                        </p>
                    </div>
                </div>
            </div>

            <Button variant="primary" onClick={() => openModal('Explorar Apps')}>Explorar Nuestras Apps</Button>
        </section>
    );
};

export default Products;
