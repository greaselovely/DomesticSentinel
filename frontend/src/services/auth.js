// frontend/src/services/auth.js
import api, { setAuthToken } from './api';

export const login = async (username, password) => {
    try {
      console.log('Sending login request');
      const response = await api.post('auth/', { username, password });
      console.log('Login response:', response.data);
      const token = response.data.token;
      if (token) {
        console.log('Token received, setting in localStorage');
        localStorage.setItem('token', token);
        setAuthToken(token);
      } else {
        console.error('No token received in login response');
      }
      return response.data;
    } catch (error) {
      console.error('Login error:', error.response ? error.response.data : error.message);
      throw error;
    }
  };

export const logout = () => {
  localStorage.removeItem('token');
  setAuthToken(null);
};

export const checkAuth = () => {
  const token = localStorage.getItem('token');
  if (token) {
    setAuthToken(token);
    return true;
  }
  return false;
};