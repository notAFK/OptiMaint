import React from 'react';
import { Link } from 'react-router-dom';

const TitleMap = () => {
  return (
    <div className="title">
      <Link to="/" className="btn btn-primary pull-xs-right map-button">Services</Link>
      <h1>OptiMaint</h1>
    </div>
  );
}

export default TitleMap;