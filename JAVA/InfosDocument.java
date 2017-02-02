public class InfoDocument {
    /**Classe définissant un document caractérisée par :
    - son isbn
    - son titre
    - son auteur
    - son edition(&année)
    - sa cote
    **/

    protected Integer isbn;
    protected String titre, auteur, edition_annee, cote;
    public InfoDocument(Integer isbn, String titre, String auteur, String edition_annee, String cote) {
        /**Constructeur de la classe. Chaque attribut va être instancié
        avec la var Null par défaut**/
        this.isbn = isbn;
        this.titre = titre;
        this.auteur = auteur;
        this.edition_annee = edition_annee;
        this.cote = cote;
      }
  }
