import React from 'react';
import Navbar from '../components/Navbar/Navbar';
import Footer from '../components/Footer/Footer';
import Generate_Header from '../components/Header/Generate_Header';

const Generate = () => {
  return (
    <div className='generate'>
      <Navbar />
      <Generate_Header />
      <Footer />
    </div>
  );
}

export default Generate;