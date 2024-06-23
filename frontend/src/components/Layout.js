// frontend/src/components/Layout.js
// src/components/Layout.js
import React from 'react';
import { AppBar, Toolbar, Typography, Container, Button } from '@mui/material';
import { Link, useNavigate } from 'react-router-dom';
import { logout } from '../services/auth';

const Layout = ({ children, isAuthenticated, setIsAuthenticated }) => {
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    setIsAuthenticated(false);
    navigate('/login');
  };

  return (
    <>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" style={{ flexGrow: 1 }}>
            DS
          </Typography>
          {isAuthenticated ? (
            <>
              <Button color="inherit" component={Link} to="/">
                Home
              </Button>
              <Button color="inherit" component={Link} to="/vendors">
                Vendors
              </Button>
              <Button color="inherit" component={Link} to="/vendor-contacts">
                Vendor Contacts
              </Button>
              <Button color="inherit" component={Link} to="/inventories">
                Inventory
              </Button>
              <Button color="inherit" component={Link} to="/products">
                Products
              </Button>
              <Button color="inherit" onClick={handleLogout}>
                Logout
              </Button>
            </>
          ) : (
            <Button color="inherit" component={Link} to="/login">
              Login
            </Button>
          )}
        </Toolbar>
      </AppBar>
      <Container style={{ marginTop: '20px' }}>{children}</Container>
    </>
  );
};

export default Layout;