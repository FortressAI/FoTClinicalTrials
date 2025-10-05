# 🚀 GitHub Wiki Upload Guide

## 📋 **Overview**

This guide explains how to upload the comprehensive wiki documentation to the GitHub repository using the GitHub API.

## 🔑 **Step 1: Set Up GitHub Token**

### **Create Personal Access Token**
1. Go to [GitHub Settings](https://github.com/settings/tokens)
2. Click "Developer settings" → "Personal access tokens" → "Tokens (classic)"
3. Click "Generate new token" → "Generate new token (classic)"
4. Set expiration (recommend 90 days)
5. Select scopes:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `write:org` (Write org and team membership)
6. Click "Generate token"
7. **Copy the token immediately** (you won't see it again)

### **Set Environment Variable**
```bash
export GITHUB_TOKEN=your_token_here
```

## 🚀 **Step 2: Upload Wiki Pages**

### **Option A: Using the Shell Script (Recommended)**
```bash
# Make sure you're in the repository root
cd /Users/richardgillespie/Documents/FoTClinicalTrials

# Run the upload script
./upload_wiki.sh
```

### **Option B: Using Python Script**
```bash
# Install required packages
pip install requests

# Run the Python script
python upload_wiki.py
```

### **Option C: Manual Upload with curl**

#### **Upload Home Page**
```bash
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Home",
    "body": "'"$(cat wiki/Home.md | sed 's/"/\\"/g' | tr '\n' '\\n')"'",
    "message": "Add Home wiki page"
  }' \
  https://api.github.com/repos/FortressAI/FoTClinicalTrials/wiki/pages
```

#### **Upload Quick Start Guide**
```bash
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Quick-Start-Guide",
    "body": "'"$(cat wiki/Quick-Start-Guide.md | sed 's/"/\\"/g' | tr '\n' '\\n')"'",
    "message": "Add Quick Start Guide"
  }' \
  https://api.github.com/repos/FortressAI/FoTClinicalTrials/wiki/pages
```

## 📊 **Step 3: Verify Upload**

### **Check Wiki Status**
```bash
curl -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/FortressAI/FoTClinicalTrials/wiki/pages
```

### **Visit Wiki**
Go to: https://github.com/FortressAI/FoTClinicalTrials/wiki

## 🔧 **Troubleshooting**

### **Common Issues**

#### **401 Unauthorized**
- Check if GitHub token is set: `echo $GITHUB_TOKEN`
- Verify token has correct permissions
- Ensure token hasn't expired

#### **403 Forbidden**
- Check repository permissions
- Ensure wiki is enabled in repository settings
- Verify organization permissions

#### **404 Not Found**
- Verify repository exists
- Check repository name spelling
- Ensure you have access to the repository

#### **422 Unprocessable Entity**
- Check JSON formatting
- Verify file content is valid
- Ensure title doesn't contain special characters

### **Debug Commands**
```bash
# Test API access
curl -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/user

# Check repository access
curl -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/FortressAI/FoTClinicalTrials

# List existing wiki pages
curl -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/FortressAI/FoTClinicalTrials/wiki/pages
```

## 📚 **Wiki Pages to Upload**

The following pages will be uploaded:

1. **Home** - Main wiki landing page with navigation
2. **Quick-Start-Guide** - 5-minute setup guide
3. **Quantum-Substrate** - Quantum mechanics in clinical trials
4. **Field-of-Truth-Claims** - FoT claims system documentation
5. **FDA-Compliance** - FDA regulatory compliance
6. **FAQ** - Frequently asked questions

## 🎯 **Expected Results**

After successful upload:
- ✅ All 6 wiki pages uploaded
- ✅ Wiki accessible at https://github.com/FortressAI/FoTClinicalTrials/wiki
- ✅ Navigation working between pages
- ✅ Content properly formatted
- ✅ Links functional

## 🔄 **Updating Wiki Pages**

To update existing pages, use the same process but with PUT requests:

```bash
# Get existing page SHA first
curl -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/FortressAI/FoTClinicalTrials/wiki/pages/Home

# Update page with SHA
curl -X PUT \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Home",
    "body": "'"$(cat wiki/Home.md | sed 's/"/\\"/g' | tr '\n' '\\n')"'",
    "message": "Update Home page",
    "sha": "existing_sha_here"
  }' \
  https://api.github.com/repos/FortressAI/FoTClinicalTrials/wiki/pages/Home
```

## 📞 **Support**

If you encounter issues:
1. Check the troubleshooting section above
2. Verify your GitHub token permissions
3. Ensure repository access
4. Check GitHub API status
5. Review error messages for specific guidance

---

**🚀 GitHub Wiki Upload Guide - Get Your Documentation Live**
**📚 Comprehensive Documentation | 🔗 API Integration | 🎯 Production Ready**
