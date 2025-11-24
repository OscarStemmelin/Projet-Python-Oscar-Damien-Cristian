from dataclasses import dataclass
from typing import List, Literal


@dataclass
class Livre :
    id : str
    titre : str
    auteur : str
    status : Literal["Disponible", "Emprunté"]

@dataclass
class Utilisateur :
    id : str
    nom : str
    livres_empruntes : List[str]