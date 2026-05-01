import React, { useState } from 'react';
import Button from './Button';

const PurchaseModal = ({ isOpen, onClose, appName, appPrice }) => {
    const [form, setForm] = useState({ nombre: '', email: '', telefono: '', mensaje: '' });
    const [status, setStatus] = useState('idle'); // idle | sending | success | error

    if (!isOpen) return null;

    const handleChange = (e) => {
        setForm(prev => ({ ...prev, [e.target.name]: e.target.value }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setStatus('sending');
        try {
            const res = await fetch(import.meta.env.VITE_N8N_VENTAS_WEBHOOK, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ appName, appPrice, ...form }),
            });
            if (!res.ok) throw new Error('HTTP ' + res.status);
            setStatus('success');
        } catch {
            setStatus('error');
        }
    };

    const handleClose = () => {
        setForm({ nombre: '', email: '', telefono: '', mensaje: '' });
        setStatus('idle');
        onClose();
    };

    return (
        <div className="purchase-modal-overlay" onClick={handleClose}>
            <div className="purchase-modal-container" onClick={e => e.stopPropagation()}>
                <button className="purchase-modal-close" onClick={handleClose}>✕</button>

                <div className="purchase-modal-header">
                    <h2 className="purchase-modal-appname">{appName}</h2>
                    <p className="purchase-modal-price">{appPrice}</p>
                </div>
                <hr className="purchase-modal-divider" />

                {status === 'success' ? (
                    <div style={{ textAlign: 'center', padding: '20px 0' }}>
                        <div style={{ fontSize: '3rem', marginBottom: '16px' }}>✅</div>
                        <h2 style={{ fontFamily: 'var(--font-heading)', marginBottom: '12px' }}>¡Solicitud enviada!</h2>
                        <p style={{ color: 'var(--secondary-text-color)' }}>Te contactaremos a la brevedad.</p>
                        <Button variant="primary" onClick={handleClose} style={{ marginTop: '24px' }}>Cerrar</Button>
                    </div>
                ) : (
                    <form onSubmit={handleSubmit} className="purchase-modal-form">
                        <input
                            className="modal-input"
                            name="nombre"
                            placeholder="Nombre completo *"
                            required
                            value={form.nombre}
                            onChange={handleChange}
                        />
                        <input
                            className="modal-input"
                            name="email"
                            type="email"
                            placeholder="Correo electrónico *"
                            required
                            value={form.email}
                            onChange={handleChange}
                        />
                        <input
                            className="modal-input"
                            name="telefono"
                            placeholder="Teléfono (opcional)"
                            value={form.telefono}
                            onChange={handleChange}
                        />
                        <textarea
                            className="modal-input"
                            name="mensaje"
                            placeholder="¿Alguna pregunta o comentario?"
                            rows={3}
                            value={form.mensaje}
                            onChange={handleChange}
                            style={{ resize: 'vertical' }}
                        />

                        {status === 'error' && (
                            <p style={{ color: '#f87171', fontSize: '0.9rem' }}>
                                Hubo un error al enviar. Intenta de nuevo o escríbenos a ventas@nexiasoluciones.com.mx
                            </p>
                        )}

                        <Button
                            variant="primary"
                            type="submit"
                            disabled={status === 'sending'}
                            style={{ marginTop: '8px' }}
                        >
                            {status === 'sending' ? 'Enviando...' : 'Enviar solicitud'}
                        </Button>
                    </form>
                )}
            </div>
        </div>
    );
};

export default PurchaseModal;
