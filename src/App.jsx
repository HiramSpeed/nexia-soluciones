import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, useLocation } from 'react-router-dom';
import Header from './components/Header';
import Hero from './components/Hero';
import MissionVision from './components/MissionVision';
import Benefits from './components/Benefits';
import Consulting from './components/Consulting';
import Academy from './components/Academy';
import Footer from './components/Footer';
import ContactModal from './components/ContactModal';
import PrivacyPolicyModal from './components/PrivacyPolicyModal';
import ProductsPage from './components/ProductsPage';
import AppLanding from './components/AppLanding';
import ScrollToTop from './components/ScrollToTop';
import ParticleCanvas from './components/ParticleCanvas';
// import Testimonials from './components/Testimonials'; // TEMPORALMENTE DESHABILITADO - Pendiente de autorización de clientes

// Componente auxiliar para manejar el scroll con hash
const HashScrollHandler = () => {
  const { pathname, hash, key } = useLocation();

  useEffect(() => {
    // Si no hay hash, scroll arriba (ScrollToTop ya lo hace, pero reforzamos)
    if (hash === '') {
      window.scrollTo(0, 0);
    }
    // Si hay hash, esperar un momento al render y hacer scroll
    else {
      setTimeout(() => {
        const id = hash.replace('#', '');
        const element = document.getElementById(id);
        if (element) {
          element.scrollIntoView({ behavior: 'smooth' });
        }
      }, 100); // Pequeño delay para asegurar que el DOM existe
    }
  }, [pathname, hash, key]);

  return null;
};

function App() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [modalSource, setModalSource] = useState('General');
  const [isPrivacyOpen, setIsPrivacyOpen] = useState(false);

  const openModal = (source) => {
    setModalSource(source);
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

  const openPrivacy = () => {
    setIsPrivacyOpen(true);
  };

  const closePrivacy = () => {
    setIsPrivacyOpen(false);
  };

  return (
    <Router>
      <ScrollToTop />
      <HashScrollHandler />
      <div className="App">
        <ParticleCanvas />
        <Header openModal={openModal} />

        <Routes>
          <Route path="/" element={
            <>
              <Hero openModal={openModal} />
              <MissionVision />
              <ProductsPage openModal={openModal} />
              <Benefits />
              <Consulting openModal={openModal} />
              <Academy openModal={openModal} />
            </>
          } />
          <Route path="/planner" element={<AppLanding slug="nexia-planner" />} />
          <Route path="/facturacion" element={<AppLanding slug="nexia-facturacion" />} />
          <Route path="/tienda" element={<AppLanding slug="nexia-tienda" />} />
        </Routes>

        {/* SECCIÓN TEMPORALMENTE DESHABILITADA */}
        {/* TODO: Habilitar cuando se obtenga autorización de los clientes para usar sus testimonios */}
        {/* <Testimonials /> */}
        <Footer openPrivacy={openPrivacy} openModal={openModal} />
        <ContactModal isOpen={isModalOpen} onClose={closeModal} source={modalSource} />
        <PrivacyPolicyModal isOpen={isPrivacyOpen} onClose={closePrivacy} />
      </div>
    </Router>
  );
}

export default App;
