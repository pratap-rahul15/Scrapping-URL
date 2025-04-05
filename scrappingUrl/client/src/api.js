import axios from "axios";

const BASE_URL = "http://localhost:8000";

export const searchWebsite = async (url, query) => {
  const response = await axios.post(`${BASE_URL}/search`, { url, query });
  return response.data;
};
