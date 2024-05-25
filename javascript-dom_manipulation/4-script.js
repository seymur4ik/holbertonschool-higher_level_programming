document.addEventListener('DOMContentLoaded', (event) => {
  const button = document.querySelector('#add_item');
  button.addEventListener('click', () => {
    const ul = document.querySelector('.my_list');
    if (ul) {
      const li = document.createElement('li');
      li.textContent = 'Item';
      ul.appendChild(li);
    }
  });
});
