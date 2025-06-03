import React from "react";
import { Document, Page } from "react-pdf";
import { useState } from "react";
import { pdfjs } from "react-pdf";
import styles from "./ResumePage.module.css";
import NavBar from "../components/NavBar";
import Footer from "../components/Footer";

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
  const [isZoomed, setIsZoomed] = useState(false);

  const toggleZoom = () => {
    setIsZoomed((prevZoom) => !prevZoom);
  };

  return (
    <div>
      <NavBar />
      <button style={{}} onClick={handleDownload}>
        Click here to download Resume!
      </button>

      <div style={{ display: "flex", flexDirection: "column" }}>
        <Document file="./Resume_Tyler_Du.pdf">
          <div
            onClick={toggleZoom}
            className={styles["pdf-container"]}
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
        ></div>
      </div>
      <Footer />
    </div>
  );
}

export default ResumePage;
