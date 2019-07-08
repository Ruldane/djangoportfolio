$(document).ready(

function(){ $('.education-block').hide(); $('.read-more').click(function()
{ $(this).siblings('.education-block').show(); $(this).hide(); $(this).parent().find('.read-less').show(); });
$('.read-less').click(function(){ $(this).siblings('.education-block').hide(); $(this).hide(); $(this).parent().find('.read-more').show(); }); });