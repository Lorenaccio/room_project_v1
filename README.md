# Room Project V2

Un projet Python qui génère automatiquement une chambre optimisée avec meubles, en utilisant un algorithme génétique.

## 🛠️ Fonctionnalités

- Placement automatique de :
  - ✅ Lit
  - ✅ Armoire
  - ✅ Table
- Optimisation pour éviter :
  - 🚪 Portes
  - 🪟 Fenêtres
  - 🧱 Murs
  - 📦 Autres meubles
- Affichage du **score global**
- Interface graphique simple avec bouton pour déclencher l’optimisation
- Légende graphique intégrée dans l'affichage

---

## ▶️ Installation (Windows 11)

1. **Télécharge et extrait** le fichier `room_project_v2.zip`
2. **Ouvre PowerShell** dans le dossier extrait
3. Installe les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
4. Lance le programme :
   ```bash
   python main.py
   ```

---

## 🖼️ Interface utilisateur

- Une fenêtre `Tkinter` s’ouvre avec un bouton **"Placer automatiquement"**
- Cliquez dessus pour lancer l’algorithme et voir le résultat graphique
- Le score total s’affiche en haut à gauche

---

## 📦 Contenu du projet

| Fichier                  | Rôle                                     |
|--------------------------|------------------------------------------|
| `main.py`                | Lancement de l’interface graphique       |
| `chambre_renderer.py`    | Affichage Pygame avec rendu optimisé     |
| `genetic_furniture.py`   | Algorithme génétique                     |
| `config.py`              | Constantes de couleur, taille, etc.      |
| `requirements.txt`       | Dépendances Python (pygame, shapely)     |
| `README.md`              | Ce fichier                              |

---

## ✅ Exigences

- Python 3.8 ou supérieur
- `pip install pygame shapely`

---

## ✨ À venir (extensions possibles)

- Export PNG / JSON
- Rotation des meubles
- Placement dynamique avec souris
- Ajout d'autres objets (tapis, chaise, etc.)

---

## 👤 Auteur

Projet généré automatiquement avec [ChatGPT + Python + Tkinter + Pygame]
