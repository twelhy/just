function Test() {
  return (
    <div>
      <h1>print(Hello world)</h1>
        <input type="checkbox" name="l1" id="l1" />
        <label htmlFor="l1">Error</label> <br />
        <input type="checkbox" name="l2" id="l2" />
        <label htmlFor="l2">Hello world</label> <br />
        <input type="checkbox" name="l3" id="l3" />
        <label htmlFor="l3">Helloworld</label> <br />
        <input type="checkbox" name="l4" id="l4" />
        <label htmlFor="l4">HELLO WORLD</label>
        <script>
            console.log(document.getElementById("l1"));
            if (document.getElementById("l1").value == true) {
                console.log(123)                
            }
        </script>
    </div>
  );
}

export default Test;
