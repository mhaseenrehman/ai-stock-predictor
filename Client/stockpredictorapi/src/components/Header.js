import * as React from 'react';
import { AppBar, Typography} from '@mui/material';

export default function HeaderBar() {
  return (
    <>
      <AppBar sx={{display: 'flex', flexDirection: "row"}}>
        <Typography>Fuck israel</Typography>
      </AppBar>
    </>
  );
}