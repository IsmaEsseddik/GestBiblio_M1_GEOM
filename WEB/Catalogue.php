<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Catalogue GestBiblio</title>
    <link href="https://fonts.googleapis.com/css?family=Gentium+Book+Basic" rel="stylesheet">
    <link type="text/css" rel="stylesheet" href="Catalog.css">
  </head>

  <header >
    <p>Vous etes sur le catalogue en ligne de :</p>
      <h1> Gestbiblio </h1>
  </header>
<!-------------------------------------------------------------------------->
  <body>


    <script type="text/javascript" src="Catalog.js"></script>
  </body>
  <footer>


<!-------------------------------------------------------------------------->
  </footer>
  <?php $timestamp = time();
  $tabtemp = getdate($timestamp);
  $heure = $tabtemp["hours"];
  $minu = $tabtemp["minutes"];
  $joursem = $tabtemp["wday"];
  $jourmois = $tabtemp["mday"];
  $mois = $tabtemp["minutes"];
  $annee = $tabtemp["minutes"];
    ?>

  <div id= "heure">
    <?php echo "<p>Il est : ".$heure." heures et ".$minu." minutes</p>"; ?>
  </div>
  <div id = 'banniere'>
  <p>Plateforme en construction</p>
  </div>
  <div id = "date">
    <?php echo "<p>Nous somme le :". ."</p>" ?>

  </div>
</html>
