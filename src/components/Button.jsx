import React from 'react';

const Button = ({ children, onClick, variant = 'primary', className = '' }) => {
    const baseStyle = {
        padding: '12px 24px',
        borderRadius: '8px',
        fontWeight: '700',
        fontSize: '1rem',
        transition: 'all 0.3s ease',
        cursor: 'pointer',
        border: 'none',
        textTransform: 'uppercase',
        letterSpacing: '1px',
    };

    const variants = {
        primary: {
            backgroundColor: 'var(--primary-color)',
            color: '#FFFFFF',
            boxShadow: '0 4px 15px rgba(0, 163, 255, 0.4)',
        },
        secondary: {
            backgroundColor: 'transparent',
            border: '2px solid var(--primary-color)',
            color: 'var(--primary-color)',
        },
        text: {
            backgroundColor: 'transparent',
            color: 'var(--text-color)',
            padding: '12px 16px',
        }
    };

    return (
        <button
            style={{ ...baseStyle, ...variants[variant] }}
            className={className}
            onClick={onClick}
            onMouseEnter={(e) => {
                if (variant === 'primary') {
                    e.currentTarget.style.backgroundColor = 'var(--primary-hover)';
                    e.currentTarget.style.transform = 'translateY(-2px)';
                }
            }}
            onMouseLeave={(e) => {
                if (variant === 'primary') {
                    e.currentTarget.style.backgroundColor = 'var(--primary-color)';
                    e.currentTarget.style.transform = 'translateY(0)';
                }
            }}
        >
            {children}
        </button>
    );
};

export default Button;
