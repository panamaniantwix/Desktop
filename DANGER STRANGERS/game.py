
<button onclick="fetchData()">Get Data</button>
<div id="data"></div>

<script>
  function fetchData() {
    fetch('https://your-api-gateway-endpoint.com/path/to/your/function')
      .then(response => response.json())
      .then(data => {
        const dataDiv = document.getElementById('data');
        dataDiv.textContent = JSON.stringify(data);
      })
      .catch(error => console.error(error));
  }
</script>
