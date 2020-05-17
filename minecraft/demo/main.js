let g_file;
  const fileSelector = document.getElementById('file-selector');
  fileSelector.addEventListener('change', (event) => {
    const fileList = event.target.files;
    console.log(fileList);
    g_file = event.target.files[0];
  });


  function kaaro_update() {
    g_file = fileSelector.files[0];
  }