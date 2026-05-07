import React, { useState } from 'react';
import { Navigate } from 'react-router-dom';
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

const AppLanding = ({ slug }) => {
    const [formData, setFormData] = useState({ nombre: '', email: '', telefono: '', mensaje: '' });
    const [formStatus, setFormStatus] = useState('idle');

    const product = products.find(p => p.slug === slug);
    if (!product) return <Navigate to="/" replace />;

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
        <div className="app-landing-page">
            <div className="app-landing-card">
                <div className="alc-img">
                    <img src={product.image} alt={product.title} />
                </div>

                <div className="alc-body">
                    <h2 className="alc-title">{product.title}</h2>
                    <p className="alc-subtitle">{product.subtitle}</p>

                    <ul className="alc-features">
                        {product.features.map((f, i) => (
                            <li key={i}><span className="alc-check">✓</span>{f}</li>
                        ))}
                    </ul>

                    {product.priceLabel && (
                        <p className="alc-price-label">{product.priceLabel}</p>
                    )}
                    <p className="alc-price">{product.price}</p>

                    {formStatus === 'success' ? (
                        <div className="alc-success">
                            <div style={{ fontSize: '2.5rem', marginBottom: '12px' }}>✅</div>
                            <p style={{ fontWeight: '700', marginBottom: '4px' }}>¡Solicitud enviada!</p>
                            <p className="alc-subtitle">Te contactaremos a la brevedad.</p>
                        </div>
                    ) : (
                        <form onSubmit={handleSubmit} className="alc-form">
                            <hr className="alc-divider" />
                            <input className="alc-input" name="nombre" placeholder="Nombre completo *" required value={formData.nombre} onChange={handleChange} />
                            <input className="alc-input" name="email" type="email" placeholder="Correo electrónico *" required value={formData.email} onChange={handleChange} />
                            <input className="alc-input" name="telefono" placeholder="Teléfono (opcional)" value={formData.telefono} onChange={handleChange} />
                            <textarea className="alc-input alc-textarea" name="mensaje" placeholder="¿Alguna pregunta o comentario?" rows={3} value={formData.mensaje} onChange={handleChange} />
                            {formStatus === 'error' && (
                                <p className="alc-error">Error al enviar. Escríbenos a ventas@nexiasoluciones.com.mx</p>
                            )}
                            <button type="submit" disabled={formStatus === 'sending'} className="alc-submit">
                                {formStatus === 'sending' ? 'Enviando...' : 'Enviar solicitud'}
                            </button>
                        </form>
                    )}
                </div>
            </div>

            <a href="/#productos" className="alc-back">← Ver todas las apps</a>
        </div>
    );
};

export default AppLanding;
