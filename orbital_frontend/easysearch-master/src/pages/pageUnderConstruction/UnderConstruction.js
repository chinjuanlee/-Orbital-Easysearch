import React from "react";
import { Button } from "@material-ui/core";
import { useHistory } from "react-router";
export default function Construction() {
  const history = useHistory();
  return (
    <>
      <p> this page is under construction :)</p>
      <Button
        variant="outlined"
        color="primary"
        aria-describedby="home"
        onClick={() => history.push("/")}
      >
        Back to Login
      </Button>
    </>
  );
}
