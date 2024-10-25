import * as React from 'react';
import { Button, Grid2} from '@mui/material';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from "recharts"

export default function Stocks() {
    const url = "https://aistockpredictor.onrender.com/";

    const [rawStockData, setRawStockData] = React.useState([]);
    const [stockPrediction, setStockPrediction] = React.useState([]);

    // UI Settings
    const [activatedDot, setActivatedDot] = React.useState(true);

    const getData = async () => {
        console.log("Starting Retrieve Stock Data & Prediction Request")
        await axios.get(url).then(res => {
            // Obtain Response from Django JSON & add dates
            const data = res.data;
            
            // Set up Raw stock Data
            Object.keys(data).forEach(function(key) {
              if (key !== 300) {
                setRawStockData(
                  rawStockData => [...rawStockData, data[key]]
                );
              }
            });

            // Set Stock Price Prediction
            setStockPrediction(stockPrediction => [...stockPrediction, data[300]])

            // Print new stock data
            console.log("New stock data Added");
        });
    }

    const printData = async () => {
      console.log(rawStockData)
      console.log(stockPrediction)
    }

    const activateDotUI = async () => {
      if (activatedDot === false) {
        setActivatedDot(true);
      } else {
        setActivatedDot(false);
      }
      console.log(activatedDot)
    }
    
  return (
    <div>
      <Grid2>
        <Button onClick={getData}>Click for data</Button>
        <Button onClick={printData}>Print Retrieved Stock Data</Button>
        <Button onClick={activateDotUI}>Activate Dot UI</Button>
      </Grid2>
      <ResponsiveContainer width="100%" height={400}>
          <LineChart
            width={500}
            height={300}
            data={rawStockData}
            margin={{
              top: 5,
              right: 30,
              left: 20,
              bottom: 5
            }}
          >
            <CartesianGrid strokeDasharray="3 3"/>
            <XAxis dataKey="date"/>
            <YAxis type="number" domain={["auto", "auto"]}/>
            <Tooltip/>
            <Legend/>
            <Line type="monotone" dataKey="close" stroke="#8884d8" activeDot={{r: 8}} dot={activatedDot}/>
            <Line type="monotone" dataKey="close2" stroke="red" dot={activatedDot} /> */
          </LineChart>
        </ResponsiveContainer>
    </div>
  );
}