import React, { Component } from 'react';
// Material UI
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
//Imported Components
import AppBarComp from './components/AppBarComp.jsx';
import Home from './components/Home.jsx';

class App extends Component {
  componentDidMount(){
    twttr.widgets.load()
  }
  render() {
    return (
      <MuiThemeProvider>
        <div>
          <AppBarComp />
          <Home />

        </div>
      </MuiThemeProvider>
    );
  }
}

export default App;
