import { useEffect } from "react";
import "./navbar.css";

const NavBar = ({ setIsVisible, setDisplay, properties }) => {
  return (
    <div className="navbar">
      <span
        id="backarrow"
        onClick={() => {
          setIsVisible("none");
          setDisplay("flex");
        }}
      ></span>
      <div className="navbar-text">
        <h2>
          We found a total of <p id="property-count">{properties.length}</p>{" "}
          properties
        </h2>
      </div>
    </div>
  );
};

export default NavBar;
