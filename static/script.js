let productsData = [];

fetch("/products")
  .then((res) => res.json())
  .then((data) => {
    productsData = data;
    let container = document.getElementById("products");

    data.forEach((p) => {
      container.innerHTML += `
            <div class="product">
                ${p.name} - ${p.price} Tsh
                <input type="number" id="q${p.id}" value="0" min="0">
            </div>
        `;
    });
  });

function pay() {
  let selected = [];

  productsData.forEach((p) => {
    let qty = document.getElementById("q" + p.id).value;
    if (qty > 0) {
      selected.push({
        price: p.price,
        quantity: parseInt(qty),
      });
    }
  });

  fetch("/total", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(selected),
  })
    .then((res) => res.json())
    .then((data) => {
      document.getElementById("total").innerText =
        "Total Price: " + data.total + " Tsh";
    });
}
