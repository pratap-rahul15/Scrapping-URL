import React, { useState } from "react";

const SearchForm = ({ onSearch }) => {
  const [url, setUrl] = useState("");
  const [query, setQuery] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    onSearch({ url, query });
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4 w-full max-w-2xl">
      <div>
        <input
          type="text"
          placeholder="Enter website URL"
          className="w-full p-3 rounded border border-gray-300 shadow"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          required
        />
      </div>
      <div className="flex space-x-2">
        <input
          type="text"
          placeholder="Enter your search query"
          className="flex-1 p-3 rounded border border-gray-300 shadow"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          required
        />
        <button
          type="submit"
          className="bg-blue-600 text-white px-6 py-2 rounded shadow hover:bg-blue-700"
        >
          Search
        </button>
      </div>
    </form>
  );
};

export default SearchForm;
