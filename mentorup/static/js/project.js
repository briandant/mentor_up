/* Project specific Javascript goes here. */

// Skill fields for user form
$(document).ready(function() { 
    $("#id_skills_to_learn").selectize({
        persist: false,
        hideSelected: true });

    $("#id_skills_to_teach").selectize({
        persist: false,
        hideSelected: true });

    $("#id_locations_to_search").selectize({
        persist: false,
        hideSelected: true });

    $("#id_skills_to_search").selectize({
        persist: false,
        hideSelected: true });

    $("#id_member_search_form").submit(function(e) {
        // alert("Search coming soon! Goooooo Django Dash!");
        // e.preventDefault();
    })
})

//        $.ajax({
//           url: this.attr('action'),
//           data: $("#id_member_search_form").serialize(), // serializes the form's elements.
//         }).done(function(data) {
//           alert("Done"); // show response from the php script.
//         })
//    })
//               type: "GET",
//               url: url,
