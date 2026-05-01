import React, { useState } from 'react';

const ContactModal = ({ isOpen, onClose, source = 'General', onSuccess }) => {
    const [formData, setFormData] = useState({
        nombre: '',
        empresa: '',
        cargo: '',
        email: '',
        celular: '',
        mensaje: '',
        origen: source,
        agreement: false
    });
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [submitStatus, setSubmitStatus] = useState(null);

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setIsSubmitting(true);

        try {
            const response = await fetch(import.meta.env.VITE_N8N_CONTACTO_WEBHOOK, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    nombre: formData.nombre,
                    empresa: formData.empresa,
                    cargo: formData.cargo,
                    email: formData.email,
                    celular: formData.celular,
                    mensaje: formData.mensaje,
                    origen: formData.origen,
                    agreement: formData.agreement ? 'Sí' : 'No',
                })
            });

            if (response.ok) {
                setSubmitStatus('success');
                setTimeout(() => {
                    onClose();
                    setFormData({ 
                        nombre: '', 
                        empresa: '', 
                        cargo: '', 
                        email: '', 
                        celular: '', 
                        mensaje: '', 
                        origen: source, 
                        agreement: false 
                    });
                    setSubmitStatus(null);
                    if (onSuccess) onSuccess();
                }, 2000);
            } else {
                setSubmitStatus('error');
            }
        } catch (error) {
            console.error('Error sending form:', error);
            setSubmitStatus('error');
        } finally {
            setIsSubmitting(false);
        }
    };

    if (!isOpen) return null;

    const modalOverlayStyle = {
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        backgroundColor: 'rgba(0, 0, 0, 0.8)',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        zIndex: 10000,
        padding: '20px',
    };

    const modalContentStyle = {
        backgroundColor: 'var(--card-background)',
        borderRadius: '20px',
        padding: '40px',
        maxWidth: '500px',
        width: '100%',
        position: 'relative',
        border: '1px solid rgba(255, 255, 255, 0.1)',
    };

    const closeButtonStyle = {
        position: 'absolute',
        top: '20px',
        right: '20px',
        background: 'none',
        border: 'none',
        color: 'var(--text-color)',
        fontSize: '1.5rem',
        cursor: 'pointer',
        padding: '5px',
    };

    const titleStyle = {
        fontSize: '2rem',
        fontWeight: '700',
        marginBottom: '10px',
        color: 'var(--text-color)',
        fontFamily: 'var(--font-heading)',
    };

    const subtitleStyle = {
        fontSize: '0.95rem',
        color: 'var(--secondary-text-color)',
        marginBottom: '30px',
    };

    const formStyle = {
        display: 'flex',
        flexDirection: 'column',
        gap: '20px',
    };

    const inputStyle = {
        padding: '14px',
        borderRadius: '8px',
        border: '1px solid rgba(255, 255, 255, 0.1)',
        backgroundColor: 'rgba(0, 0, 0, 0.3)',
        color: 'var(--text-color)',
        fontSize: '1rem',
        fontFamily: 'inherit',
        outline: 'none',
        transition: 'border-color 0.3s',
    };

    const buttonStyle = {
        padding: '14px 28px',
        borderRadius: '8px',
        backgroundColor: 'var(--primary-color)',
        color: '#FFFFFF',
        border: 'none',
        fontSize: '1rem',
        fontWeight: '700',
        cursor: isSubmitting ? 'not-allowed' : 'pointer',
        textTransform: 'uppercase',
        letterSpacing: '1px',
        fontFamily: 'var(--font-heading)',
        opacity: isSubmitting ? 0.6 : 1,
    };

    const successMessageStyle = {
        padding: '15px',
        borderRadius: '8px',
        backgroundColor: 'rgba(56, 161, 105, 0.2)',
        border: '1px solid var(--primary-color)',
        color: 'var(--primary-color)',
        textAlign: 'center',
        fontWeight: '600',
    };

    const errorMessageStyle = {
        padding: '15px',
        borderRadius: '8px',
        backgroundColor: 'rgba(220, 38, 38, 0.2)',
        border: '1px solid #DC2626',
        color: '#FCA5A5',
        textAlign: 'center',
        fontWeight: '600',
    };

    const checkboxContainerStyle = {
        display: 'flex',
        alignItems: 'flex-start',
        gap: '10px',
        fontSize: '0.9rem',
        color: 'var(--text-color)',
    };

    const checkboxStyle = {
        marginTop: '3px',
        accentColor: 'var(--primary-color)',
        width: '16px',
        height: '16px',
        cursor: 'pointer',
    };

    return (
        <div style={modalOverlayStyle} onClick={onClose}>
            <div style={modalContentStyle} onClick={(e) => e.stopPropagation()}>
                <button style={closeButtonStyle} onClick={onClose}>×</button>

                <h2 style={titleStyle}>Contáctanos</h2>
                <p style={subtitleStyle}>Completa el formulario y nos pondremos en contacto contigo pronto.</p>

                {submitStatus === 'success' && (
                    <div style={successMessageStyle}>
                        ¡Gracias! Pronto nos pondremos en contacto.
                    </div>
                )}

                {submitStatus === 'error' && (
                    <div style={errorMessageStyle}>
                        Hubo un error. Por favor intenta de nuevo o contáctanos directamente.
                    </div>
                )}

                <form style={formStyle} onSubmit={handleSubmit}>
                    <input
                        type="text"
                        name="nombre"
                        placeholder="Nombre del Responsable *"
                        value={formData.nombre}
                        onChange={handleChange}
                        required
                        style={inputStyle}
                        onFocus={(e) => e.target.style.borderColor = 'var(--primary-color)'}
                        onBlur={(e) => e.target.style.borderColor = 'rgba(255, 255, 255, 0.1)'}
                    />

                    <input
                        type="text"
                        name="empresa"
                        placeholder="Empresa *"
                        value={formData.empresa}
                        onChange={handleChange}
                        required
                        style={inputStyle}
                        onFocus={(e) => e.target.style.borderColor = 'var(--primary-color)'}
                        onBlur={(e) => e.target.style.borderColor = 'rgba(255, 255, 255, 0.1)'}
                    />

                    <input
                        type="text"
                        name="cargo"
                        placeholder="Cargo / Puesto *"
                        value={formData.cargo}
                        onChange={handleChange}
                        required
                        style={inputStyle}
                        onFocus={(e) => e.target.style.borderColor = 'var(--primary-color)'}
                        onBlur={(e) => e.target.style.borderColor = 'rgba(255, 255, 255, 0.1)'}
                    />

                    <input
                        type="email"
                        name="email"
                        placeholder="Correo Corporativo *"
                        value={formData.email}
                        onChange={handleChange}
                        required
                        style={inputStyle}
                        onFocus={(e) => e.target.style.borderColor = 'var(--primary-color)'}
                        onBlur={(e) => e.target.style.borderColor = 'rgba(255, 255, 255, 0.1)'}
                    />

                    <input
                        type="tel"
                        name="celular"
                        placeholder="Celular *"
                        value={formData.celular}
                        onChange={handleChange}
                        required
                        style={inputStyle}
                        onFocus={(e) => e.target.style.borderColor = 'var(--primary-color)'}
                        onBlur={(e) => e.target.style.borderColor = 'rgba(255, 255, 255, 0.1)'}
                    />

                    <textarea
                        name="mensaje"
                        placeholder="Mensaje / Comentarios"
                        value={formData.mensaje}
                        onChange={handleChange}
                        rows="4"
                        style={inputStyle}
                        onFocus={(e) => e.target.style.borderColor = 'var(--primary-color)'}
                        onBlur={(e) => e.target.style.borderColor = 'rgba(255, 255, 255, 0.1)'}
                    />

                    <label style={checkboxContainerStyle}>
                        <input
                            type="checkbox"
                            name="agreement"
                            checked={formData.agreement}
                            onChange={(e) => setFormData({ ...formData, agreement: e.target.checked })}
                            required
                            style={checkboxStyle}
                        />
                        <span>Entiendo que esta información se compartirá con NexIA Soluciones para fines de contacto empresarial.</span>
                    </label>

                    <button type="submit" style={buttonStyle} disabled={isSubmitting}>
                        {isSubmitting ? 'Enviando...' : 'Enviar Mensaje'}
                    </button>
                </form>
            </div>
        </div>
    );
};

export default ContactModal;
