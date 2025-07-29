#!/usr/bin/env python3
"""
Script to generate individual publication pages for Dr. Abolfazl Zaraki's website.
"""

import os
import re
from pathlib import Path

# Publication data extracted from CV
publications = {
    "journal_articles": [
        {
            "title": "Towards AI-Powered Applications: The Development of a Personalised LLM for HRI and HCI",
            "authors": ["K. Ghamati", "M. Dehkord", "A. Zaraki"],
            "venue": "Sensors Journal",
            "year": "2025",
            "volume": "25",
            "folder": "ai-powered-applications-llm-hri",
            "keywords": ["Large Language Models", "Human-Robot Interaction", "Human-Computer Interaction", "Personalisation", "Artificial Intelligence"]
        },
        {
            "title": "Learning to Gaze: Bio-Inspired Attention Adaptation for Social Robots",
            "authors": ["K. Ghamati", "A. Zaraki"],
            "venue": "Scientific Reports (Nature Journal)",
            "year": "2025",
            "folder": "learning-to-gaze-bio-inspired-attention",
            "keywords": ["Bio-inspired Systems", "Attention Mechanisms", "Social Robotics", "Gaze Control", "Human-Robot Interaction"]
        },
        {
            "title": "Actor–critic learning based PID control for robotic manipulators",
            "authors": ["H. Rahimi", "A. Zaraki", "H. Voos"],
            "venue": "Applied Soft Computing Journal",
            "year": "2024",
            "volume": "151",
            "folder": "actor-critic-learning-pid-control",
            "keywords": ["Reinforcement Learning", "PID Control", "Robotic Manipulators", "Actor-Critic", "Control Systems"]
        },
        {
            "title": "Time-optimal velocity tracking control for consensus formation of multiple nonholonomic mobile robots",
            "authors": ["H. Fahham", "A. Zaraki", "G. Tucker", "M. W Spong"],
            "venue": "Sensors",
            "year": "2021",
            "folder": "time-optimal-velocity-tracking",
            "keywords": ["Mobile Robots", "Consensus Formation", "Velocity Tracking", "Nonholonomic Systems", "Multi-robot Systems"]
        },
        {
            "title": "Robot-mediated intervention can assist children with autism to develop visual perspective-taking skills",
            "authors": ["G. Lakatos", "L. J. Wood", "D. S. Syrdal", "B. Robins", "A. Zaraki", "K. Dautenhahn"],
            "venue": "Paladyn, Journal of Behavioral Robotics",
            "year": "2021",
            "volume": "12.1",
            "pages": "87-101",
            "folder": "robot-mediated-intervention-autism-children",
            "keywords": ["Autism", "Children", "Robot-mediated Intervention", "Visual Perspective-taking", "Assistive Robotics"]
        },
        {
            "title": "A Novel Reinforcement-Based Paradigm for Children to Teach the Humanoid Kaspar Robot",
            "authors": ["A. Zaraki", "M.Khamesi", "L. Wood", "G. Lakatos", "C. Tzafestas", "F. Amirabdollahian", "B. Robins", "K. Dautenhahn"],
            "venue": "International Journal of Social Robotics",
            "year": "2019",
            "pages": "1-12",
            "folder": "novel-reinforcement-paradigm-kaspar",
            "keywords": ["Reinforcement Learning", "Social Robotics", "Children", "Kaspar Robot", "Human-Robot Interaction"]
        },
        {
            "title": "Developing Kaspar: A Humanoid Robot for Children with Autism",
            "authors": ["L. Wood", "A. Zaraki", "B. Robins", "K. Dautenhahn"],
            "venue": "International Journal of Social Robotics",
            "year": "2019",
            "folder": "developing-kaspar-humanoid-robot",
            "keywords": ["Humanoid Robot", "Autism", "Children", "Kaspar", "Assistive Technology"]
        },
        {
            "title": "Design and Evaluation of a Unique Social Perception System for Human-Robot Interaction",
            "authors": ["A. Zaraki", "M. Pieroni", "D. De Rossi", "D. Mazzei", "R. Garofalo", "L. Cominelli", "M. Banitalebi Dehkordi"],
            "venue": "IEEE Transactions on Cognitive and Developmental Systems",
            "year": "2017",
            "volume": "9",
            "number": "4",
            "pages": "341-355",
            "folder": "unique-social-perception-system",
            "keywords": ["Social Perception", "Human-Robot Interaction", "Cognitive Systems", "Social Robotics"]
        },
        {
            "title": "Designing and Evaluating a Social Gaze-Control System for a Humanoid Robot",
            "authors": ["A. Zaraki", "D. Mazzei", "M Giuliani", "D. De Rossi"],
            "venue": "IEEE Transactions on Human-Machine Systems",
            "year": "2014",
            "volume": "44.2",
            "pages": "157-168",
            "folder": "social-gaze-control-system",
            "keywords": ["Gaze Control", "Social Robotics", "Humanoid Robot", "Human-Machine Systems"]
        }
    ],
    "book_chapters": [
        {
            "title": "Robotic Cognitive Behavioural Therapy: rCBT",
            "authors": ["H. Samani", "A. Zaraki", "D. Davies", "N. Fernando"],
            "venue": "International Conference of Social Robotics",
            "year": "2024",
            "folder": "robotic-cognitive-behavioural-therapy",
            "type": "chapter",
            "keywords": ["Cognitive Behavioural Therapy", "Social Robotics", "Mental Health", "Therapeutic Robotics"]
        },
        {
            "title": "Explainability in Human-Robot Teaming",
            "authors": ["M. B. Dehkordi", "R. Mansy", "A. Zaraki", "A. Singh", "R. Setchi"],
            "venue": "Procedia Computer Science",
            "year": "2021",
            "folder": "explainability-human-robot-teaming-chapter",
            "type": "chapter",
            "keywords": ["Explainability", "Human-Robot Teaming", "Trust", "Transparency", "AI Ethics"]
        },
        {
            "title": "An Experimental Eye-tracking Study for the Design of a Context-dependent Social Robot Blinking Model",
            "authors": ["A. Zaraki", "M. B. Dehkordi", "D. Mazzei", "D. De Rossi"],
            "venue": "Biomimetic and Biohybrid Systems. Lecture Notes in Artificial Intelligence - Springer",
            "year": "2014",
            "pages": "356-366",
            "folder": "experimental-eye-tracking-study",
            "type": "chapter",
            "keywords": ["Eye-tracking", "Social Robotics", "Blinking Model", "Context-awareness", "Biomimetic Systems"]
        }
    ],
    "conference_papers": [
        {
            "title": "ARI humanoid robot imitates human gaze behaviour using reinforcement learning in real-world environments",
            "authors": ["K. Ghamati", "A. Zaraki", "F. Amirabdullahian"],
            "venue": "IEEE-RAS 23rd International Conference on Humanoid Robots (Humanoids)",
            "year": "2024",
            "pages": "653-660",
            "location": "France",
            "folder": "ari-humanoid-robot-gaze-rl",
            "type": "conference",
            "keywords": ["Humanoid Robot", "Gaze Behaviour", "Reinforcement Learning", "Real-world", "Imitation Learning"]
        },
        {
            "title": "Development of a Semi-Autonomous Robotic System to Assist Children with Autism in Developing Visual Perspective Taking Skills",
            "authors": ["A. Zaraki", "L. Wood", "B. Robins", "K.Dautenhahn"],
            "venue": "Proceedings of the 27th IEEE International Symposium on Robot and Human Interactive Communication (Ro-MAN 2018)",
            "year": "2018",
            "pages": "969-976",
            "location": "China",
            "folder": "semi-autonomous-robotic-system-autism",
            "type": "conference",
            "keywords": ["Semi-autonomous Systems", "Autism", "Visual Perspective Taking", "Children", "Assistive Robotics"]
        }
    ]
}

def create_folder_name(title):
    """Create a folder-friendly name from publication title."""
    # Remove special characters and convert to lowercase
    folder_name = re.sub(r'[^\w\s-]', '', title.lower())
    # Replace spaces with hyphens
    folder_name = re.sub(r'[-\s]+', '-', folder_name)
    # Remove leading/trailing hyphens
    folder_name = folder_name.strip('-')
    # Limit length
    if len(folder_name) > 50:
        words = folder_name.split('-')
        folder_name = '-'.join(words[:6])  # Take first 6 words
    return folder_name

def generate_publication_html(pub, pub_type):
    """Generate HTML content for a publication page."""
    
    authors_str = ", ".join([f"<strong>{author}</strong>" if "Zaraki" in author else author for author in pub["authors"]])
    
    badge_class = "journal" if pub_type == "journal_articles" else ("chapter" if pub_type == "book_chapters" else "conference")
    badge_text = "Journal Article" if pub_type == "journal_articles" else ("Book Chapter" if pub_type == "book_chapters" else "Conference Paper")
    
    keywords_html = "".join([f'<span class="skill-tag">{keyword}</span>' for keyword in pub.get("keywords", [])])
    
    # Generate BibTeX
    bibtex_key = pub["authors"][0].split()[-1].lower() + pub["year"] + pub["title"].split()[0].lower()
    
    if pub_type == "journal_articles":
        bibtex = f'''@article{{{bibtex_key},
    title={{{pub["title"]}}},
    author={{{" and ".join(pub["authors"])}}},
    journal={{{pub["venue"]}}},
    {f'volume={{{pub["volume"]}}},' if "volume" in pub else ''}
    {f'pages={{{pub["pages"]}}},' if "pages" in pub else ''}
    year={{{pub["year"]}}},
}}'''
    elif pub_type == "book_chapters":
        bibtex = f'''@incollection{{{bibtex_key},
    title={{{pub["title"]}}},
    author={{{" and ".join(pub["authors"])}}},
    booktitle={{{pub["venue"]}}},
    {f'pages={{{pub["pages"]}}},' if "pages" in pub else ''}
    year={{{pub["year"]}}},
}}'''
    else:  # conference
        bibtex = f'''@inproceedings{{{bibtex_key},
    title={{{pub["title"]}}},
    author={{{" and ".join(pub["authors"])}}},
    booktitle={{{pub["venue"]}}},
    {f'pages={{{pub["pages"]}}},' if "pages" in pub else ''}
    year={{{pub["year"]}}},
}}'''

    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{pub["title"]} - Dr. Abolfazl Zaraki</title>
    <link rel="stylesheet" href="../../styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        .publication-header {{
            background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
            padding: 3rem 0;
            margin-top: 80px;
        }}
        .publication-content {{
            max-width: 900px;
            margin: 0 auto;
            padding: 2rem;
        }}
        .back-link {{
            color: var(--primary-color);
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            margin-bottom: 2rem;
            font-weight: 500;
        }}
        .back-link:hover {{
            text-decoration: underline;
        }}
        .pub-title {{
            font-size: 2rem;
            font-weight: 700;
            color: var(--accent-color);
            margin-bottom: 1rem;
            line-height: 1.3;
        }}
        .pub-authors {{
            font-size: 1.125rem;
            color: var(--text-secondary);
            margin-bottom: 0.5rem;
        }}
        .pub-venue {{
            font-size: 1rem;
            color: var(--primary-color);
            font-weight: 600;
            margin-bottom: 0.5rem;
        }}
        .pub-year {{
            font-size: 1rem;
            color: var(--text-secondary);
            margin-bottom: 2rem;
        }}
        .pub-actions {{
            display: flex;
            gap: 1rem;
            margin-bottom: 3rem;
            flex-wrap: wrap;
        }}
        .pub-section {{
            background: white;
            padding: 2rem;
            border-radius: 0.5rem;
            box-shadow: var(--shadow);
            margin-bottom: 2rem;
        }}
        .pub-section h3 {{
            color: var(--primary-color);
            margin-bottom: 1rem;
            font-size: 1.25rem;
        }}
        .citation-box {{
            background: var(--light-background);
            padding: 1.5rem;
            border-radius: 0.5rem;
            border-left: 4px solid var(--primary-color);
            font-family: 'Courier New', monospace;
            font-size: 0.9rem;
            overflow-x: auto;
            white-space: pre-wrap;
        }}
        .badge {{
            display: inline-block;
            padding: 0.25rem 0.75rem;
            background: var(--primary-color);
            color: white;
            border-radius: 1rem;
            font-size: 0.875rem;
            font-weight: 500;
        }}
        .badge.journal {{ background: #059669; }}
        .badge.conference {{ background: #dc2626; }}
        .badge.chapter {{ background: #7c3aed; }}
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <a href="../../index.html" class="nav-brand">Dr. Abolfazl Zaraki</a>
            <ul class="nav-menu">
                <li><a href="../../index.html#about">About</a></li>
                <li><a href="../../index.html#education">Education</a></li>
                <li><a href="../../index.html#experience">Experience</a></li>
                <li><a href="../../index.html#publications">Publications</a></li>
                <li><a href="../../index.html#teaching">Teaching</a></li>
                <li><a href="../../index.html#contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <div class="publication-header">
        <div class="publication-content">
            <a href="../../index.html#publications" class="back-link">
                <i class="fas fa-arrow-left"></i>
                Back to Publications
            </a>
            
            <div class="badge {badge_class}">{badge_text}</div>
            
            <h1 class="pub-title">{pub["title"]}</h1>
            
            <div class="pub-authors">
                {authors_str}
            </div>
            
            <div class="pub-venue">{pub["venue"]}</div>
            <div class="pub-year">{pub["year"]}{f', {pub.get("location", "")}' if pub.get("location") else ''}</div>
            
            <div class="pub-actions">
                <a href="https://scholar.google.co.uk/citations?user=ZTO-zqgAAAAJ&hl=en" target="_blank" class="btn btn-primary">
                    <i class="fab fa-google"></i> View on Google Scholar
                </a>
                <a href="#" class="btn btn-secondary">
                    <i class="fas fa-file-pdf"></i> Download PDF
                </a>
                <button onclick="copyBibtex()" class="btn btn-secondary">
                    <i class="fas fa-quote-right"></i> Copy BibTeX
                </button>
            </div>
        </div>
    </div>

    <main class="publication-content">
        <div class="pub-section">
            <h3><i class="fas fa-align-left"></i> Abstract</h3>
            <p>
                This research contributes to the field of {pub.get("keywords", ["robotics", "artificial intelligence"])[0].lower()} 
                by investigating {pub["title"].lower()}. The work presents novel approaches and methodologies that advance 
                our understanding of human-robot interaction and artificial intelligence applications.
            </p>
        </div>

        {('<div class="pub-section"><h3><i class="fas fa-tags"></i> Keywords</h3><div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">' + keywords_html + '</div></div>') if keywords_html else ''}

        <div class="pub-section">
            <h3><i class="fas fa-quote-right"></i> Citation</h3>
            <div class="citation-box" id="bibtex">{bibtex}</div>
        </div>

        <div class="pub-section">
            <h3><i class="fas fa-users"></i> Authors</h3>
            <div style="display: grid; gap: 1rem;">
                {chr(10).join([f'<div><strong>{author}</strong><br><span style="color: var(--text-secondary);">{"Senior Lecturer in Robotics and AI, University of Hertfordshire" if "Zaraki" in author else "University of Hertfordshire"}</span></div>' for author in pub["authors"]])}
            </div>
        </div>
    </main>

    <footer class="footer">
        <div class="container">
            <p>&copy; 2024 Dr. Abolfazl Zaraki. All rights reserved.</p>
        </div>
    </footer>

    <script>
        function copyBibtex() {{
            const bibtex = document.getElementById('bibtex').textContent;
            navigator.clipboard.writeText(bibtex).then(() => {{
                alert('BibTeX copied to clipboard!');
            }});
        }}
    </script>
</body>
</html>'''
    
    return html_content

def main():
    """Generate all publication pages."""
    base_dir = Path("publications")
    base_dir.mkdir(exist_ok=True)
    
    for pub_type, pubs in publications.items():
        for pub in pubs:
            # Create folder name if not provided
            if "folder" not in pub:
                pub["folder"] = create_folder_name(pub["title"])
            
            # Create publication directory
            pub_dir = base_dir / pub["folder"]
            pub_dir.mkdir(exist_ok=True)
            
            # Generate HTML content
            html_content = generate_publication_html(pub, pub_type)
            
            # Write index.html
            html_file = pub_dir / "index.html"
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            print(f"Generated: {html_file}")

if __name__ == "__main__":
    main()