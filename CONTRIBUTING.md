# Guide de contribution

## 🌿 Modèle de branches (Git Flow simplifié)

| Branche | Rôle | Protégée |
|---------|------|----------|
| `main` | Production stable | ✅ Oui |
| `develop` | Intégration continue | ✅ Oui |
| `feat/*` | Nouvelle fonctionnalité | ❌ Non |
| `fix/*` | Correction de bug | ❌ Non |
| `hotfix/*` | Correction urgente en prod | ❌ Non |
| `release/*` | Préparation de version | ❌ Non |

## 🔄 Workflow

### Pour une nouvelle fonctionnalité

```bash
# 1. Se placer sur develop à jour
git checkout develop
git pull origin develop

# 2. Créer la branche
git checkout -b feat/<nom-court>

# 3. Développer avec des commits conventionnels
git add .
git commit -m "feat(scope): description"

# 4. Pousser
git push -u origin feat/<nom-court>

# 5. Ouvrir une Pull Request vers develop sur GitHub
