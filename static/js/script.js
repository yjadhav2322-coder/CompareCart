// CompareCart JavaScript

console.log("CompareCart JavaScript loaded");

function filterProducts(category) {

    const products = document.querySelectorAll(".product-card");
    const buttons = document.querySelectorAll(".category-filter button");

    products.forEach(function(product) {

        const productCategory =
            product.querySelector(".product-category").textContent.trim();

        if (category === "all" || productCategory === category) {
            product.style.display = "block";
        } else {
            product.style.display = "none";
        }

    });


    buttons.forEach(function(button) {
        button.classList.remove("active");
    });


    event.target.classList.add("active");
}