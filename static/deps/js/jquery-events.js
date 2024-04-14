
// When the html document is ready (drawn)
$(document).ready(function () {
    // Take an element from the markup by id - alerts from django
    var notification = $('#notification');

    // And remove after 7 sec.
    if (notification.length > 0) {
        setTimeout(function () {
            notification.alert('close');
        }, 7000);
    }


    //When you click on the cart icon, a pop-up (modal) window opens
    $('#modalButton').click(function () {
        $('#exampleModal').appendTo('body');

        $('#exampleModal').modal('show');
    });


    // Click on the button to close the cart window
    $('#exampleModal .btn-close').click(function () {
        $('#exampleModal').modal('hide');
    });


    // Event handler for radio button selecting delivery method
    $("input[name='requires_delivery']").change(function() {
        var selectedValue = $(this).val();

        // Hiding or displaying the delivery address input
        if (selectedValue === "1") {
            $("#deliveryAddressField").show();
        } else {
            $("#deliveryAddressField").hide();
        }
    });

});