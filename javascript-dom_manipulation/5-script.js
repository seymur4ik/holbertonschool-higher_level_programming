document.addEventListener('DOMContentLoaded', (event) => {
  const button = document.querySelector('#update_header');
  button.addEventListener('click', () => {
    const header = document.querySelector('header');
    if (header) {
      header.textContent = 'New Header!!!';
    }
  });
});
