#!/usr/bin/env python3
"""
Simple GitHub Wiki Upload Script
Handles JSON escaping and uploads wiki pages to GitHub
"""

import os
import json
import requests
import sys

def upload_wiki_page(title, content, token, repo_owner="FortressAI", repo_name="FoTClinicalTrials"):
    """Upload a single wiki page to GitHub"""
    
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/wiki/pages"
    
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
        'Content-Type': 'application/json'
    }
    
    data = {
        'title': title,
        'body': content,
        'message': f'Add {title} wiki page'
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 201:
            print(f"✅ Successfully uploaded: {title}")
            return True
        else:
            print(f"❌ Failed to upload {title}: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error uploading {title}: {str(e)}")
        return False

def main():
    print("🏥⚛️ Field of Truth Clinical Trials - Simple Wiki Uploader")
    print("=" * 60)
    
    # Check for GitHub token
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        print("❌ Error: GITHUB_TOKEN environment variable not set")
        print("\nTo set up your GitHub token:")
        print("1. Go to https://github.com/settings/tokens")
        print("2. Generate a new token with 'repo' permissions")
        print("3. Run: export GITHUB_TOKEN=your_token_here")
        print("4. Run this script again")
        return False
    
    # Check if wiki directory exists
    if not os.path.exists('wiki'):
        print("❌ Error: 'wiki' directory not found")
        print("Please run this script from the FoTClinicalTrials repository root")
        return False
    
    # Define pages to upload
    pages = [
        ("Home", "wiki/Home.md"),
        ("Quick-Start-Guide", "wiki/Quick-Start-Guide.md"),
        ("Quantum-Substrate", "wiki/Quantum-Substrate.md"),
        ("Field-of-Truth-Claims", "wiki/Field-of-Truth-Claims.md"),
        ("FDA-Compliance", "wiki/FDA-Compliance.md"),
        ("FAQ", "wiki/FAQ.md")
    ]
    
    print(f"🔗 Repository: FortressAI/FoTClinicalTrials")
    print(f"📁 Wiki directory: {os.path.abspath('wiki')}")
    print()
    
    success_count = 0
    total_count = len(pages)
    
    for title, filename in pages:
        print(f"📄 Processing: {title}")
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if upload_wiki_page(title, content, token):
                success_count += 1
            
            print()  # Add spacing
            
        except Exception as e:
            print(f"❌ Error reading {filename}: {str(e)}")
            print()
    
    print("=" * 50)
    print(f"📊 Upload Summary:")
    print(f"✅ Successful: {success_count}/{total_count}")
    print(f"❌ Failed: {total_count - success_count}/{total_count}")
    
    if success_count == total_count:
        print("\n🎉 All wiki pages uploaded successfully!")
        print(f"🔗 View your wiki at: https://github.com/FortressAI/FoTClinicalTrials/wiki")
    else:
        print(f"\n⚠️  {total_count - success_count} pages failed to upload.")
        print("Check the errors above and try again.")
    
    return success_count == total_count

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
