// frontend/src/pages/ProductDetail.js
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { Typography, Box, TextField, Button, CircularProgress } from '@mui/material';
import api from '../services/api';

const ProductDetail = () => {
  const { id } = useParams();
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [isEditing, setIsEditing] = useState(false);
  const [formValues, setFormValues] = useState({
    name: '',
    description: '',
    manufacturer: '',
    url: '',
    price: '',
  });

  useEffect(() => {
    const fetchProduct = async () => {
      try {
        const response = await api.get(`products/${id}/`);
        setFormValues(response.data);
        setLoading(false);
      } catch (error) {
        setError('Failed to fetch product. Please try again later.');
        setLoading(false);
      }
    };

    fetchProduct();
  }, [id]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormValues({
      ...formValues,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.put(`products/${id}/`, formValues);
      setIsEditing(false); // Exit editing mode
    } catch (error) {
      setError('Failed to update product. Please try again later.');
    }
  };

  if (loading) return <CircularProgress />;
  if (error) return <Typography color="error">{error}</Typography>;

  return (
    <Box sx={{ padding: 2 }}>
      <Typography variant="h4" gutterBottom>
        {isEditing ? 'Edit Product' : 'Product Details'}
      </Typography>
      {isEditing ? (
        <form onSubmit={handleSubmit}>
          <TextField
            label="Name"
            name="name"
            value={formValues.name}
            onChange={handleInputChange}
            fullWidth
            margin="normal"
          />
          <TextField
            label="Description"
            name="description"
            value={formValues.description}
            onChange={handleInputChange}
            fullWidth
            multiline
            rows={4}
            margin="normal"
          />
          <TextField
            label="Manufacturer"
            name="manufacturer"
            value={formValues.manufacturer}
            onChange={handleInputChange}
            fullWidth
            margin="normal"
          />
          <TextField
            label="URL"
            name="url"
            value={formValues.url}
            onChange={handleInputChange}
            fullWidth
            margin="normal"
          />
          <TextField
            label="Price"
            name="price"
            type="number"
            value={formValues.price}
            onChange={handleInputChange}
            fullWidth
            margin="normal"
          />
          <Button type="submit" variant="contained" sx={{ mt: 3, mr: 2 }}>
            Save Changes
          </Button>
          <Button variant="outlined" sx={{ mt: 3 }} onClick={() => setIsEditing(false)}>
            Cancel
          </Button>
        </form>
      ) : (
        <div>
          <Typography variant="h6" gutterBottom>
            Name:
          </Typography>
          <Typography paragraph>{formValues.name}</Typography>
          {formValues.image && (
            <img src={formValues.image} alt={formValues.name} style={{ width: '100%', maxWidth: '400px' }} />
          )}
          <Typography variant="h6" gutterBottom>
            Description:
          </Typography>
          <Typography paragraph>{formValues.description}</Typography>
          <Typography variant="h6" gutterBottom>
            Manufacturer:
          </Typography>
          <Typography paragraph>{formValues.manufacturer}</Typography>
          <Typography variant="h6" gutterBottom>
            Price:
          </Typography>
          <Typography paragraph>${formValues.price}</Typography>
          {formValues.url && (
            <>
              <Typography variant="h6" gutterBottom>
                More Info:
              </Typography>
              <Typography paragraph>
                <a href={formValues.url} target="_blank" rel="noopener noreferrer">
                  {formValues.url}
                </a>
              </Typography>
            </>
          )}
          <Button variant="contained" sx={{ mt: 3 }} onClick={() => setIsEditing(true)}>
            Edit
          </Button>
        </div>
      )}
    </Box>
  );
};

export default ProductDetail;
