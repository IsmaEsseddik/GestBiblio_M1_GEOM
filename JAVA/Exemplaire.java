class Exemplaire extends InfoDocument {
  /**
  herite de la classe InfoDocument, classe definissant un exemplaire avec :
  - les attributs d'un document
  - un codebar
  - un statut
  - un commentaire
  **/

  protected Integer codebar;
  protected Boolean statut;
  protected String exemp_commentaire;

  public InfoDocument(Integer isbn, String titre, String auteur, String edition_annee, String cote, Integer codebar, Boolean statut, String exemp_commentaire ) {
      /***Constructeur de la classe. Chaque attribut va être instancié
      avec une chaine de caractére par défaut**/
      super(Integer isbn, String titre, String auteur, String edition_annee, String cote);
      this.codebar = codebar;
      this.statut = statut;
      this.exemp_commentaire = exemp_commentaire;
    }

}
