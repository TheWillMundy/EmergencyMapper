import React, { Component } from 'react';
//Material UI Imports
import AppBar from 'material-ui/AppBar'
import GoogleHeatMap from './GoogleMapHeat.jsx'
import MapWithAMarkerClusterer from './GoogleMapCluster'

class Home extends Component {
  render() {
    return (
      <div>
        <MapWithAMarkerClusterer />
        <h1>Homepage</h1>
      </div>
    );
  }
}

export default Home;
