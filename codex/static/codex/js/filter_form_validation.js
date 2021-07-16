
// Function for formatting filter form data
function filterSubmission(event) {
    event.preventDefault();
    let boxes = $("input[name=min_level]:checked");
    let boxValues = [];
    for (let i = 0; i < boxes.length; i++){
        boxValues.push(boxes[i].value);
        boxes[i].disabled = true;
    }

    // If all boxes are ticked, disable form
    if (boxValues == "1,2,3,4,5" || boxValues == "" ){
        $('#minLevelString').prop('disabled', true);
    } else {
        // Otherwise, add to hidden field as a string
        $('#minLevelString').val(boxValues.toString());
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

$('#filterForm').on('submit', filterSubmission);
