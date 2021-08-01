import {
  AppBar,
  Button,
  Toolbar,
  Typography,
  Menu,
  MenuItem,
  makeStyles,
  IconButton,
} from "@material-ui/core";

import HomeIcon from "@material-ui/icons/Home";
import HistoryIcon from "@material-ui/icons/History";
import BookmarkIcon from "@material-ui/icons/Bookmark";
import PersonIcon from "@material-ui/icons/Person";
import FastfoodIcon from "@material-ui/icons/Fastfood";

import React, { useState, useEffect } from "react";
import { useHistory, withRouter } from "react-router-dom";

import { useAuth } from "../../context/AuthContext";
import { auth } from "../../config/firebase";
const useStyles = makeStyles({
  title: {
    flexGrow: "1",
  },
});
function AppShell() {
  const [width, setWidth] = useState(window.innerWidth);
  const breakpoint = 500;

  const classes = useStyles();
  const history = useHistory();
  const [anchorEl, setAnchorEl] = useState(null);
  const { currentUser } = useAuth();
  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const handleSignout = () => {
    auth.signOut();
    history.push("/");
    handleClose();
  };

  useEffect(() => {
    const handleWindowResize = () => setWidth(window.innerWidth);
    window.addEventListener("resize", handleWindowResize);

    return () => window.removeEventListener("resize", handleWindowResize);
  }, []);
  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h5" className={classes.title}>
          EasySearch
        </Typography>

        {currentUser ? (
          <>
            {width < breakpoint ? (
              <>
                <IconButton color="inherit" onClick={() => history.push("/")}>
                  <HomeIcon />
                </IconButton>
                <IconButton
                  color="inherit"
                  onClick={() => history.push("/food")}
                >
                  <FastfoodIcon />
                </IconButton>
                <IconButton
                  color="inherit"
                  aria-describedby="search-history"
                  onClick={() => history.push("/history")}
                >
                  <HistoryIcon />
                </IconButton>
                <IconButton
                  color="inherit"
                  aria-describedby="search-history"
                  onClick={() => history.push("/wishlist")}
                >
                  <BookmarkIcon />
                </IconButton>
                <IconButton
                  color="inherit"
                  aria-controls="simple-menu"
                  aria-haspopup="true"
                  onClick={handleClick}
                >
                  <PersonIcon />
                </IconButton>
              </>
            ) : (
              <>
                <Button
                  color="inherit"
                  aria-describedby="home"
                  onClick={() => history.push("/")}
                >
                  home
                </Button>
                <Button
                  color="inherit"
                  aria-describedby="home"
                  onClick={() => history.push("/food")}
                >
                  food
                </Button>
                <Button
                  color="inherit"
                  aria-describedby="search-history"
                  onClick={() => history.push("/history")}
                >
                  history
                </Button>
                <Button
                  color="inherit"
                  aria-describedby="wishlist"
                  onClick={() => history.push("/wishlist")}
                >
                  wishlist
                </Button>
                <Button
                  color="inherit"
                  aria-controls="simple-menu"
                  aria-haspopup="true"
                  onClick={handleClick}
                >
                  User
                </Button>
              </>
            )}
            <Menu
              id="simple-menu"
              anchorEl={anchorEl}
              keepMounted
              open={Boolean(anchorEl)}
              onClose={handleClose}
            >
              <MenuItem onClick={handleSignout}>Logout</MenuItem>
            </Menu>
          </>
        ) : null}
      </Toolbar>
    </AppBar>
  );
}

export default withRouter(AppShell);
