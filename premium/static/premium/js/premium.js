// AJAX Request to config route to access public Stripe key
$(function () {
    fetch("/premium/config/")
    .then((result) => { return result.json(); })
    .then((data) => {
      // Initialize Stripe.js
      const stripe = Stripe(data.publicKey);
    });
});

