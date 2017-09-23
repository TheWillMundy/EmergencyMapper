import React, { Component } from 'react';
//Material UI Imports
import AppBar from 'material-ui/AppBar'
import MapToExport from './GoogleMap.jsx'

class Home extends Component {
  render() {
    return (
      <div>
        <MapToExport />
        <h1>Homepage</h1>
      </div>
    );
  }
}

export default Home;
