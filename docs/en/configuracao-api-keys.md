# 🔑 API Keys Configuration for Complete Integration

This document explains how to configure the necessary API keys for all Codex CLI integrations to work perfectly.

## 🚀 How to Configure

### 1. Google API Key (For Google Search)

#### 1.1. Create Google Cloud Project
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Sign in with your Google account
3. Click **New Project** or select an existing project
4. Give your project a name (e.g., "codex-cli-integrations")

#### 1.2. Enable Custom Search API
1. In the dashboard, go to **APIs & Services** → **Library**
2. Search for "Custom Search API"
3. Click **Enable**

#### 1.3. Create Credentials
1. Go to **APIs & Services** → **Credentials**
2. Click **+ Create Credentials** → **API Key**
3. Copy the generated key

#### 1.4. Create Search Engine
1. Go to [Google Custom Search Engine](https://cse.google.com/)
2. Click **Add**
3. In "Sites to search", enter: `*` (to search the entire web)
4. Click **Create**
5. Copy the **Search engine ID**

#### 1.5. Configure Environment Variables
```bash
export GOOGLE_API_KEY="your_api_key_here"
export GOOGLE_SEARCH_API_KEY="your_api_key_here"  # Same key
export GOOGLE_SEARCH_CX="your_search_engine_id_here"
```

### 2. WolframAlpha APP ID (For Mathematical/Scientific Queries)

#### 2.1. Create Account
1. Go to [WolframAlpha Developer Portal](https://products.wolframalpha.com/api/)
2. Click **Get Started for Free**
3. Create a free account

#### 2.2. Get APP ID
1. After login, go to **My Apps**
2. Click **Get an AppID**
3. Choose the free plan (2000 queries/month)
4. Fill in the application details:
   - **Application name**: "Codex CLI"
   - **Description**: "Personal AI assistant with mathematical capabilities"
5. Copy the generated **AppID**

#### 2.3. Configure Environment Variable
```bash
export WOLFRAMALPHA_APPID="your_app_id_here"
```

### 3. GitHub Token (Optional - For Higher API Limits)

#### 3.1. Create Personal Access Token
1. Go to [GitHub Settings](https://github.com/settings/tokens)
2. Click **Generate new token** → **Generate new token (classic)**
3. Configure:
   - **Note**: "Codex CLI Integration"
   - **Expiration**: Choose desired period
   - **Scopes**: Select only **public_repo** (for public repositories)
4. Click **Generate token**
5. Copy the generated token (you'll only see it once!)

#### 3.2. Configure Environment Variable
```bash
export GITHUB_TOKEN="your_token_here"
```

## 🔧 Permanent Configuration

### Linux/macOS
Add the variables to your `~/.bashrc` or `~/.zshrc` file:

```bash
# Codex CLI API Keys
export GOOGLE_API_KEY="your_key_here"
export GOOGLE_SEARCH_API_KEY="your_key_here"
export GOOGLE_SEARCH_CX="your_cx_here"
export WOLFRAMALPHA_APPID="your_appid_here"
export GITHUB_TOKEN="your_token_here"  # Optional
```

Then execute:
```bash
source ~/.bashrc  # or ~/.zshrc
```

### Windows
Using Command Prompt:
```cmd
setx GOOGLE_API_KEY "your_key_here"
setx GOOGLE_SEARCH_API_KEY "your_key_here"
setx GOOGLE_SEARCH_CX "your_cx_here"
setx WOLFRAMALPHA_APPID "your_appid_here"
setx GITHUB_TOKEN "your_token_here"
```

### Using .env (Development)
Create a `.env` file in the project root:
```env
GOOGLE_API_KEY=your_key_here
GOOGLE_SEARCH_API_KEY=your_key_here
GOOGLE_SEARCH_CX=your_cx_here
WOLFRAMALPHA_APPID=your_appid_here
GITHUB_TOKEN=your_token_here
```

## ✅ Verify Configuration

Run Codex CLI and test each integration:

```bash
# Test Google Search
python -m codex
# Type: "search for Python on Google"

# Test WolframAlpha
# Type: "what is the derivative of x²+3x?"

# Test GitHub
# Type: "find repositories about machine learning"

# Test Wikipedia (no API needed)
# Type: "what is artificial intelligence?"
```

## 📊 Free API Limits

| Service | Free Limit | Limit with Token/Key |
|---------|------------|---------------------|
| **Google Search** | - | 100 searches/day |
| **WolframAlpha** | - | 2000 queries/month |
| **GitHub** | 60 req/hour | 5000 req/hour |
| **Wikipedia** | Unlimited | Unlimited |
| **StackOverflow** | Unlimited | Unlimited |

## 🚨 Security

- ⚠️ **Never** commit API keys to code
- 🔒 Use environment variables or `.env` files
- 🗂️ Add `.env` to `.gitignore`
- 🔄 Rotate keys periodically
- 👥 For team projects, use GitHub Secrets or similar

## 🔍 Troubleshooting

### Error: "API key not found"
- Check if the environment variable is configured correctly
- Run `echo $VARIABLE_NAME` to verify

### Error: "403 Forbidden"
- Your key might be invalid or expired
- Check if you enabled the correct API in Google Cloud

### Error: "Quota exceeded"
- You've reached the free API limit
- Consider upgrading to a paid plan or wait for limit reset

### Error: "Invalid search engine ID"
- Check if you copied the correct CX from Google Custom Search
- The ID should have a format like: `017576662512468239146:omuauf_lfve`
