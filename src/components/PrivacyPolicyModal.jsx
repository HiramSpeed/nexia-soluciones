import React from 'react';
import Button from './Button';

const PrivacyPolicyModal = ({ isOpen, onClose }) => {
    if (!isOpen) return null;

    const overlayStyle = {
        position: 'fixed',
        top: 0,
        left: 0,
        width: '100%',
        height: '100%',
        backgroundColor: 'rgba(0, 0, 0, 0.75)',
        backdropFilter: 'blur(5px)',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        zIndex: 2000,
        padding: '20px'
    };

    const modalStyle = {
        backgroundColor: '#FFFFFF', // Fondo claro
        color: '#1a202c', // Texto oscuro para contraste
        padding: '30px',
        borderRadius: '16px',
        maxWidth: '700px',
        width: '100%',
        maxHeight: '85vh',
        overflowY: 'auto',
        position: 'relative',
        boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.25)'
    };

    const headerStyle = {
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        marginBottom: '20px',
        borderBottom: '1px solid #e2e8f0',
        paddingBottom: '15px'
    };

    const titleStyle = {
        color: '#2d3748',
        fontSize: '1.5rem',
        fontWeight: 'bold'
    };

    const closeButtonStyle = {
        background: 'none',
        border: 'none',
        fontSize: '1.5rem',
        cursor: 'pointer',
        color: '#718096'
    };

    const contentStyle = {
        lineHeight: '1.7',
        fontSize: '0.95rem'
    };

    const sectionTitleStyle = {
        fontSize: '1.1rem',
        fontWeight: 'bold',
        marginTop: '20px',
        marginBottom: '10px',
        color: '#2b6cb0' // Un azul tenue
    };

    return (
        <div style={overlayStyle} onClick={onClose} className="modal-overlay">
            <div style={modalStyle} onClick={e => e.stopPropagation()} className="modal-content">
                <div style={headerStyle}>
                    <h2 style={titleStyle}>AVISO DE PRIVACIDAD</h2>
                    <button style={closeButtonStyle} onClick={onClose}>×</button>
                </div>

                <div style={contentStyle}>
                    <p><strong>Daniel Hiram Navarro Muñoz</strong>, comercialmente conocido como <strong>NexIA Soluciones</strong>, con domicilio en Cto. Brianza 411. Residencial Lombardia, CP 38115 Celaya Guanajuato, es el responsable del uso y protección de sus datos personales.</p>

                    <h3 style={sectionTitleStyle}>FINALIDADES PRIMARIAS</h3>
                    <p>Los datos personales que recabamos de usted, los utilizaremos para las siguientes finalidades que son necesarias para el servicio que solicita:</p>
                    <ul style={{ listStyle: 'disc', paddingLeft: '20px', marginTop: '10px' }}>
                        <li>Respuesta a mensajes del formulario de contacto</li>
                        <li>Prestación de cualquier servicio solicitado</li>
                        <li>Envío de productos adquiridos en esta tienda en línea</li>
                    </ul>

                    <h3 style={sectionTitleStyle}>DATOS PERSONALES RECABADOS</h3>
                    <p>Para las finalidades señaladas en el presente aviso de privacidad, podemos recabar sus datos de identificación y contacto.</p>

                    <h3 style={sectionTitleStyle}>DERECHOS ARCO</h3>
                    <p>Usted tiene derecho a conocer qué datos personales tenemos de usted, para qué los utilizamos y las condiciones del uso que les damos (Acceso). Asimismo, es su derecho solicitar la corrección de su información personal en caso de que esté desactualizada, sea inexacta o incompleta (Rectificación); que la eliminemos de nuestros registros o bases de datos cuando considere que la misma no está siendo utilizada adecuadamente (Cancelación); así como oponerse al uso de sus datos personales para fines específicos (Oposición). Estos derechos se conocen como derechos ARCO.</p>
                    <p style={{ marginTop: '10px' }}>Para el ejercicio de cualquiera de los derechos ARCO, usted deberá presentar la solicitud respectiva a través del mismo correo electrónico de donde se envió la petición. La respuesta a su solicitud será atendida en un plazo máximo de 20 días hábiles.</p>

                    <h3 style={sectionTitleStyle}>DATOS RECABADOS POR EL SITIO WEB</h3>
                    <p>Nuestro sitio web recaba automáticamente los siguientes datos:</p>
                    <ul style={{ listStyle: 'disc', paddingLeft: '20px', marginTop: '10px' }}>
                        <li>Idioma preferido por el usuario</li>
                        <li>Región en la que se encuentra el usuario</li>
                        <li>Fecha y hora del inicio y final de una sesión de un usuario</li>
                    </ul>

                    <h3 style={sectionTitleStyle}>CONTACTO</h3>
                    <p>Para más información sobre este aviso de privacidad, puede contactarnos en:</p>
                    <p style={{ marginTop: '10px' }}>
                        <strong>Correo electrónico:</strong> daniel.navarro@nexiasoluciones.com.mx<br />
                        <strong>Sitio web:</strong> https://nexiasoluciones.com.mx
                    </p>

                    <p style={{ marginTop: '30px', fontSize: '0.85rem', color: '#718096', borderTop: '1px solid #e2e8f0', paddingTop: '10px' }}>
                        Última actualización: 12/5/2025
                    </p>
                </div>

                <div style={{ marginTop: '30px', textAlign: 'right' }}>
                    <Button variant="secondary" onClick={onClose} style={{ color: '#1a202c', borderColor: '#cbd5e0' }}>Cerrar</Button>
                </div>
            </div>
        </div>
    );
};

export default PrivacyPolicyModal;
