import React, { useState, useEffect } from "react";
import { Typography, Grid, makeStyles, Divider } from "@material-ui/core";
import LinkIcon from "@material-ui/icons/Link";

const useStyles = makeStyles({
  sortButton: {
    color: "#212121",
    backgroundColor: "#80d8ff",
  },

  divider: {
    height: "5px",
    backgroundColor: "#212121",
  },

  resultHeader: {
    paddingTop: "5px",
    textAlign: "center",
  },
});

export default function WishlistHeader() {
  const [width, setWidth] = useState(window.innerWidth);
  const lg = 1000;
  const sm = 750;
  const xs = 400;
  useEffect(() => {
    const handleWindowResize = () => setWidth(window.innerWidth);
    window.addEventListener("resize", handleWindowResize);

    return () => window.removeEventListener("resize", handleWindowResize);
  }, []);
  const classes = useStyles();
  return (
    <div>
      <Grid container className={classes.resultHeader}>
        <Grid item xs={width < lg ? false : 1}></Grid>

        <Grid item xs={2}>
          <Typography variant="button" display="block" gutterBottom>
            IMAGE
          </Typography>
        </Grid>

        {width < lg ? (
          <Grid item xs={2}>
            <Typography variant="button" display="block" gutterBottom>
              ITEM
            </Typography>
          </Grid>
        ) : (
          <Grid item xs={3}>
            <Typography variant="button" display="block" gutterBottom>
              ITEM NAME
            </Typography>
          </Grid>
        )}

        <Grid item xs={width < lg ? 2 : 1}>
          <Typography variant="button" display="block" gutterBottom>
            price
          </Typography>
        </Grid>

        <Grid item xs={width < lg ? 2 : 1}>
          <Typography variant="button" display="block" gutterBottom>
            store
          </Typography>
        </Grid>

        {width < sm ? null : (
          <Grid item xs={1}>
            <Typography variant="button" display="block" gutterBottom>
              RATING
            </Typography>
          </Grid>
        )}

        <Grid item xs={width < sm ? 2 : 1}>
          <Typography variant="button" display="block" gutterBottom>
            WISHLIST
          </Typography>
        </Grid>

        <Grid item xs={width < xs ? 2 : 1}>
          {width < lg ? (
            <LinkIcon />
          ) : (
            <Typography variant="button" display="block" gutterBottom>
              link to site
            </Typography>
          )}
        </Grid>
      </Grid>
      <Divider className={classes.divider} />
    </div>
  );
}
