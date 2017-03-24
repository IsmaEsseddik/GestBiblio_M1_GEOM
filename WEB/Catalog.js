//------------------------------banniere-------------------------------------------

/*
var banniere = document.getElementById('banniere');
var texte = banniere.firstElementChild;
var tailleTexte = banniere.scrollWidth;

function defile(){

  var pos = texte.style.marginLeft.replace('px','');
  pos -= 5;
  if(pos < -tailleTexte){
            pos = 200;
       }
  texte.style.marginLeft = pos+"px";
  window.setTimeout(function(){ defile(); }, 100);

}

defile();

*/



/*
Rechercher un document


*/

var txtbienvenue = "Bienvenue sur le catalogue en ligne de notre fond documentaire"
var txtrecherche = "Entrez vos critères de recherche dans les champs ci-dessous"
var nb_result = 0
