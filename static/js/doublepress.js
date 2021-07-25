
 $(document).ready(function () {
    // Button Clickjack prevention 
    const buttons = document.querySelectorAll('.anti-double-click');
    Array.from(buttons).forEach(button => {
        button.addEventListener('click', function(event) {
            if(this.classList.contains('in-progress')) {
                event.preventDefault();
                return false;
            } else {
                this.classList.add("in-progress");
            }
        });
    });
 });
 
 