#!/usr/bin/env python3
import os
import re

def fix_html_files():
    docs_dir = '/Users/hirakawa/heiwadai-manual/docs/manual'
    
    # Map of Japanese filenames to English filenames
    filename_map = {
        'アプリ管理画面 操作マニュアル.html': 'admin-manual.html',
        '①アプリユーザー一覧.html': 'app-user-list.html',
        '②メルマガ配信.html': 'newsletter.html',
        '③アプリログイン時通知.html': 'login-notification.html',
        '＜×＞管理画面ユーザー登録方法.html': 'admin-user-registration.html'
    }
    
    # First, rename all files
    for old_name, new_name in filename_map.items():
        old_path = os.path.join(docs_dir, old_name)
        new_path = os.path.join(docs_dir, new_name)
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            print(f"Renamed: {old_name} -> {new_name}")
    
    # Now fix content in all HTML files
    for filename in os.listdir(docs_dir):
        if filename.endswith('.html'):
            filepath = os.path.join(docs_dir, filename)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Fix navigation links
            content = content.replace('href="../index.html"', 'href="/heiwadai-manual/"')
            content = content.replace('href="%E3%82%A2%E3%83%97%E3%83%AA%E7%AE%A1%E7%90%86%E7%94%BB%E9%9D%A2%20%E6%93%8D%E4%BD%9C%E3%83%9E%E3%83%8B%E3%83%A5%E3%82%A2%E3%83%AB.html"', 'href="/heiwadai-manual/manual/admin-manual.html"')
            content = content.replace('href="%E2%91%A0%E3%82%A2%E3%83%97%E3%83%AA%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC%E4%B8%80%E8%A6%A7.html"', 'href="/heiwadai-manual/manual/app-user-list.html"')
            content = content.replace('href="%E2%91%A1%E3%83%A1%E3%83%AB%E3%83%9E%E3%82%AC%E9%85%8D%E4%BF%A1.html"', 'href="/heiwadai-manual/manual/newsletter.html"')
            content = content.replace('href="%E2%91%A2%E3%82%A2%E3%83%97%E3%83%AA%E3%83%AD%E3%82%B0%E3%82%A4%E3%83%B3%E6%99%82%E9%80%9A%E7%9F%A5.html"', 'href="/heiwadai-manual/manual/login-notification.html"')
            
            # Fix broken image syntax - convert !<a href="..."> to <img src="...">
            # Pattern: !<a href="path">text</a>
            image_pattern = r'!<a href="([^"]+)">([^<]+)</a>'
            
            def fix_image(match):
                path = match.group(1)
                alt_text = match.group(2)
                # Convert relative paths to absolute paths
                if not path.startswith('/'):
                    path = f"/heiwadai-manual/manual/{path}"
                return f'<img src="{path}" alt="{alt_text}">'
            
            content = re.sub(image_pattern, fix_image, content)
            
            # Write back the fixed content
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Fixed: {filename}")

def fix_index_html():
    index_path = '/Users/hirakawa/heiwadai-manual/docs/index.html'
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update all the links to use the new English paths
    replacements = [
        ('../manual/アプリ管理画面%20操作マニュアル.html', 'manual/admin-manual.html'),
        ('../manual/①アプリユーザー一覧.html', 'manual/app-user-list.html'),
        ('../manual/②メルマガ配信.html', 'manual/newsletter.html'),
        ('../manual/③アプリログイン時通知.html', 'manual/login-notification.html'),
        ('../manual/＜×＞管理画面ユーザー登録方法.html', 'manual/admin-user-registration.html')
    ]
    
    for old, new in replacements:
        content = content.replace(f'href="{old}"', f'href="{new}"')
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed index.html")

if __name__ == "__main__":
    fix_html_files()
    fix_index_html()
    print("\nAll files have been fixed!")