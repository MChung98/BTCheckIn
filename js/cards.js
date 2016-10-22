var source   = $("#card-template").html();
var template = Handlebars.compile(source);

function card(img, name, inOut) {
    var context  = {img: img, name: name, inOut: inOut};
    $("#card-container").append(template(context));
}

card("res/avatar.jpg", "Kevin Aiken", "Checked in since");
card("res/avatar.jpg", "Nishant Sinha", "hes not here right now");