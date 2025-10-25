from django.shortcuts import render
import os, json
from django.conf import settings

CHAPTERS_DIR = os.path.join('reader', 'static', 'chapters')

def home(request):
    json_path = os.path.join(settings.BASE_DIR, 'reader', 'static', 'chapters', 'chapters.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        chapters = json.load(f)

    # Show first 50 by default
    show_all = request.GET.get('all', '0') == '1'
    initial_count = 50
    displayed_chapters = chapters if show_all else chapters[:initial_count]

    context = {
        'chapters': displayed_chapters,
        'total_chapters': len(chapters),
        'show_all': show_all,
        'initial_count': initial_count,
    }
    return render(request, 'reader/home.html', context)



def read_chapter(request, chapter_number):
    chapter_file = os.path.join(CHAPTERS_DIR, f'chap_{chapter_number:02d}.xhtml')
    with open(chapter_file, 'r', encoding='utf-8') as f:
        content = f.read()

    return render(request, 'reader/read_chapter.html', {
        'chapter_number': chapter_number,
        'chapter_content': content,
        'chapters': range(1, 1730),
        'prev_chapter': chapter_number - 1 if chapter_number > 1 else None,
        'next_chapter': chapter_number + 1 if chapter_number < 1729 else None,
    })
