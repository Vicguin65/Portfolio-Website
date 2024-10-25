import React from "react";
import { Document, Page } from "react-pdf";
import { useState } from "react";
import { pdfjs } from "react-pdf";
import "./ResumePage.css";

pdfjs.GlobalWorkerOptions.workerSrc = new URL(
  "pdfjs-dist/build/pdf.worker.min.mjs",
  import.meta.url
).toString();

const handleDownload = () => {
  const pdfUrl = "./Resume_Tyler_Du.pdf"; // Adjust the path if stored elsewhere
  const link = document.createElement("a");
  link.href = pdfUrl;
  link.download = "Resume_Tyler_Du.pdf"; // Set the download file name
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
};

function ResumePage() {
  const [numPages, setNumPages] = useState(1);
  const [pageNumber, setPageNumber] = useState(1);
  const [isZoomed, setIsZoomed] = useState(false);

  const toggleZoom = () => {
    setIsZoomed((prevZoom) => !prevZoom);
  };

  return (
    <div style={{ display: "flex", flexDirection: "column" }}>
      <Document file="./Resume_Tyler_Du.pdf">
        <div
          onClick={toggleZoom}
          className="pdf-container"
          style={{
            cursor: "zoom-in", // Show zoom-in cursor when not zoomed
            transform: isZoomed ? "scale(1.5)" : "scale(1)", // Adjust scale factor
            transition: "transform 0.3s ease",
          }}
        >
          <Page pageNumber={1} renderTextLayer={false} />
        </div>
      </Document>

      <div
        style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <button style={{}} onClick={handleDownload}>
          Click here to download Resume!
        </button>
      </div>
    </div>
  );
}

export default ResumePage;
