const express = require('express');
const axios = require('axios');

const app = express();
//Example code for Fetch
app.get('/fetch-resources', async (req, res) => {
  try {
    const response = await axios.get('http://localhost:5000/resources', {
      responseType: 'arraybuffer',
    });
    res.setHeader('Content-Type', 'image/png');
    res.send(response.data);
    print("HEllo")
  } catch (error) {
    res.status(500).send('Error fetching chart');
  }
});

app.listen(3000, () => console.log('Express server running on port 3000'));