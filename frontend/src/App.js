// frontend/src/App.js
import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Layout from './components/Layout';
import Home from './pages/Home';
import VendorList from './pages/VendorList';
import Login from './pages/Login';
import { checkAuth } from './services/auth';
import VendorContactsList from './pages/VendorContactsList';
import InventoriesList from './pages/InventoriesList';
import ProductsList from './pages/ProductsList';
import ProductDetail from './pages/ProductDetail';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    setIsAuthenticated(checkAuth());
  }, []);

  return (
    <Router>
      <Layout isAuthenticated={isAuthenticated} setIsAuthenticated={setIsAuthenticated}>
        <Routes>
          <Route path="/login" element={<Login setIsAuthenticated={setIsAuthenticated} />} />
          <Route path="/" element={isAuthenticated ? <Home /> : <Navigate to="/login" />} />
          <Route path="/vendors" element={isAuthenticated ? <VendorList /> : <Navigate to="/login" />} />
          <Route path="/vendor-contacts" element={isAuthenticated ? <VendorContactsList /> : <Navigate to="/login" />} />
          <Route path="/inventories" element={isAuthenticated ? <InventoriesList /> : <Navigate to="/login" />} />
          <Route path="/products" element={isAuthenticated ? <ProductsList /> : <Navigate to="/login" />} />
          <Route path="/products/:id" element={isAuthenticated ? <ProductDetail /> : <Navigate to="/login" />} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;
