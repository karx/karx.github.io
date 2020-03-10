// Randomizing alternates on each letter
var list = document.getElementsByTagName("UL")[0]
// Prevent processing last line
for (var i=0; i < list.childElementCount - 1; i++) {
	var textSource = list.getElementsByTagName("LI")[i].innerHTML
	list.getElementsByTagName("LI")[i].innerHTML = mixAlternates (textSource, 3)
}

function mixAlternates (txt, maxAlts) {
  var txtString = ''
  for (var i=0; i < txt.length; i++) {
		var letterVersion = Math.floor((Math.random() * maxAlts))
		txtString += '<span class="aalt-'+letterVersion+'">'+txt[i]+'</span>'
	}
	return txtString
}

warnIfColorFont();