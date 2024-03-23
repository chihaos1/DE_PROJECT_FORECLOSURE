import React, { useState } from "react";
import "./tooltip.css";

const tooltip = ({ text, children }) => {
  const [isVisible, setIsVisible] = useState(false);

  return (
    <div
      className="info-tooltip-container"
      onMouseEnter={() => setIsVisible(true)}
      onMouseLeave={() => setIsVisible(false)}
    >
      {children}
      {isVisible &&  <div className="info-tooltip">{text}</div>}
    </div>
  );
};

export default tooltip;
