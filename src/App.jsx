import React, { useState } from 'react';
import Header from './components/Header';
import Hero from './components/Hero';
import Benefits from './components/Benefits';
import Products from './components/Products';
import Consulting from './components/Consulting';
import Academy from './components/Academy';
// import Testimonials from './components/Testimonials'; // TEMPORALMENTE DESHABILITADO - Pendiente de autorización de clientes
import Footer from './components/Footer';
import ContactModal from './components/ContactModal';
import PrivacyPolicyModal from './components/PrivacyPolicyModal';

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
    <div className="App">
      <Header openModal={openModal} />
      <Hero openModal={openModal} />
      <Benefits />
      <Products openModal={openModal} />
      <Consulting openModal={openModal} />
      <Academy openModal={openModal} />
      {/* SECCIÓN TEMPORALMENTE DESHABILITADA */}
      {/* TODO: Habilitar cuando se obtenga autorización de los clientes para usar sus testimonios */}
      {/* <Testimonials /> */}
      <Footer openPrivacy={openPrivacy} />
      <ContactModal isOpen={isModalOpen} onClose={closeModal} source={modalSource} />
      <PrivacyPolicyModal isOpen={isPrivacyOpen} onClose={closePrivacy} />
    </div>
  );
}

export default App;
