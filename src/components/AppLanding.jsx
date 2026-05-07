import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import appNexiaPlanner from '../assets/app-nexia-planner.jpeg';
import appNexiaGastos from '../assets/app-nexia-gastos.jpeg';
import appNexiaTienda from '../assets/app-nexia-tienda.jpeg';

const products = [
    {
        slug: 'nexia-planner',
        title: 'NexIA Planner',
        subtitle: 'Planificador Académico',
        image: appNexiaPlanner,
        price: '$280 MXN / año',
        priceLabel: 'Precio de lanzamiento',
        features: [
            'Organización sin estrés — centraliza materias, alumnos y asistencia',
            'Promedia y califica automáticamente — sin cálculos manuales',
            'Comunicación rápida — notifica a alumnos en segundos',
            'Sin papeleo — certificados, diplomas y registros desde tu app',
            'Ahorra horas cada semana — fácil de usar desde el primer día',
        ],
    },
    {
        slug: 'nexia-facturacion',
        title: 'Nexia Gastos',
        subtitle: 'Control de Gastos',
        image: appNexiaGastos,
        price: 'Consultar precio',
        priceLabel: 'Disponible ahora',
        features: [
            'Control de gastos empresariales',
            'Categorización inteligente',
            'Reportes por período',
            'Dashboard financiero ejecutivo',
            'Acceso multi-usuario',
        ],
    },
    {
        slug: 'nexia-tienda',
        title: 'Nexia Tienda',
        subtitle: 'Gestión de Ventas',
        image: appNexiaTienda,
        price: 'Próximamente',
        priceLabel: '',
        features: [
            'Gestión de inventario',
            'Punto de venta digital',
            'Reportes de ventas',
            'Control de clientes',
            'Facturación integrada',
        ],
    },
];

const inputStyle = {
    background: '#1a202c',
    border: '1px solid rgba(255,255,255,0.1)',
    color: '#fff',
    padding: '12px',
    borderRadius: '8px',
    width: '100%',
    fontSize: '0.95rem',
    fontFamily: 'var(--font-main)',
    outline: 'none',
};

const AppLanding = ({ slug }) => {
    const [formData, setFormData] = useState({ nombre: '', email: '', telefono: '', mensaje: '' });
    const [formStatus, setFormStatus] = useState('idle');
    const navigate = useNavigate();

    const product = products.find(p => p.slug === slug);

    if (!product) {
        navigate('/');
        return null;
    }

    const handleChange = (e) => {
        setFormData(prev => ({ ...prev, [e.target.name]: e.target.value }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setFormStatus('sending');
        try {
            const webhook = import.meta.env.VITE_N8N_VENTAS_WEBHOOK;
            const res = await fetch(webhook, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ appName: product.title, appPrice: product.price, ...formData }),
            });
            if (!res.ok) throw new Error('HTTP ' + res.status);
            setFormStatus('success');
        } catch {
            setFormStatus('error');
        }
    };

    return (
        <div style={{
            minHeight: '80vh',
            backgroundColor: 'var(--background-color)',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            padding: '80px 5%',
        }}>
            <div style={{
                backgroundColor: 'var(--card-background)',
                borderRadius: '16px',
                overflow: 'hidden',
                border: '1px solid #00A3FF',
                width: '100%',
                maxWidth: '480px',
            }}>
                <div style={{ height: '200px', overflow: 'hidden', backgroundColor: '#1E2530' }}>
                    <img src={product.image} alt={product.title} style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
                </div>

                <div style={{ padding: '28px' }}>
                    <h2 style={{ fontSize: '1.6rem', color: 'var(--primary-color)', fontFamily: 'var(--font-heading)', marginBottom: '4px' }}>
                        {product.title}
                    </h2>
                    <p style={{ color: 'var(--secondary-text-color)', fontSize: '0.9rem', marginBottom: '20px' }}>
                        {product.subtitle}
                    </p>

                    <ul style={{ listStyle: 'none', padding: 0, margin: '0 0 24px', display: 'flex', flexDirection: 'column', gap: '8px' }}>
                        {product.features.map((f, i) => (
                            <li key={i} style={{ color: 'var(--secondary-text-color)', fontSize: '0.9rem', display: 'flex', alignItems: 'center', gap: '8px' }}>
                                <span style={{ color: '#00A3FF', flexShrink: 0 }}>✓</span> {f}
                            </li>
                        ))}
                    </ul>

                    {product.priceLabel && (
                        <p style={{ fontSize: '0.75rem', color: 'var(--secondary-text-color)', marginBottom: '4px' }}>{product.priceLabel}</p>
                    )}
                    <p style={{ fontSize: '1.2rem', fontWeight: '700', color: 'var(--text-color)', marginBottom: '20px' }}>{product.price}</p>

                    {formStatus === 'success' ? (
                        <div style={{ textAlign: 'center', padding: '16px 0' }}>
                            <div style={{ fontSize: '2.5rem', marginBottom: '12px' }}>✅</div>
                            <p style={{ fontWeight: '700', marginBottom: '4px' }}>¡Solicitud enviada!</p>
                            <p style={{ color: 'var(--secondary-text-color)', fontSize: '0.9rem' }}>Te contactaremos a la brevedad.</p>
                        </div>
                    ) : (
                        <>
                            <hr style={{ border: 'none', borderTop: '2px solid #00A3FF', margin: '0 0 20px' }} />
                            <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                                <input style={inputStyle} name="nombre" placeholder="Nombre completo *" required value={formData.nombre} onChange={handleChange} />
                                <input style={inputStyle} name="email" type="email" placeholder="Correo electrónico *" required value={formData.email} onChange={handleChange} />
                                <input style={inputStyle} name="telefono" placeholder="Teléfono (opcional)" value={formData.telefono} onChange={handleChange} />
                                <textarea style={{ ...inputStyle, resize: 'vertical' }} name="mensaje" placeholder="¿Alguna pregunta o comentario?" rows={3} value={formData.mensaje} onChange={handleChange} />
                                {formStatus === 'error' && (
                                    <p style={{ color: '#f87171', fontSize: '0.85rem' }}>Error al enviar. Escríbenos a ventas@nexiasoluciones.com.mx</p>
                                )}
                                <button
                                    type="submit"
                                    disabled={formStatus === 'sending'}
                                    style={{ background: '#00A3FF', color: '#fff', padding: '12px', borderRadius: '8px', border: 'none', width: '100%', fontWeight: '700', cursor: formStatus === 'sending' ? 'not-allowed' : 'pointer', fontFamily: 'var(--font-heading)', fontSize: '0.95rem' }}
                                >
                                    {formStatus === 'sending' ? 'Enviando...' : 'Enviar solicitud'}
                                </button>
                            </form>
                        </>
                    )}
                </div>
            </div>

            <a href="/#productos" style={{ marginTop: '32px', color: 'var(--secondary-text-color)', fontSize: '0.9rem', textDecoration: 'none' }}>
                ← Ver todas las apps
            </a>
        </div>
    );
};

export default AppLanding;
