const apiKey = '32e830892433c4222bac617875a44ee3'; // Replace with your API key from OpenWeatherMap

document.getElementById('getWeather').addEventListener('click', () => {
    const city = document.getElementById('city').value;
    if (city) {
        fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`)
            .then(response => response.json())
            .then(data => {
                const weatherInfo = `
                    <p><strong>City:</strong> ${data.name}</p>
                    <p><strong>Temperature:</strong> ${data.main.temp}°C</p>
                    <p><strong>Condition:</strong> ${data.weather[0].description}</p>
                `;
                document.getElementById('weatherInfo').innerHTML = weatherInfo;
            })
            .catch(() => {
                document.getElementById('weatherInfo').innerHTML = '<p>City not found!</p>';
            });
    } else {
        alert('Please enter a city name!');
    }
});
