import React, { useEffect, useState } from "react";
import {
  BrowserRouter as Router,
  Redirect,
  Route,
  Switch,
} from "react-router-dom";

import AppShell from "./components/AppShell";
import Food from "./pages/pageFood";
import ForgetPassword from "./pages/pageForgetPassword";
import Home from "./pages/pageHome";
import History from "./pages/pageHistory";
import Login from "./pages/pageLogin";
import Signup from "./pages/pageSignup";
import Trending from "./pages/pageTrending";
import Wishlist from "./pages/pageWishlist";
import { auth } from "./config/firebase";
import { AuthProvider } from "./context/AuthContext";

export default function App() {
  const [loggedIn, setLoggedIn] = useState(false);
  useEffect(() => {
    auth.onAuthStateChanged((user) => {
      if (user) {
        setLoggedIn(true);
      } else {
        setLoggedIn(false);
      }
    });
  }, [setLoggedIn]);
  return (
    <div>
      <AuthProvider>
        <Router>
          <AppShell />
          {loggedIn ? (
            <Switch>
              <Route path="/history">
                <History />
              </Route>

              <Route path="/food">
                <Food />
              </Route>

              <Route path="/wishlist">
                <Wishlist />
              </Route>

              <Route path="/trending">
                <Trending />
              </Route>

              <Route exact path="/">
                <Home />
              </Route>
              <Route path="/forget">
                <Redirect to="/" />
              </Route>
            </Switch>
          ) : (
            <Switch>
              <Route path="/signup">
                <Signup />
              </Route>

              <Route path="/forget">
                <ForgetPassword />
              </Route>

              <Route path="/">
                <Login />
              </Route>
            </Switch>
          )}
        </Router>
      </AuthProvider>
    </div>
  );
}
