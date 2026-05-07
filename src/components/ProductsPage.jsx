import React, { useState, useEffect } from 'react';
import appNexiaPlanner from '../assets/app-nexia-planner.jpeg';
import appNexiaPdca from '../assets/app-nexia-pdca.jpeg';
import appNexiaVsm from '../assets/app-nexia-vsm.jpeg';
import appNexiaSmed from '../assets/app-nexia-smed.jpeg';
import appNexiaHeijunka from '../assets/app-nexia-heijunka.jpeg';
import appNexiaGastos from '../assets/app-nexia-gastos.jpeg';
import appNexiaTienda from '../assets/app-nexia-tienda.jpeg';

const ProductsPage = ({ openModal }) => {
    const [expandedCard, setExpandedCard] = useState(null);
    const [formData, setFormData] = useState({ nombre: '', email: '', telefono: '', mensaje: '' });
    const [formStatus, setFormStatus] = useState('idle');
    const [activeGroup, setActiveGroup] = useState('todos');

    useEffect(() => {
        const handleHashChange = () => {
            if (window.location.hash === '#productos') {
                setActiveGroup('todos');
                setExpandedCard(null);
                setFormStatus('idle');
            }
        };
        window.addEventListener('hashchange', handleHashChange);
        return () => window.removeEventListener('hashchange', handleHashChange);
    }, []);

    useEffect(() => {
        const slug = new URLSearchParams(window.location.search).get('app');
        if (!slug) return;
        const allProducts = groups.flatMap(g => g.products);
        const product = allProducts.find(p => p.slug === slug);
        if (!product || !product.ctaActive) return;
        setExpandedCard(product.id);
        setTimeout(() => {
            document.getElementById(`card-${product.slug}`)?.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }, 100);
    }, []); // eslint-disable-line react-hooks/exhaustive-deps

    useEffect(() => {
        if (formStatus === 'success') {
            const timer = setTimeout(() => {
                handleCollapse();
                setActiveGroup('todos');
                document.getElementById('productos')?.scrollIntoView({ behavior: 'smooth' });
            }, 4000);
            return () => clearTimeout(timer);
        }
    }, [formStatus]);

    const handleExpand = (p) => {
        setExpandedCard(p.id);
        setFormData({ nombre: '', email: '', telefono: '', mensaje: '' });
        setFormStatus('idle');
    };

    const handleCollapse = () => {
        setExpandedCard(null);
        setFormStatus('idle');
    };

    const handleChange = (e) => {
        setFormData(prev => ({ ...prev, [e.target.name]: e.target.value }));
    };

    const handleSubmit = async (e, p) => {
        e.preventDefault();
        setFormStatus('sending');
        try {
            const webhook = import.meta.env.VITE_N8N_VENTAS_WEBHOOK;
            const body = { appName: p.title, appPrice: p.price, ...formData };
            const res = await fetch(webhook, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(body),
            });
            if (!res.ok) throw new Error('HTTP ' + res.status);
            setFormStatus('success');
        } catch {
            setFormStatus('error');
        }
    };

    const groups = [
        {
            id: 'educacion',
            label: '📚 Educación',
            products: [
                {
                    id: 1, slug: 'nexia-planner',
                    title: 'NexIA Planner', subtitle: 'Planificador Académico',
                    image: appNexiaPlanner,
                    badge: null,
                    price: '$280 MXN / año', priceLabel: 'Precio de lanzamiento',
                    features: [
                        'Organización sin estrés — centraliza materias, alumnos y asistencia',
                        'Promedia y califica automáticamente — sin cálculos manuales',
                        'Comunicación rápida — notifica a alumnos en segundos',
                        'Sin papeleo — certificados, diplomas y registros desde tu app',
                        'Ahorra horas cada semana — fácil de usar desde el primer día'
                    ],
                    ctaActive: true, ctaLabel: 'Quiero esta app', onlinePayment: false,
                }
            ]
        },
        {
            id: 'mejora-continua',
            label: '📈 Mejora Continua',
            products: [
                {
                    id: 2, slug: 'nexia-pdca',
                    title: 'Nexia PDCA', subtitle: 'Mejora Continua',
                    image: appNexiaPdca, badge: 'PRÓXIMAMENTE', badgeColor: '#F5A623',
                    price: 'Próximamente', priceLabel: '',
                    features: ['Ciclos PDCA digitales', 'Seguimiento en tiempo real', 'Historial de proyectos', 'Reportes automáticos', 'Acceso multi-usuario'],
                    ctaActive: false, ctaLabel: 'Quiero esta app', onlinePayment: false,
                },
                {
                    id: 3, slug: 'nexia-vsm',
                    title: 'Nexia VSM', subtitle: 'Value Stream Mapping',
                    image: appNexiaVsm, badge: 'PRÓXIMAMENTE', badgeColor: '#F5A623',
                    price: 'Próximamente', priceLabel: '',
                    features: ['Mapeo digital de flujo de valor', 'Identificación de desperdicios', 'Simulación de estado futuro', 'Export PDF', 'Colaboración en equipo'],
                    ctaActive: false, ctaLabel: 'Quiero esta app', onlinePayment: false,
                },
                {
                    id: 4, slug: 'nexia-smed',
                    title: 'Nexia SMED', subtitle: 'Cambio Rápido de Herramental',
                    image: appNexiaSmed, badge: 'PRÓXIMAMENTE', badgeColor: '#F5A623',
                    price: 'Próximamente', priceLabel: '',
                    features: ['Cronometrado de actividades', 'Separación interno/externo', 'Plan de reducción', 'Seguimiento de mejoras', 'Dashboard por máquina'],
                    ctaActive: false, ctaLabel: 'Quiero esta app', onlinePayment: false,
                },
                {
                    id: 5, slug: 'nexia-heijunka',
                    title: 'Nexia Heijunka', subtitle: 'Nivelación de Producción',
                    image: appNexiaHeijunka, badge: 'PRÓXIMAMENTE', badgeColor: '#F5A623',
                    price: 'Próximamente', priceLabel: '',
                    features: ['Tablero de nivelación digital', 'Balanceo de carga', 'Visualización de takt time', 'Alertas de desbalance', 'Integración con VSM'],
                    ctaActive: false, ctaLabel: 'Quiero esta app', onlinePayment: false,
                }
            ]
        },
        {
            id: 'admin-finanzas',
            label: '💼 Administración & Finanzas',
            products: [
                {
                    id: 6, slug: 'nexia-facturacion',
                    title: 'Nexia Gastos', subtitle: 'Control de Gastos',
                    image: appNexiaGastos, badge: null,
                    price: 'Consultar precio', priceLabel: 'Disponible ahora',
                    features: ['Control de gastos empresariales', 'Categorización inteligente', 'Reportes por período', 'Dashboard financiero ejecutivo', 'Acceso multi-usuario'],
                    ctaActive: true, ctaLabel: 'Quiero esta app', onlinePayment: false,
                },
                {
                    id: 7, slug: 'nexia-tienda',
                    title: 'Nexia Tienda', subtitle: 'Gestión de Ventas',
                    image: appNexiaTienda, badge: 'BETA', badgeColor: '#00A3FF',
                    price: 'Próximamente', priceLabel: '',
                    features: ['Gestión de inventario', 'Punto de venta digital', 'Reportes de ventas', 'Control de clientes', 'Facturación integrada'],
                    ctaActive: true, ctaLabel: 'Quiero esta app', onlinePayment: false,
                }
            ]
        }
    ];

    const activeProducts = activeGroup === 'todos'
        ? groups.flatMap(g => g.products)
        : groups.find(g => g.id === activeGroup)?.products || [];

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

    return (
        <div id="productos" style={{ padding: '80px 5% 80px', backgroundColor: 'var(--background-color)', minHeight: '100vh' }}>
            <div style={{ textAlign: 'center', marginBottom: '60px', maxWidth: '800px', margin: '0 auto 60px' }}>
                <span style={{
                    display: 'inline-block',
                    color: '#00A3FF',
                    fontSize: '0.75rem',
                    fontWeight: '700',
                    letterSpacing: '0.2em',
                    textTransform: 'uppercase',
                    marginBottom: '16px',
                    border: '1px solid rgba(0,163,255,0.3)',
                    borderRadius: '20px',
                    padding: '4px 16px'
                }}>
                    Portafolio de Soluciones
                </span>
                <h1 style={{
                    fontSize: '3rem',
                    fontWeight: '700',
                    color: 'var(--text-color)',
                    fontFamily: 'var(--font-heading)',
                    marginBottom: '20px',
                    lineHeight: '1.1'
                }}>
                    Tecnología que construimos<br />y operamos.
                </h1>
                <p style={{
                    color: 'var(--secondary-text-color)',
                    fontSize: '1.1rem',
                    lineHeight: '1.7',
                    maxWidth: '600px',
                    margin: '0 auto'
                }}>
                    Nuestras apps no son productos de terceros — las desarrollamos internamente para resolver problemas concretos, democratizar la IA y garantizar que la mejora persiste mucho después de que la consultoría termina.
                </p>
            </div>

            {/* Tabs de grupos */}
            <div style={{ display: 'flex', justifyContent: 'center', gap: '12px', marginBottom: '40px', flexWrap: 'wrap' }}>
                <button
                    onClick={() => { setActiveGroup('todos'); setExpandedCard(null); setFormStatus('idle'); }}
                    style={{
                        padding: '10px 24px', borderRadius: '8px', fontFamily: 'var(--font-heading)',
                        fontWeight: '600', fontSize: '0.9rem', cursor: 'pointer', transition: 'all 0.2s ease',
                        background: activeGroup === 'todos' ? '#00A3FF' : 'transparent',
                        color: activeGroup === 'todos' ? '#fff' : 'var(--secondary-text-color)',
                        border: activeGroup === 'todos' ? '1px solid #00A3FF' : '1px solid rgba(255,255,255,0.1)',
                    }}
                    onMouseEnter={e => { if (activeGroup !== 'todos') { e.currentTarget.style.borderColor = '#00A3FF'; e.currentTarget.style.color = '#fff'; }}}
                    onMouseLeave={e => { if (activeGroup !== 'todos') { e.currentTarget.style.borderColor = 'rgba(255,255,255,0.1)'; e.currentTarget.style.color = 'var(--secondary-text-color)'; }}}
                >🌐 Todos</button>
                {groups.map(g => (
                    <button
                        key={g.id}
                        onClick={() => { setActiveGroup(g.id); setExpandedCard(null); setFormStatus('idle'); }}
                        style={{
                            padding: '10px 24px',
                            borderRadius: '8px',
                            fontFamily: 'var(--font-heading)',
                            fontWeight: '600',
                            fontSize: '0.9rem',
                            cursor: 'pointer',
                            transition: 'all 0.2s ease',
                            background: activeGroup === g.id ? '#00A3FF' : 'transparent',
                            color: activeGroup === g.id ? '#fff' : 'var(--secondary-text-color)',
                            border: activeGroup === g.id ? '1px solid #00A3FF' : '1px solid rgba(255,255,255,0.1)',
                        }}
                        onMouseEnter={e => { if (activeGroup !== g.id) { e.currentTarget.style.borderColor = '#00A3FF'; e.currentTarget.style.color = '#fff'; }}}
                        onMouseLeave={e => { if (activeGroup !== g.id) { e.currentTarget.style.borderColor = 'rgba(255,255,255,0.1)'; e.currentTarget.style.color = 'var(--secondary-text-color)'; }}}
                    >
                        {g.label}
                    </button>
                ))}
            </div>

            {expandedCard !== null && (
                <div
                    onClick={handleCollapse}
                    style={{ position: 'fixed', inset: 0, zIndex: 100, background: 'rgba(0,0,0,0.7)' }}
                />
            )}

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 400px))', justifyContent: 'center', gap: '32px', maxWidth: '1200px', margin: '0 auto' }}>
                {activeProducts.map((p) => {
                    const isExpanded = expandedCard === p.id;
                    return (
                        <div
                            key={p.id}
                            id={`card-${p.slug}`}
                            style={{
                                backgroundColor: 'var(--card-background)',
                                borderRadius: '16px',
                                overflow: 'hidden',
                                border: isExpanded ? '1px solid #00A3FF' : '1px solid rgba(255,255,255,0.05)',
                                display: 'flex',
                                flexDirection: 'column',
                                transition: 'all 0.3s ease',
                                position: 'relative',
                                zIndex: isExpanded ? 101 : 1,
                                transform: isExpanded ? 'scale(1.02)' : 'scale(1)',
                            }}
                        >
                            {isExpanded && (
                                <button
                                    onClick={handleCollapse}
                                    style={{ position: 'absolute', top: '12px', right: '16px', background: 'none', border: 'none', color: '#64748b', fontSize: '1.2rem', cursor: 'pointer', zIndex: 1, lineHeight: 1 }}
                                    onMouseEnter={e => e.currentTarget.style.color = '#fff'}
                                    onMouseLeave={e => e.currentTarget.style.color = '#64748b'}
                                >✕</button>
                            )}

                            <div style={{ height: '200px', overflow: 'hidden', backgroundColor: '#1E2530', display: 'flex', alignItems: 'center', justifyContent: 'center', position: 'relative' }}>
                                {p.image
                                    ? <img src={p.image} alt={p.title} style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
                                    : <span style={{ fontSize: '3.5rem', opacity: 0.25 }}>⚙️</span>
                                }
                                {p.badge && (
                                    <span style={{ position: 'absolute', top: '12px', right: '12px', backgroundColor: p.badgeColor, color: '#fff', fontSize: '0.7rem', fontWeight: '700', padding: '3px 10px', borderRadius: '20px', letterSpacing: '0.08em' }}>
                                        {p.badge}
                                    </span>
                                )}
                            </div>

                            <div style={{ padding: '28px', display: 'flex', flexDirection: 'column', flexGrow: 1 }}>
                                <h3 style={{ fontSize: '1.6rem', color: 'var(--primary-color)', fontFamily: 'var(--font-heading)', marginBottom: '4px' }}>{p.title}</h3>
                                <p style={{ color: 'var(--secondary-text-color)', fontSize: '0.9rem', marginBottom: '20px' }}>{p.subtitle}</p>

                                <ul style={{ listStyle: 'none', padding: 0, margin: '0 0 24px', display: 'flex', flexDirection: 'column', gap: '8px' }}>
                                    {p.features.map((f, i) => (
                                        <li key={i} style={{ color: 'var(--secondary-text-color)', fontSize: '0.9rem', display: 'flex', alignItems: 'center', gap: '8px' }}>
                                            <span style={{ color: '#00A3FF', flexShrink: 0 }}>✓</span> {f}
                                        </li>
                                    ))}
                                </ul>

                                <div style={{ marginTop: 'auto' }}>
                                    {p.priceLabel && (
                                        <p style={{ fontSize: '0.75rem', color: 'var(--secondary-text-color)', marginBottom: '4px' }}>{p.priceLabel}</p>
                                    )}
                                    <p style={{ fontSize: '1.2rem', fontWeight: '700', color: 'var(--text-color)', marginBottom: '16px' }}>{p.price}</p>

                                    {!isExpanded ? (
                                        <>
                                            {p.ctaActive ? (
                                                <button
                                                    onClick={() => handleExpand(p)}
                                                    style={{ width: '100%', marginBottom: '10px', padding: '12px', borderRadius: '8px', border: 'none', background: '#00A3FF', color: '#fff', fontWeight: '700', cursor: 'pointer', fontFamily: 'var(--font-heading)', fontSize: '0.95rem' }}
                                                >
                                                    {p.ctaLabel}
                                                </button>
                                            ) : (
                                                <button
                                                    disabled
                                                    style={{ width: '100%', marginBottom: '10px', padding: '12px', borderRadius: '8px', border: 'none', background: '#00A3FF', color: '#fff', fontWeight: '700', cursor: 'not-allowed', fontFamily: 'var(--font-heading)', fontSize: '0.95rem', opacity: 0.4 }}
                                                >
                                                    {p.ctaLabel}
                                                </button>
                                            )}
                                            <button disabled className="btn-online-soon">
                                                🔒 Pago en línea — Próximamente
                                            </button>
                                        </>
                                    ) : (
                                        formStatus === 'success' ? (
                                            <div style={{ textAlign: 'center', padding: '16px 0' }}>
                                                <div style={{ fontSize: '2.5rem', marginBottom: '12px' }}>✅</div>
                                                <p style={{ fontWeight: '700', marginBottom: '4px' }}>¡Solicitud enviada!</p>
                                                <p style={{ color: 'var(--secondary-text-color)', fontSize: '0.9rem' }}>Te contactaremos a la brevedad.</p>
                                            </div>
                                        ) : (
                                            <>
                                                <hr style={{ border: 'none', borderTop: '2px solid #00A3FF', margin: '0 0 20px' }} />
                                                <form onSubmit={e => handleSubmit(e, p)} style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
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
                                        )
                                    )}
                                </div>
                            </div>
                        </div>
                    );
                })}
            </div>
        </div>
    );
};

export default ProductsPage;
