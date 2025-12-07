import React from 'react';

const FileViewerModal = ({ isOpen, onClose, fileUrl, fileType, title }) => {
    if (!isOpen) return null;

    const modalOverlayStyle = {
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        backgroundColor: 'rgba(0, 0, 0, 0.9)',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        zIndex: 10001, // Higher than ContactModal
        padding: '20px',
    };

    const modalContentStyle = {
        backgroundColor: '#1A1A1A',
        borderRadius: '12px',
        width: '100%',
        maxWidth: '1000px',
        height: '90vh',
        position: 'relative',
        display: 'flex',
        flexDirection: 'column',
    };

    const headerStyle = {
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        padding: '15px 20px',
        borderBottom: '1px solid rgba(255, 255, 255, 0.1)',
    };

    const closeButtonStyle = {
        background: 'none',
        border: 'none',
        color: '#FFFFFF',
        fontSize: '2rem',
        cursor: 'pointer',
        padding: '0 10px',
        lineHeight: '1',
    };

    const contentContainerStyle = {
        flex: 1,
        overflow: 'hidden',
        padding: '20px',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
    };

    return (
        <div style={modalOverlayStyle} onClick={onClose}>
            <div style={modalContentStyle} onClick={(e) => e.stopPropagation()}>
                <div style={headerStyle}>
                    <h3 style={{ margin: 0, color: '#FFFFFF', fontSize: '1.2rem' }}>{title}</h3>
                    <button style={closeButtonStyle} onClick={onClose}>×</button>
                </div>

                <div style={contentContainerStyle}>
                    {fileType === 'pdf' ? (
                        <iframe
                            src={fileUrl}
                            style={{ width: '100%', height: '100%', border: 'none', backgroundColor: '#FFFFFF' }}
                            title="PDF Viewer"
                        />
                    ) : (
                        <img
                            src={fileUrl}
                            alt={title}
                            style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain' }}
                        />
                    )}
                </div>
            </div>
        </div>
    );
};

export default FileViewerModal;
