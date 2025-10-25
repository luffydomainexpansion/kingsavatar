import os
from django.shortcuts import render
from django.conf import settings

def read_chapter(request, number):
    chapter_filename = f"chap_{int(number):02d}.xhtml"
    chapter_path = os.path.join(settings.BASE_DIR, 'reader', 'static', 'chapters', chapter_filename)

    if not os.path.exists(chapter_path):
        return render(request, "404.html", {"message": "Chapter not found"})

    with open(chapter_path, encoding="utf-8") as f:
        content = f.read()

    return render(request, "reader/read_chapter.html", {"content": content, "chapter": number})
