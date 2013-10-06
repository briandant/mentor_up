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

    $("#nav_skills_to_search").selectize({
        persist: false,
        hideSelected: true });

});
