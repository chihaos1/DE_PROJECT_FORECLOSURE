import React, { useState } from "react";
import "./tooltip.css";

const AlertTooltip = ({ text, children }) => {
  const [isVisible, setIsVisible] = useState(false);

  return (
    <div
      className="alert-tooltip-container"
      onMouseEnter={() => setIsVisible(true)}
      onMouseLeave={() => setIsVisible(false)}
    >
      {children}
      {isVisible && <div className="alert-tooltip">{text}</div>}
    </div>
  );
};

export default AlertTooltip;
