// AJAX Request to config route to access public Stripe key
$(function () {
  // Check if the checkout button exists in the DOM
  if(document.querySelector("#checkoutButton")) {
    fetch("/premium/config/")
    .then((result) => { return result.json(); })
    .then((data) => {
      // Initialize Stripe.js
      const stripe = Stripe(data.publicKey);
      // Set button listener for obtaining checkout session and redirecting user to stripe
      document.querySelector("#checkoutButton").addEventListener("click", () => {
        // Get Checkout Session ID
        fetch("/premium/checkout/")
        .then((result) => { return result.json(); })
        .then((data) => {
          console.log(data);
            // If route passed error, throw an Error. 
            if (data.error) {
              throw Error("User is already premium");
          } else {
            // Redirect to Stripe Checkout
            return stripe.redirectToCheckout({sessionId: data.sessionId});
          }
        })
        // Log result to console
        .then((res) => {
          console.log(res);
        })
        // Catch error, disable button, confirm user is already premium
        .catch(function(error) {
          document.querySelector("#checkoutButton").disabled = true;
          document.querySelector("#checkoutButton span").innerHTML = "Already premium!";
        });
      });
    });
  }
});