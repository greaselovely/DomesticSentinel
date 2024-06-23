// frontend/src/pages/VendorContactsList.js
import React, { useState, useEffect } from 'react';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Typography, CircularProgress } from '@mui/material';
import api from '../services/api';

const VendorContactsList = () => {
  const [vendorContacts, setVendorContacts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchVendorContacts = async () => {
      try {
        setLoading(true);
        const response = await api.get('vendor-contacts/');
        setVendorContacts(response.data);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching vendor contacts:', error);
        setError('Failed to fetch vendor contacts. Please try again later.');
        setLoading(false);
      }
    };

    fetchVendorContacts();
  }, []);

  if (loading) return <CircularProgress />;
  if (error) return <Typography color="error">{error}</Typography>;

  return (
    <div>
      <Typography variant="h4" gutterBottom>
        Vendor Contacts
      </Typography>
      {vendorContacts.length === 0 ? (
        <Typography>No vendor contacts found.</Typography>
      ) : (
        <TableContainer component={Paper}>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>First Name</TableCell>
                <TableCell>Last Name</TableCell>
                <TableCell>Title</TableCell>
                <TableCell>Email</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {vendorContacts.map((contact) => (
                <TableRow key={contact.id}>
                  <TableCell>{contact.first_name}</TableCell>
                  <TableCell>{contact.last_name}</TableCell>
                  <TableCell>{contact.title}</TableCell>
                  <TableCell>{contact.email}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      )}
    </div>
  );
};

export default VendorContactsList;