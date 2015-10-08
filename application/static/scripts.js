var system;
var subunit;

var HTMLformInput_sn = '<input type="text" name="sn" value="%data%" id="form_sn">';
var HTMLformInput_belongsSn = '<input type="text" name="belongs_sn" value="%data%" id="form_belongs_sn">';

function overlay(sys, sub) {
	system = sys;
	subunit = sub;
	
	HTMLformInput_sn = HTMLformInput_sn.replace("%data%", subunit);
	$("#form_sn").replaceWith(HTMLformInput_sn);
	
	HTMLformInput_belongsSn = HTMLformInput_belongsSn.replace("%data%", system);
	$("#form_belongs_sn").replaceWith(HTMLformInput_belongsSn);
	

	el = document.getElementById("overlay");
	el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
	console.log(system);
	console.log(subunit);
}



function show_full_table() {
	$('.hide__550').toggle();
	var icon0 = "fa-expand";
	var icon1 = "fa-compress";
	var srg = $("#show__all").html();

	if(srg.indexOf(icon1) >= 0){
		srg = srg.replace(icon1, icon0);
		$("#show__all").empty().append(srg);
	}
	else if(srg.indexOf(icon0) >= 0){
		srg = srg.replace(icon0, icon1);
		$("#show__all").empty().append(srg);
	}
}