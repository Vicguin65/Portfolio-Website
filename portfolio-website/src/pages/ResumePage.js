import React from "react";
import {Document, Page} from "react-pdf"
import { useState } from "react";
import { pdfjs } from 'react-pdf';
import "react-pdf/dist/esm/Page/TextLayer.css";

pdfjs.GlobalWorkerOptions.workerSrc = new URL(
  'pdfjs-dist/build/pdf.worker.min.mjs',
  import.meta.url,
).toString();

function ResumePage() {
    const [numPages, setNumPages] = useState(1);
    const [pageNumber, setPageNumber] = useState(1);

    function onDocumentLoadSuccess(numPages) {
        setNumPages(numPages);
    }

  return (
    <div>
      <Document file="./Tyler_Du_Resume.pdf" onLoadSuccess={()=>{}}>
        <Page pageNumber={1} renderTextLayer={false}/>
      </Document>
    </div>
  );
}

export default ResumePage;
