import axios from "axios";

const API_BASE = "http://localhost:8000";

export const login = async (username, password) => {
  const response = await axios.post(`${API_BASE}/token`, new URLSearchParams({
    username,
    password,
  }));
  return response.data.access_token;
};

export const getTreatment = async (symptom, token) => {
  const response = await axios.post(
    `${API_BASE}/predict_treatment`,
    { symptom },
    { headers: { Authorization: `Bearer ${token}` } }
  );
  return response.data;
};
