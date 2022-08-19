import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import PLViewerPage from "./components/pages/PLViewerPage";
import HomePage from "./components/pages/HomePage";

const App: React.FC = () => {
  return (
      <Router>
        <Switch>
          <Route path="/plviewer" component={PLViewerPage} exact />
          <Route path="/" component={HomePage} exact />
        </Switch>
      </Router>
  );
};

export default App;