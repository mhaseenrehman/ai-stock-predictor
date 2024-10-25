import * as React from 'react';
import { AppBar, Typography} from '@mui/material';

export default function BottomBar() {
    return (
        <>
            <AppBar 
            color="primary"
            sx={{margin: "auto", display: "flex", flex: 1, top: "auto", bottom: 0, justifyContent: "center"}}>
                <Typography>Made by Haseen</Typography>
            </AppBar>
        </>
    );
}
