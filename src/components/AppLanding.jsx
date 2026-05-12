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
    const [formData, setFormData] = useState({
        nombre: '', email: '', telefono: '', mensaje: '',
        requiere_factura: false,
        factura_rfc: '', factura_razon_social: '',
        factura_uso_cfdi: '', factura_regimen_fiscal: '',
        factura_correo: '',
    });
    const [formStatus, setFormStatus] = useState('idle');

    const product = products.find(p => p.slug === slug);
    if (!product) return <Navigate to="/" replace />;

    const handleChange = (e) => {
        const { name, type, value, checked } = e.target;
        if (name === 'requiere_factura') {
            setFormData(prev => ({
                ...prev,
                requiere_factura: checked,
                factura_correo: checked ? (prev.factura_correo || prev.email) : '',
            }));
        } else {
            setFormData(prev => ({ ...prev, [name]: type === 'checkbox' ? checked : value }));
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setFormStatus('sending');
        try {
            const webhook = import.meta.env.VITE_N8N_VENTAS_WEBHOOK;
            const slugMap = {
                'nexia-planner': 'scholar',
                'nexia-facturacion': 'facturacion',
                'nexia-tienda': 'tienda',
            };
            const res = await fetch(webhook, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ appName: product.title, appPrice: product.price, appSlug: slugMap[product.slug] || product.slug, ...formData }),
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
                            <label style={{ display: 'flex', alignItems: 'center', gap: '10px', cursor: 'pointer', fontSize: '0.9rem', userSelect: 'none' }}>
                                <input type="checkbox" name="requiere_factura" checked={formData.requiere_factura} onChange={handleChange} style={{ width: '16px', height: '16px', accentColor: '#00A3FF', cursor: 'pointer' }} />
                                ¿Necesitas factura?
                            </label>
                            {formData.requiere_factura && (
                                <>
                                    <input className="alc-input" name="factura_rfc" placeholder="RFC *" required maxLength={13} value={formData.factura_rfc} onChange={handleChange} />
                                    <input className="alc-input" name="factura_razon_social" placeholder="Razón Social *" required value={formData.factura_razon_social} onChange={handleChange} />
                                    <select className="alc-input" name="factura_uso_cfdi" required value={formData.factura_uso_cfdi} onChange={handleChange}>
                                        <option value="">Uso CFDI *</option>
                                        <option value="G03">G03 — Gastos en general</option>
                                        <option value="S01">S01 — Sin efectos fiscales</option>
                                        <option value="G01">G01 — Adquisición de mercancias</option>
                                        <option value="I08">I08 — Licencias y derechos de autor</option>
                                        <option value="D10">D10 — Pagos por servicios educativos</option>
                                    </select>
                                    <select className="alc-input" name="factura_regimen_fiscal" required value={formData.factura_regimen_fiscal} onChange={handleChange}>
                                        <option value="">Régimen Fiscal *</option>
                                        <option value="601">601 — General de Ley Personas Morales</option>
                                        <option value="612">612 — Personas Físicas con Act. Empresariales</option>
                                        <option value="626">626 — Régimen Simplificado de Confianza</option>
                                        <option value="621">621 — Incorporación Fiscal</option>
                                        <option value="603">603 — Personas Morales sin Fines de Lucro</option>
                                    </select>
                                    <input className="alc-input" name="factura_correo" type="email" placeholder="Correo para factura *" required value={formData.factura_correo} onChange={handleChange} />
                                </>
                            )}
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
