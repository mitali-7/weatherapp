// const cityname = document.getElementById("cityname");
// const getweather = document.getElementById("getweather");
// const weatheroutput = document.getElementById("weatheroutput")

// getweather.addEventListener("click", () => {
//     const cityname = cityname.value;

//     fetch('http://127.0.0.1:5000/weather', {
//         method: 'POST',
//         body: JSON.stringify({cityname}),
//         headers: {
//             'Content-Type': 'application/json'
//         }
//     })

//     .then(function(response){ 
//         return response.json()})
//         .then(function(data)
//         {
//         weatheroutput.innerHTML = data.weather_info
//       }).catch(error => console.error('Error:', error)); 
// });

// -----------------------------------------------------------

//     .then(response => response.blob())
//     .then(blob => {
//         const weather = 
//         weatheroutput.src = 
//         const videoURL = URL.createObjectURL(blob);
//         videoOutput.src = videoURL;
//     });
// });

// --------------------------------------------------------------

const cityInput = document.getElementById("cityname");
const getWeatherBtn = document.getElementById("getweather");
const weatherOutput = document.getElementById("weatheroutput");

getWeatherBtn.addEventListener("click", () => {
    const cityname = cityInput.value;

    fetch('http://127.0.0.1:5000/weather', {
        method: 'POST',
        body: JSON.stringify({ cityname}),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('City not found');
        }
        return response.json();
    })
    .then(data => {

        console.log(weatherOutput);
        // weatherOutput.innerHTML = `
        //     <h2>Weather Report</h2>
        //     <p>Weather: ${data.weather}</p>
        //     <p>Temperature: ${data.temp} K</p>
        //     <p>Humidity: ${data.humidity}%</p>
        // `;
    })
    .catch(error => {
        weatherOutput.innerHTML = `<p>${error.message}</p>`;
    });
});
