# 🔐 Secrets Configuration for Complete Automation

This document explains how to configure the necessary secrets for all automation to work perfectly.

## 🚀 How to Configure

### 1. Access Repository Settings
1. Go to your repository on GitHub
2. Click on **Settings**
3. In the sidebar, click on **Secrets and variables** → **Actions**

### 2. Configure PyPI Token (Required for automatic publishing)

#### 2.1. Create Token on PyPI
1. Access [pypi.org](https://pypi.org)
2. Log into your account
3. Go to **Account settings** → **API tokens**
4. Click **Add API token**
5. Set:
   - **Token name**: `github-actions-codex` (or other name)
   - **Scope**: **Entire account** (for simplicity) or **Specific project** (more secure)
6. Click **Add token**
7. **COPY THE TOKEN** (only appears once!)

#### 2.2. Add to GitHub
1. On GitHub, in **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Configure:
   - **Name**: `PYPI_API_TOKEN`
   - **Secret**: Paste the PyPI token (starts with `pypi-`)
4. Click **Add secret**

### 3. Configure Environment (Recommended)

For greater security, configure an environment called `pypi`:

1. Go to **Settings** → **Environments**
2. Click **New environment**
3. Name: `pypi`
4. Configure:
   - **Required reviewers**: Add yourself (optional)
   - **Deployment branches**: Only `master` and `main`
5. In **Environment secrets**, add:
   - **Name**: `PYPI_API_TOKEN`
   - **Value**: Your PyPI token

## 🔧 Required Secrets

| Secret | Description | Required |
|--------|-------------|----------|
| `PYPI_API_TOKEN` | Token to publish to PyPI | ✅ Yes |
| `GITHUB_TOKEN` | Automatic from GitHub | ✅ Automatic |

## 🧪 Testing Configuration

To test if everything is working:

```bash
# 1. Make a small change
echo "# Test" >> README.md

# 2. Commit and push
git add README.md
git commit -m "test: verify automation"
git push

# 3. Watch in GitHub → Actions
```

## 🚀 Making a Release

Two options:

### Option 1: Automated Script (Recommended)
```bash
make release
```

### Option 2: Manual
```bash
# 1. Update version in pyproject.toml
# 2. Commit
git add pyproject.toml
git commit -m "chore: bump version to 1.2.0"

# 3. Create tag
git tag -a "v1.2.0" -m "Release version 1.2.0"

# 4. Push
git push origin master
git push origin v1.2.0
```

## 🔍 Monitoring

Track workflows at:
- **GitHub → Actions** (to see executions)
- **PyPI → Your projects** (to see publications)
- **GitHub Pages** (to see documentation)

## ❗ Troubleshooting

### Error: "PYPI_API_TOKEN not found"
- Check if the secret is configured correctly
- Confirm the name: `PYPI_API_TOKEN` (case-sensitive)

### Error: "Authentication failed"
- Regenerate the token on PyPI
- Update the secret on GitHub

### Workflow doesn't execute
- Check if you're on `master` or `main` branch
- Confirm that `.github/workflows/*.yml` file is committed

## 🎉 Final Result

With everything configured, **each push to master** automatically:

1. ✅ **Runs tests** on multiple Python versions
2. ✅ **Lints code**
3. ✅ **Generates test coverage**
4. ✅ **Builds Python package**
5. ✅ **Publishes to PyPI** (if version changed)
6. ✅ **Updates documentation** on GitHub Pages
7. ✅ **Creates release** on GitHub (for tags)

**🎯 Zero manual work!**
