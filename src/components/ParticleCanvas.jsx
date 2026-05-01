import { useEffect, useRef } from 'react';

const ParticleCanvas = () => {
  const canvasRef = useRef(null);
  const mouseRef = useRef({ x: -1000, y: -1000 });
  const animRef = useRef(0);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');

    // Colores corporativos NexIA
    const PRIMARY = '0, 163, 255';   // #00A3FF
    const ACCENT  = '0, 129, 204';   // #0081CC

    let W = canvas.width  = window.innerWidth;
    let H = canvas.height = window.innerHeight;

    const count = Math.min(70, Math.floor(W * H / 20000));
    const particles = Array.from({ length: count }, () => ({
      x: Math.random() * W,
      y: Math.random() * H,
      vx: (Math.random() - 0.5) * 0.35,
      vy: (Math.random() - 0.5) * 0.35,
      r: Math.random() * 1.5 + 0.5,
    }));

    const onResize = () => {
      W = canvas.width  = window.innerWidth;
      H = canvas.height = window.innerHeight;
    };
    const onMove = (e) => {
      mouseRef.current = { x: e.clientX, y: e.clientY };
    };

    window.addEventListener('resize', onResize);
    window.addEventListener('mousemove', onMove);

    const draw = () => {
      ctx.clearRect(0, 0, W, H);
      const { x: mx, y: my } = mouseRef.current;

      for (let i = 0; i < particles.length; i++) {
        const p = particles[i];
        p.x += p.vx;
        p.y += p.vy;
        if (p.x < 0 || p.x > W) p.vx *= -1;
        if (p.y < 0 || p.y > H) p.vy *= -1;

        const dx = mx - p.x;
        const dy = my - p.y;
        const dist = Math.sqrt(dx * dx + dy * dy);

        // Atracción suave al cursor
        if (dist < 180) {
          p.x += dx * 0.007;
          p.y += dy * 0.007;
        }

        // Dibujar partícula
        const alpha = dist < 180 ? 0.85 : 0.3;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(${PRIMARY}, ${alpha})`;
        ctx.fill();

        // Líneas entre partículas
        for (let j = i + 1; j < particles.length; j++) {
          const q = particles[j];
          const ex = p.x - q.x;
          const ey = p.y - q.y;
          const ed = Math.sqrt(ex * ex + ey * ey);
          if (ed < 140) {
            const a = (1 - ed / 140) * 0.12;
            ctx.beginPath();
            ctx.moveTo(p.x, p.y);
            ctx.lineTo(q.x, q.y);
            ctx.strokeStyle = `rgba(${ACCENT}, ${a})`;
            ctx.lineWidth = 0.6;
            ctx.stroke();
          }
        }

        // Línea al cursor
        if (dist < 180) {
          const a = (1 - dist / 180) * 0.35;
          ctx.beginPath();
          ctx.moveTo(p.x, p.y);
          ctx.lineTo(mx, my);
          ctx.strokeStyle = `rgba(${PRIMARY}, ${a})`;
          ctx.lineWidth = 0.8;
          ctx.stroke();
        }
      }

      animRef.current = requestAnimationFrame(draw);
    };

    draw();

    return () => {
      cancelAnimationFrame(animRef.current);
      window.removeEventListener('resize', onResize);
      window.removeEventListener('mousemove', onMove);
    };
  }, []);

  return (
    <canvas
      ref={canvasRef}
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        width: '100%',
        height: '100%',
        zIndex: 0,
        pointerEvents: 'none',
      }}
    />
  );
};

export default ParticleCanvas;
