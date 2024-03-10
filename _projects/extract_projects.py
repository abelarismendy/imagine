import os
import json
import frontmatter
import re
import datetime

def md_to_json(md_folder, json_file):
    proyectos = []
    for filename in os.listdir(md_folder):
        if filename.endswith('.md'):
            with open(os.path.join(md_folder, filename), 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
                content = post.content
                video_match = re.search(r'<iframe[^>]+src="([^"]+)"', content)
                video = video_match.group(1) if video_match else ""
                imagen = post['image'].split('/')[-1] if 'image' in post else ""
                research_area = post['research_area'] if 'research_area' in post else post['research area'] if 'research area' in post else ""
                last_updated = datetime.datetime.strftime(post['last-updated'], '%Y-%m-%d') if 'last-updated' in post else ""
                link_match = re.search(r'href="([^"]+)"', content)
                link = link_match.group(1) if link_match else post.get('link', "")
                repo_match = re.search(r'https://github.com/[^\s)\n]+', content)
                repo = repo_match.group(0) if repo_match else ""
                proyecto = {
                    "id": len(proyectos) + 1,
                    "nombreProyecto": post['title'],
                    "grupo": "Imagine",
                    "researchArea": research_area,
                    "descripcion": post['description'],
                    "integrantes": post['people'],
                    "foto": imagen,
                    "video": video,
                    "link": link,
                    "repository": repo,
                    "lastUpdated": last_updated
                }
                proyectos.append(proyecto)

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(proyectos, f, ensure_ascii=False, indent=4)

md_to_json('./_projects/', './_data/proyectos.json')
