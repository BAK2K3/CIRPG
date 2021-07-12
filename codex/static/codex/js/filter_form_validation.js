
// Function for formatting filter form data
function filter_submission(event) {
    event.preventDefault();
    let boxes = $("input[name=min_level]:checked");
    let box_values = [];
    for (let i = 0; i < boxes.length; i++){
        box_values.push(boxes[i].value);
        boxes[i].disabled = true;
    }

    // If all boxes are ticked, disable form
    if (box_values == "1,2,3,4,5" || box_values == "" ){
        $('#minLevelString').prop('disabled', true);
    } else {
        // Otherwise, add to hidden field as a string
        $('#minLevelString').val(box_values.toString());
    }

    // Disable Type filter if all selected
    if ($('#typeFilter').val() == "all") {
        $('#typeFilter').prop('disabled', true);
    }

    // Disable Premium Filter if both selected
    if ($('#premiumFilter').val() == "both") {
        $('#premiumFilter').prop('disabled', true);
    }

   // Disable Premium Filter if both selected
   if ($('#direction').val() == "asc") {
        $('#direction').prop('disabled', true);
    }

    // Disable Premium Filter if both selected
    if ($('#sortBy').val() == "default") {
        $('#sortBy').prop('disabled', true);
    }

    $('#filterForm')[0].submit();
}

$('#filterForm').on('submit', filter_submission);