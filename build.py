import os

# Use 'games' or 'mygames' depending on your folder name
game_folder = 'games' 

if not os.path.exists(game_folder):
    print(f"Error: Folder {game_folder} not found")
    exit(1)

buttons_html = []

# Using a faster way to scan 10,000+ files
for root, dirs, files in os.walk(game_folder):
    for file in files:
        if file.endswith(".html"):
            # Create the path and clean the name
            path = os.path.join(root, file).replace("\\", "/")
            name = file.replace(".html", "").replace("-", " ").replace("_", " ").title()
            
            # If the file is just 'index.html', use the folder name instead
            if name.lower() == "index":
                name = os.path.basename(root).title()
            
            buttons_html.append(f'<button onclick="loadGame(\'{path}\')">{name}</button>')

# Sort alphabetically so it's easy to find games
buttons_html.sort()

template = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Ultimate Game Stash</title>
    <style>
        body {{ display: flex; height: 100vh; margin: 0; font-family: sans-serif; background: #111; color: white; }}
        #sidebar {{ width: 280px; background: #222; overflow-y: auto; padding: 15px; border-right: 2px solid #444; }}
        #game-container {{ flex-grow: 1; border: none; background: #000; }}
        button {{ display: block; width: 100%; padding: 10px; margin: 5px 0; background: #333; color: white; border: 1px solid #555; cursor: pointer; text-align: left; border-radius: 4px; font-size: 14px; }}
        button:hover {{ background: #444; border-color: #00bcff; }}
        h2 {{ color: #00bcff; margin-top: 0; }}
    </style>
</head>
<body>
    <div id="sidebar">
        <h2>🎮 {len(buttons_html)} Games</h2>
        {"".join(buttons_html)}
    </div>
    <iframe id="game-container" name="game-container" src=""></iframe>
    <script>
        function loadGame(url) {{ document.getElementById('game-container').src = url; }}
    </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(template)
print(f"Success! Indexed {len(buttons_html)} games.")

