/* Project specific Javascript goes here. */

// Skill fields for user form
$(document).ready(function() { 
    $("#id_skills_to_learn").selectize({
        persist: false,
        hideSelected: true });

    $("#id_skills_to_teach").selectize({
        persist: false,
        hideSelected: true });

    $("#nav_skills_to_search").selectize({
        persist: false,
        hideSelected: true });

    $("#id_locations_to_search").selectize({
        persist: false,
        hideSelected: true });

    var $skills_to_search = $("#id_skills_to_search").selectize({
        persist: false,
        hideSelected: true });

    // Use selectize API to repopulate those fields
   
   if ( $.isEmptyObject(window.previouslySelectedSkills) == false ) {
        // Select the element(s) to write to
        var skills_instance = $skills_to_search[0].selectize;

         for ( skill in window.previouslySelectedSkills )  {
             skills_instance.addItem(skill);
         };
   }
})