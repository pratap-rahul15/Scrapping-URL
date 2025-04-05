import { useState } from "react";
import "./App.css";
import { searchWebsite } from "./api";
import SearchForm from "./components/SearchForm";
import Results from "./components/Results";

function App() {
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async ({ url, query }) => {
    setLoading(true);
    try {
      const data = await searchWebsite(url, query);
      setResults(data);
    } catch (err) {
      console.error(err);
      alert("Something went wrong!");
    } finally {
      setLoading(false);
    }
  };
  return (
    <div className="min-h-screen p-8 bg-gray-100 flex flex-col items-center">
      <h1 className="text-3xl font-bold mb-2">Website Content Search</h1>
      <p className="mb-6 text-gray-600 text-center">
        Search through website content with precision
      </p>

      <SearchForm onSearch={handleSearch} />

      {loading ? (
        <div className="mt-8 text-lg font-semibold">Searching...</div>
      ) : (
        <Results results={results} />
      )}
    </div>
  );
}

export default App;
