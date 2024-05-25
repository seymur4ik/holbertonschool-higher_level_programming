document.addEventListener('DOMContentLoaded', (event) => {
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      const movies = data.results;
      const listMoviesElement = document.getElementById('list_movies');
      if (listMoviesElement) {
        movies.forEach(movie => {
          const li = document.createElement('li');
          li.textContent = movie.title;
          listMoviesElement.appendChild(li);
        });
      }
    })
    .catch(error => {
      console.error('There was a problem with the fetch operation:', error);
    });
});
