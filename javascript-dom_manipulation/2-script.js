document.addEventListener('DOMContentLoaded', (event) => {
  const button = document.querySelector('#red_header');
  button.addEventListener('click', () => {
    const header = document.querySelector('header');
    if (header) {
      header.classList.add('red');
    }
  });
});
