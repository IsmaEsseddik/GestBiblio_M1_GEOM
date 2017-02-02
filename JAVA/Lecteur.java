public class Lecteur {
    /**Classe définissant un lecteur, caractérisée par :
      - un numero étudiant
      - un nom
      - un prenom
      - une date de naissance
      - un niveau d'étude
      - un numero de telephone
      - une suspension
      - un commentaire
    **/

    protected Integer num_etudiant;
    protected String nom, prenom, niveau_etude, num_tel, commentaire;
    protected Date date_naissance;
    protected Boolean suspension;
;
    public Lecteur(Integer num_etudiant, String prenom, String niveau_etude, String num_tel, String commentaire, Date date_naissance, Boolean suspension) {
        /**Constructeur de la classe. Chaque attribut va être instancié
            avec une chaine de caractére par défaut**/
        this.num_etudiant = num_etudiant;
        this.prenom = prenom;
        this.niveau_etude = niveau_etude;
        this.num_tel = num_tel;
        this.commentaire = commentaire;
        this.date_naissance = date_naissance;
        this.suspension = suspension;
      }
  }
