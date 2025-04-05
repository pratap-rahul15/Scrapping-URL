import React, { useState } from "react";

const Results = ({ results }) => {
  if (!results.length) return null;

  return (
    <div className="mt-8 grid gap-4 w-full max-w-4xl">
      {results.map((item, index) => (
        <ChunkCard
          key={index}
          index={index}
          text={item.text}
          html={item.html}
        />
      ))}
    </div>
  );
};

const ChunkCard = ({ index, text, html }) => {
  const [showHtml, setShowHtml] = useState(false);

  return (
    <div className="p-4 border rounded shadow bg-white">
      <h3 className="text-lg font-semibold mb-2">Result #{index + 1}</h3>

      
      <p className="text-gray-700 whitespace-pre-wrap">{text}</p>

      
      <button
        onClick={() => setShowHtml(!showHtml)}
        className="mt-4 text-blue-600 text-sm inline-flex items-center gap-1"
      >
        <span className="font-mono text-base">&lt;&gt;</span>
        {showHtml ? "Hide HTML" : "View HTML"}
        <span>{showHtml ? "⌃" : "⌄"}</span>
      </button>

     
      {showHtml && (
        <div
          className="mt-3 bg-gray-100 p-3 rounded text-sm overflow-auto border"
          dangerouslySetInnerHTML={{ __html: html }}
        />
      )}
    </div>
  );
};

export default Results;
