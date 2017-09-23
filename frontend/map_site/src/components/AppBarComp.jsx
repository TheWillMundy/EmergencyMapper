import React, { Component } from 'react';
//Material UI Imports
import AppBar from 'material-ui/AppBar'

class AppBarComp extends Component {
  render() {
    return (
      <AppBar
        title="Appbar"
        iconClassNameRight="muidocs-icon-navigation-expand-more"
        />
    );
  }
}

export default AppBarComp;
