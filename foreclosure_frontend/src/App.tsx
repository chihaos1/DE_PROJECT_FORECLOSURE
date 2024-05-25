import { useRef, useEffect,  useState } from "react";
import { saveAs } from "file-saver";
import axios from "axios";
import InfoToolTip from "./components/tooltip/InfoTooltip";
import AlertToolTip from "./components/tooltip/AlertTooltip";
import SearchBar from "./components/search_bar/SearchBar";
import NavBar from "./components/nav_bar/NavBar";
import PropertyCards from "./components/property_cards/PropertyCards";

function App() {
  const [display, setDisplay] = useState("flex");
  const [isVisible, setIsVisible] = useState("none");
  const [loader, setLoader] = useState("none");
  const [properties, setProperties] = useState([]);

  const infoText =
    "Enter a location in the search bar to scrape and export \
	 forclosed properties.";

  const alertText =
    "Please do not scrape in short successions. The scraper will overload \
	 the server of the source websites and result in bans.";

  let searchBarRef = useRef(null);

  const ScrapeExport = async (location: string) => {
    const response = await axios.get(
      `http://3.87.110.149:8000/foreclosure/scrape/${location}`,
      { responseType: "arraybuffer" }
    );
    let blob = new Blob([response.data], {
      type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    });
    saveAs(blob, "Property_Details.xlsx");
    setLoader("none")
    FetchData()
    setDisplay("none");
    setIsVisible("flex");
  };

  const FetchData = async () => {
    const response = await axios.get("http://3.87.110.149:8000/foreclosure");
    let properties = response.data.map((item) => item);
    console.log(properties)
    if (properties.length % 5 !== 0) {
      for (let index = 0; index < properties.length % 5; index++) {
        properties.push({})
      }
    }
    
    return setProperties(properties);
  };

  return (
    <>
      <div className="search-components" style={{ display: `${display}` }}>
        <div className="tooltips-container">
          <InfoToolTip text={infoText}>
            <i className="gg-info"></i>
          </InfoToolTip>
          <AlertToolTip text={alertText}>
            <i className="gg-bell"></i>
          </AlertToolTip>
        </div>
        <SearchBar props={searchBarRef}>
          <input
            required
            type="text"
            className="input-box"
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                setLoader("flex")
                ScrapeExport(e.target.value)
                e.target.value = ""
              }
            }}
          ></input>
          <span className="loader" style={{ display: `${loader}` }}></span>
        </SearchBar>
        
      </div>

      <div style={{ display: `${isVisible}` }}>
        <NavBar setIsVisible={setIsVisible} setDisplay={setDisplay} properties={properties}></NavBar>
      </div>
      <div
        className="property-cards-components"
        style={{ display: `${isVisible}` }}
      >
        {properties.map((properties) => (
          <PropertyCards properties={properties}></PropertyCards>
        ))}
      </div>
    </>
  );
}

export default App;
