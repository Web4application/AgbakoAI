import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:5000/api',
});

export const login = (username, password) => {
  return api.post('/login', { username, password });
};

export default api;
