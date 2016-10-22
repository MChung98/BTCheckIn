var source   = $("#card-template").html();
var template = Handlebars.compile(source);

function card(img, name, front, back) {
    var context  = {img: img, name: name, isIn: name + " last checked in at " + front, lastIn: "Last checked out at " + back};
    $("#center-cards").append(template(context));
}

card("res/KevinAiken.png", "Kevin Aiken", "9:05", "4:20");
card("res/avatar.jpg", "Nishant Sinha", "6:30", "8:20");
