# 🚀 Manual GitHub Wiki Upload Process

## 📋 **Step-by-Step Instructions**

### **Step 1: Create GitHub Personal Access Token**

1. **Go to GitHub Settings**:
   - Visit: https://github.com/settings/tokens
   - Click "Developer settings" → "Personal access tokens" → "Tokens (classic)"

2. **Generate New Token**:
   - Click "Generate new token" → "Generate new token (classic)"
   - Set expiration: 90 days (recommended)
   - Add note: "FoTClinicalTrials Wiki Upload"

3. **Select Scopes**:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `write:org` (Write org and team membership)

4. **Generate and Copy Token**:
   - Click "Generate token"
   - **IMPORTANT**: Copy the token immediately (you won't see it again)

### **Step 2: Set Environment Variable**

```bash
export GITHUB_TOKEN=your_token_here
```

### **Step 3: Upload Wiki Pages**

I'll create individual curl commands for each page. Run these one by one:

#### **Upload Home Page**
```bash
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
  "title": "Home",
  "body": "$(cat wiki/Home.md | sed 's/"/\\"/g' | tr '\n' '\\n')",
  "message": "Add Home wiki page"
}
EOF
https://api.github.com/repos/FortressAI/FoTClinicalTrials/wiki/pages
```

#### **Upload Quick Start Guide**
```bash
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
  "title": "Quick-Start-Guide",
  "body": "$(cat wiki/Quick-Start-Guide.md | sed 's/"/\\"/g' | tr '\n' '\\n')",
  "message": "Add Quick Start Guide"
}
EOF
https://api.github.com/repos/FortressAI/FoTClinicalTrials/wiki/pages
```

#### **Upload Quantum Substrate**
```bash
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
  "title": "Quantum-Substrate",
  "body": "$(cat wiki/Quantum-Substrate.md | sed 's/"/\\"/g' | tr '\n' '\\n')",
  "message": "Add Quantum Substrate documentation"
}
EOF
https://api.github.com/repos/FortressAI/FoTClinicalTrials/wiki/pages
```

#### **Upload Field of Truth Claims**
```bash
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
  "title": "Field-of-Truth-Claims",
  "body": "$(cat wiki/Field-of-Truth-Claims.md | sed 's/"/\\"/g' | tr '\n' '\\n')",
  "message": "Add Field of Truth Claims documentation"
}
EOF
https://api.github.com/repos/FortressAI/FoTClinicalTrials/wiki/pages
```

#### **Upload FDA Compliance**
```bash
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
  "title": "FDA-Compliance",
  "body": "$(cat wiki/FDA-Compliance.md | sed 's/"/\\"/g' | tr '\n' '\\n')",
  "message": "Add FDA Compliance documentation"
}
EOF
https://api.github.com/repos/FortressAI/FoTClinicalTrials/wiki/pages
```

#### **Upload FAQ**
```bash
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Content-Type: application/json" \
  -d @- <<EOF
{
  "title": "FAQ",
  "body": "$(cat wiki/FAQ.md | sed 's/"/\\"/g' | tr '\n' '\\n')",
  "message": "Add FAQ page"
}
EOF
https://api.github.com/repos/FortressAI/FoTClinicalTrials/wiki/pages
```

### **Step 4: Verify Upload**

After running all the commands above, check:

1. **Visit Wiki**: https://github.com/FortressAI/FoTClinicalTrials/wiki
2. **Check Pages**: You should see all 6 pages listed
3. **Test Navigation**: Click through the pages to ensure they work

### **Alternative: Use GitHub Web Interface**

If the API approach doesn't work, you can manually create the wiki pages:

1. **Go to Wiki**: https://github.com/FortressAI/FoTClinicalTrials/wiki
2. **Click "Create the first page"**
3. **Copy content from each file**:
   - Copy content from `wiki/Home.md`
   - Paste into the wiki editor
   - Save as "Home"
4. **Repeat for each page**:
   - Quick-Start-Guide
   - Quantum-Substrate
   - Field-of-Truth-Claims
   - FDA-Compliance
   - FAQ

### **Troubleshooting**

#### **If you get 401 Unauthorized**:
- Check if token is set: `echo $GITHUB_TOKEN`
- Verify token has correct permissions
- Ensure token hasn't expired

#### **If you get 403 Forbidden**:
- Check repository permissions
- Ensure wiki is enabled in repository settings
- Verify organization permissions

#### **If you get 422 Unprocessable Entity**:
- Check JSON formatting
- Verify file content is valid
- Ensure title doesn't contain special characters

### **Expected Results**

After successful upload:
- ✅ All 6 wiki pages visible at https://github.com/FortressAI/FoTClinicalTrials/wiki
- ✅ Professional documentation structure
- ✅ Complete navigation between pages
- ✅ Searchable content
- ✅ Community-accessible documentation

---

**🚀 Manual Wiki Upload - Get Your Documentation Live**
**📚 Step-by-Step Process | 🔗 GitHub API | 🎯 Production Ready**
