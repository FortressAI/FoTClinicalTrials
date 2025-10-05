#!/usr/bin/env python3
"""
GitHub Wiki Upload Script for Field of Truth Clinical Trials
Uploads wiki pages to GitHub using the GitHub API
"""

import os
import json
import requests
import base64
from pathlib import Path

class GitHubWikiUploader:
    def __init__(self, repo_owner="FortressAI", repo_name="FoTClinicalTrials"):
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.base_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
        self.wiki_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/wiki"
        
        # GitHub token - you'll need to set this as an environment variable
        self.token = os.getenv('GITHUB_TOKEN')
        if not self.token:
            print("❌ Error: GITHUB_TOKEN environment variable not set")
            print("Please set your GitHub token: export GITHUB_TOKEN=your_token_here")
            exit(1)
        
        self.headers = {
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github.v3+json',
            'Content-Type': 'application/json'
        }
    
    def upload_wiki_page(self, title, content, commit_message=None):
        """Upload a single wiki page to GitHub"""
        if not commit_message:
            commit_message = f"Add {title} wiki page"
        
        data = {
            'title': title,
            'body': content,
            'message': commit_message
        }
        
        try:
            response = requests.post(
                f"{self.wiki_url}/pages",
                headers=self.headers,
                json=data
            )
            
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
    
    def update_wiki_page(self, title, content, commit_message=None):
        """Update an existing wiki page"""
        if not commit_message:
            commit_message = f"Update {title} wiki page"
        
        # First, get the existing page to get the SHA
        try:
            response = requests.get(
                f"{self.wiki_url}/pages/{title}",
                headers=self.headers
            )
            
            if response.status_code == 200:
                page_data = response.json()
                sha = page_data['sha']
                
                data = {
                    'title': title,
                    'body': content,
                    'message': commit_message,
                    'sha': sha
                }
                
                update_response = requests.put(
                    f"{self.wiki_url}/pages/{title}",
                    headers=self.headers,
                    json=data
                )
                
                if update_response.status_code == 200:
                    print(f"✅ Successfully updated: {title}")
                    return True
                else:
                    print(f"❌ Failed to update {title}: {update_response.status_code}")
                    return False
            else:
                # Page doesn't exist, create it
                return self.upload_wiki_page(title, content, commit_message)
                
        except Exception as e:
            print(f"❌ Error updating {title}: {str(e)}")
            return False
    
    def upload_all_wiki_pages(self, wiki_dir="wiki"):
        """Upload all wiki pages from the wiki directory"""
        wiki_path = Path(wiki_dir)
        
        if not wiki_path.exists():
            print(f"❌ Wiki directory not found: {wiki_dir}")
            return False
        
        success_count = 0
        total_count = 0
        
        # Define the order of pages to upload
        page_order = [
            "Home.md",
            "Quick-Start-Guide.md", 
            "Quantum-Substrate.md",
            "Field-of-Truth-Claims.md",
            "FDA-Compliance.md",
            "FAQ.md"
        ]
        
        print("🚀 Starting GitHub Wiki upload process...")
        print(f"📁 Wiki directory: {wiki_path.absolute()}")
        print(f"🔗 Repository: {self.repo_owner}/{self.repo_name}")
        print()
        
        for filename in page_order:
            file_path = wiki_path / filename
            
            if file_path.exists():
                total_count += 1
                print(f"📄 Processing: {filename}")
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Convert filename to title (remove .md extension)
                    title = filename.replace('.md', '')
                    
                    # Upload the page
                    if self.update_wiki_page(title, content):
                        success_count += 1
                    
                    print()  # Add spacing between pages
                    
                except Exception as e:
                    print(f"❌ Error reading {filename}: {str(e)}")
                    print()
            else:
                print(f"⚠️  File not found: {filename}")
                print()
        
        print("=" * 50)
        print(f"📊 Upload Summary:")
        print(f"✅ Successful: {success_count}/{total_count}")
        print(f"❌ Failed: {total_count - success_count}/{total_count}")
        
        if success_count == total_count:
            print("🎉 All wiki pages uploaded successfully!")
            print(f"🔗 View your wiki at: https://github.com/{self.repo_owner}/{self.repo_name}/wiki")
        else:
            print("⚠️  Some pages failed to upload. Check the errors above.")
        
        return success_count == total_count

def main():
    """Main function to run the wiki upload"""
    print("🏥⚛️ Field of Truth Clinical Trials - GitHub Wiki Uploader")
    print("=" * 60)
    
    # Check if we're in the right directory
    if not os.path.exists("wiki"):
        print("❌ Error: 'wiki' directory not found")
        print("Please run this script from the FoTClinicalTrials repository root")
        return
    
    # Initialize uploader
    uploader = GitHubWikiUploader()
    
    # Upload all wiki pages
    success = uploader.upload_all_wiki_pages()
    
    if success:
        print("\n🎯 Next Steps:")
        print("1. Visit your GitHub repository wiki")
        print("2. Review the uploaded pages")
        print("3. Set up wiki navigation if needed")
        print("4. Share with your team")
    else:
        print("\n🔧 Troubleshooting:")
        print("1. Check your GitHub token permissions")
        print("2. Ensure you have write access to the repository")
        print("3. Verify the wiki is enabled in repository settings")

if __name__ == "__main__":
    main()
