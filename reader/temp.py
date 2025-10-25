import os

folder = "static/chapters"

for filename in os.listdir(folder):
    if filename.endswith(".xhtml"):
        path = os.path.join(folder, filename)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        text = text.replace('href="style/chapter.css"', 'href="/static/chapters/style/chapter.css"')
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)

print("Fixed all CSS paths!")
