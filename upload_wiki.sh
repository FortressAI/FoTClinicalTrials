#!/bin/bash

# GitHub Wiki Upload Script for Field of Truth Clinical Trials
# This script uploads wiki pages to GitHub using curl

echo "🏥⚛️ Field of Truth Clinical Trials - GitHub Wiki Uploader"
echo "=========================================================="
echo ""

# Check if GitHub token is set
if [ -z "$GITHUB_TOKEN" ]; then
    echo "❌ Error: GITHUB_TOKEN environment variable not set"
    echo ""
    echo "To set up your GitHub token:"
    echo "1. Go to GitHub Settings > Developer settings > Personal access tokens"
    echo "2. Generate a new token with 'repo' and 'write:org' permissions"
    echo "3. Set the token: export GITHUB_TOKEN=your_token_here"
    echo ""
    echo "Or run: export GITHUB_TOKEN=your_token_here"
    echo "Then run this script again."
    exit 1
fi

# Repository information
REPO_OWNER="FortressAI"
REPO_NAME="FoTClinicalTrials"
WIKI_URL="https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/wiki"

echo "🔗 Repository: $REPO_OWNER/$REPO_NAME"
echo "📁 Wiki directory: $(pwd)/wiki"
echo ""

# Function to upload a wiki page
upload_wiki_page() {
    local title="$1"
    local filename="$2"
    local commit_message="$3"
    
    echo "📄 Uploading: $title"
    
    # Read the file content
    if [ ! -f "$filename" ]; then
        echo "❌ File not found: $filename"
        return 1
    fi
    
    # Create JSON payload
    local json_payload=$(cat <<EOF
{
    "title": "$title",
    "body": $(cat "$filename" | jq -Rs .),
    "message": "$commit_message"
}
EOF
)
    
    # Upload the page
    local response=$(curl -s -w "\n%{http_code}" -X POST \
        -H "Authorization: token $GITHUB_TOKEN" \
        -H "Accept: application/vnd.github.v3+json" \
        -H "Content-Type: application/json" \
        -d "$json_payload" \
        "$WIKI_URL/pages")
    
    local http_code=$(echo "$response" | tail -n1)
    local body=$(echo "$response" | head -n -1)
    
    if [ "$http_code" = "201" ]; then
        echo "✅ Successfully uploaded: $title"
        return 0
    else
        echo "❌ Failed to upload $title (HTTP $http_code)"
        echo "Response: $body"
        return 1
    fi
}

# Check if wiki directory exists
if [ ! -d "wiki" ]; then
    echo "❌ Error: 'wiki' directory not found"
    echo "Please run this script from the FoTClinicalTrials repository root"
    exit 1
fi

# Change to wiki directory
cd wiki

echo "🚀 Starting wiki upload process..."
echo ""

# Upload pages in order
success_count=0
total_count=0

# Define pages to upload
declare -a pages=(
    "Home.md:Home:Add Home wiki page"
    "Quick-Start-Guide.md:Quick-Start-Guide:Add Quick Start Guide"
    "Quantum-Substrate.md:Quantum-Substrate:Add Quantum Substrate documentation"
    "Field-of-Truth-Claims.md:Field-of-Truth-Claims:Add Field of Truth Claims documentation"
    "FDA-Compliance.md:FDA-Compliance:Add FDA Compliance documentation"
    "FAQ.md:FAQ:Add FAQ page"
)

# Upload each page
for page_info in "${pages[@]}"; do
    IFS=':' read -r filename title message <<< "$page_info"
    total_count=$((total_count + 1))
    
    if upload_wiki_page "$title" "$filename" "$message"; then
        success_count=$((success_count + 1))
    fi
    
    echo ""  # Add spacing
done

# Summary
echo "=========================================================="
echo "📊 Upload Summary:"
echo "✅ Successful: $success_count/$total_count"
echo "❌ Failed: $((total_count - success_count))/$total_count"
echo ""

if [ $success_count -eq $total_count ]; then
    echo "🎉 All wiki pages uploaded successfully!"
    echo ""
    echo "🔗 View your wiki at: https://github.com/$REPO_OWNER/$REPO_NAME/wiki"
    echo ""
    echo "🎯 Next Steps:"
    echo "1. Visit the wiki URL above"
    echo "2. Review the uploaded pages"
    echo "3. Set up wiki navigation if needed"
    echo "4. Share with your team"
else
    echo "⚠️  Some pages failed to upload. Check the errors above."
    echo ""
    echo "🔧 Troubleshooting:"
    echo "1. Check your GitHub token permissions"
    echo "2. Ensure you have write access to the repository"
    echo "3. Verify the wiki is enabled in repository settings"
fi
