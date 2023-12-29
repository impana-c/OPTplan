import React from 'react';
import Navbar from '../components/Navbar/Navbar';
import Footer from '../components/Footer/Footer';
import Verify_Header from '../components/Header/Verify_Header';
const Verify = () => {
  return (
    <div>
      <div style={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
        <Navbar />
        <Verify_Header />
        <div style={{ flex: 1 }} className='container'>
          <main>
            <br /><br /><h1>Coming soon!</h1>
          </main>
          </div>
        <Footer />
      </div>
    </div>
  );
}

export default Verify;