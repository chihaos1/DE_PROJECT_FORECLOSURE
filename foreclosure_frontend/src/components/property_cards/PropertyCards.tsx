import { useState, useRef } from "react";
import "./propertycards.css";

const PropertyCards = ({ properties}) => {

  

  const checkClassName = (street_name) => {
    if (!street_name) {
      return "property-card-empty"
    } else {
      return "property-card"
    }
  }

  const checkImage = () => {
    if (properties.photo_one_url === 'N/A') {
      return "https://www.shutterstock.com/shutterstock/photos/2155242945/display_1500/stock-vector-image-coming-soon-no-photo-no-thumbnail-image-available-missing-picture-icon-vector-illustration-2155242945.jpg"
    } else {
      return properties.photo_one_url
    }
  };

  return (
    <div
      className={checkClassName(properties.street_name)}
      onClick={() => {
        if (properties.source == "REA") {
          window.open(properties.property_url, "_blank")
        } else {
          window.open("https://" + properties.property_url, "_blank")
        }
      }
        
        
      }
    >
      <div className="img-container">
        <img src={checkImage()}></img>
      </div>
      <div className="property-container">
        <div className="property-address">
          <h2 className="property-street-name">{properties.street_name}</h2>
          <p>
            {properties.city}, {properties.state} {properties.zip}
          </p>
        </div>
        <div className="property-details-container">
          <div className="property-details">
            <span className="price"></span>
            <p className="property-data">{properties.listed_price}</p>
          </div>
          <div className="property-details">
            <span className="year-built"></span>
            <p className="property-data">{properties.year_built}</p>
          </div>
          <div className="property-details">
            <span className="property-type"></span>
            <p className="property-data">{properties.property_type}</p>
          </div>
          <div className="property-details">
            <span className="square_feet"></span>
            <p className="property-data">{properties.sqft}</p>
          </div>
          <div className="property-details">
            <span className="bedroom"></span>
            <p className="property-data">{properties.bedroom}</p>
          </div>
          <div className="property-details">
            <span className="bathroom"></span>
            <p className="property-data">{properties.bathroom}</p>
          </div>
          
        </div>
      </div>
    </div>
  );
};

export default PropertyCards;
