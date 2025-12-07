import React, { useState } from 'react';
import Button from './Button';
import ContactModal from './ContactModal';
import FileViewerModal from './FileViewerModal';

const Academy = () => {
    const [unlockedModules, setUnlockedModules] = useState({});
    const [contactModalOpen, setContactModalOpen] = useState(false);
    const [viewerModalOpen, setViewerModalOpen] = useState(false);
    const [currentModule, setCurrentModule] = useState(null);
    const [viewerConfig, setViewerConfig] = useState({ url: '', type: 'pdf', title: '' });

    const modules = [
        {
            id: 'asistente',
            title: "Asistente IA",
            copy: "Dominio Práctico: Configura tu asistente de IA en 30 minutos. Enfocado en flujos de trabajo internos para maximizar la productividad.",
            pdf: "/academy/NexIA-Asistentes_de_IA.pdf",
            img: "/academy/NexIA-Asistentes_de_IA.jpg"
        },
        {
            id: 'seguridad',
            title: "Seguridad Inteligente",
            copy: "Ciberseguridad Proactiva: Estrategias impulsadas por IA para identificar amenazas antes de que escalen y proteger tus activos digitales.",
            pdf: "/academy/NexIA-SeguridadInteligente.pdf",
            img: "/academy/NexIA-SeguridadInteligente.jpg"
        },
        {
            id: 'cto',
            title: "CTO Moderno",
            copy: "Liderazgo de Impacto: Aprende a evaluar, seleccionar e implementar tecnología que garantice un ROI claro y sostenible.",
            pdf: "/academy/NexIA-CTO_Arquitecto_del_Futuro.pdf",
            img: "/academy/NexIA-CTO_Arquitecto_del_Futuro.jpg"
        }
    ];

    const handleUnlockClick = (module) => {
        setCurrentModule(module);
        setContactModalOpen(true);
    };

    const handleSuccess = () => {
        if (currentModule) {
            setUnlockedModules(prev => ({
                ...prev,
                [currentModule.id]: true
            }));
        }
    };

    const handleViewPdf = (module) => {
        setViewerConfig({
            url: module.pdf,
            type: 'pdf',
            title: `${module.title} - Diapositivas`
        });
        setViewerModalOpen(true);
    };

    const handleViewImg = (module) => {
        setViewerConfig({
            url: module.img,
            type: 'image',
            title: `${module.title} - Infografía`
        });
        setViewerModalOpen(true);
    };

    const sectionStyle = {
        padding: '100px 5%',
        backgroundColor: '#171923',
        color: '#FFFFFF',
        textAlign: 'center',
    };

    const titleStyle = {
        fontSize: '2.5rem',
        fontWeight: '700',
        marginBottom: '60px',
        color: '#FFFFFF',
        textTransform: 'uppercase',
        letterSpacing: '1px',
        fontFamily: 'var(--font-heading)',
    };

    const gridStyle = {
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(350px, 1fr))',
        gap: '40px',
        maxWidth: '1200px',
        margin: '0 auto',
    };

    const courseCardStyle = {
        backgroundColor: 'rgba(255, 255, 255, 0.05)',
        padding: '40px',
        borderRadius: '16px',
        textAlign: 'left',
        backdropFilter: 'blur(10px)',
        border: '1px solid rgba(255, 255, 255, 0.1)',
        transition: 'all 0.3s ease',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'space-between',
        height: '100%',
    };

    const courseTitleStyle = {
        fontSize: '1.5rem',
        fontWeight: '700',
        marginBottom: '15px',
        color: 'var(--primary-color)',
        fontFamily: 'var(--font-heading)',
    };

    const courseDescStyle = {
        color: 'var(--secondary-text-color)',
        fontSize: '1rem',
        marginBottom: '30px',
        lineHeight: '1.6',
        flex: 1,
    };

    const buttonGroupStyle = {
        display: 'flex',
        flexDirection: 'column',
        gap: '12px',
    };

    return (
        <section id="academy" style={sectionStyle}>
            <h2 style={titleStyle}>Academia NexIA</h2>

            <div style={gridStyle}>
                {modules.map((module) => {
                    const isUnlocked = unlockedModules[module.id];

                    return (
                        <div key={module.id} style={courseCardStyle}>
                            <div>
                                <h3 style={courseTitleStyle}>{module.title}</h3>
                                <p style={courseDescStyle}>{module.copy}</p>
                            </div>

                            <div style={buttonGroupStyle}>
                                {!isUnlocked ? (
                                    <Button
                                        variant="primary"
                                        onClick={() => handleUnlockClick(module)}
                                        style={{ width: '100%' }}
                                    >
                                        Acceder al Material
                                    </Button>
                                ) : (
                                    <>
                                        <Button
                                            variant="secondary"
                                            onClick={() => handleViewPdf(module)}
                                            style={{ width: '100%', backgroundColor: 'rgba(56, 161, 105, 0.2)', color: '#48BB78', border: '1px solid #48BB78' }}
                                        >
                                            Descargar Diapositivas
                                        </Button>
                                        <Button
                                            variant="secondary"
                                            onClick={() => handleViewImg(module)}
                                            style={{ width: '100%' }}
                                        >
                                            Ver Infografía
                                        </Button>
                                    </>
                                )}
                            </div>
                        </div>
                    );
                })}
            </div>

            <ContactModal
                isOpen={contactModalOpen}
                onClose={() => setContactModalOpen(false)}
                source={currentModule ? `Academia - ${currentModule.title}` : 'Academia'}
                onSuccess={handleSuccess}
            />

            <FileViewerModal
                isOpen={viewerModalOpen}
                onClose={() => setViewerModalOpen(false)}
                fileUrl={viewerConfig.url}
                fileType={viewerConfig.type}
                title={viewerConfig.title}
            />
        </section>
    );
};

export default Academy;
