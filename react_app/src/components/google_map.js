import React, { Component, PropTypes } from 'react';
import GoogleMapReact from 'google-map-react';


class GoogleMap extends Component {
  static defaultProps = {
    center: { lat: 52.962038, lng: -1.491284 },
    zoom: 6
  }
render() {
    return (
      <div className='google-map'>
        <GoogleMapReact
          defaultCenter={ this.props.center }
          defaultZoom={ this.props.zoom }>
        </GoogleMapReact>
      </div>
    )
  }
}

export default GoogleMap;