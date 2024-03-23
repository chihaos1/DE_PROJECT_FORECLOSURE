import { useEffect, useRef, useState } from "react";
import axios from "axios";
import { saveAs } from "file-saver";
import "./searchbar.css";

function SearchBar({ props, children }) {
  // const ScrapeExport = async (location: string) => {
  //   const response = await axios.get(
  //     `http://127.0.0.1:9000/foreclosure/scrape/${location}`,
  //     { responseType: "arraybuffer" }
  //   );
  //   let blob = new Blob([response.data], {
  //     type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
  //   });
  //   saveAs(blob, "test.xlsx");
  // };



  // props.current = {
  //   ScrapeExport: ScrapeExport
  // };

  return (
    <>
      <div className="search-bar-container">
        <h1>Search Foreclosure Near You</h1>
        {children}
        <span className="input-content">Enter state, city, or zipcode</span>
      </div>
    </>
  );
}

export default SearchBar;
