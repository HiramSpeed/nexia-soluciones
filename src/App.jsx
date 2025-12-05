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

function App() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [modalSource, setModalSource] = useState('General');

  const openModal = (source) => {
    setModalSource(source);
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
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
      <Footer />
      <ContactModal isOpen={isModalOpen} onClose={closeModal} source={modalSource} />
    </div>
  );
}

export default App;
