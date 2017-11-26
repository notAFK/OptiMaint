import React, { Component } from 'react';
import TitleMap from '../components/title_map';
import GoogleMap from '../components/google_map';

class DepoMap extends Component {
  render() {
    return (
        <div className="container map">
          <TitleMap />
          <GoogleMap />
        </div>
    );
  }
}

export default DepoMap;