// frontend/src/services/api.js
// src/services/api.js
import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const setAuthToken = (token) => {
  if (token) {
    api.defaults.headers.common['Authorization'] = `Token ${token}`;
  } else {
    delete api.defaults.headers.common['Authorization'];
  }
};

export const login = async (username, password) => {
  const response = await api.post('auth/', { username, password });
  const token = response.data.token;
  localStorage.setItem('token', token);
  setAuthToken(token);
  return response.data;
};

export const logout = () => {
  localStorage.removeItem('token');
  setAuthToken(null);
};

export default api;