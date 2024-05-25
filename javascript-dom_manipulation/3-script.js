document.addEventListener('DOMContentLoaded', (event) => {
  const button = document.querySelector('#toggle_header');
  button.addEventListener('click', () => {
    const header = document.querySelector('header');
    if (header) {
      if (header.classList.contains('red')) {
        header.classList.remove('red');
        header.classList.add('green');
      } else {
        header.classList.remove('green');
        header.classList.add('red');
      }
    }
  });
});
