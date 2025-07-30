# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a GitHub Pages repository (azaraki.github.io) for Dr. Abolfazl Zaraki's academic profile website. The site serves as a professional academic portfolio showcasing research, publications, and career achievements.

## Site Architecture

This is a static academic website with the following key components:

### Core Pages
- **index.html**: Main landing page with profile overview, recent highlights, and navigation
- **publications.html**: Complete publication list with filtering and search capabilities
- **research.html**: Research interests and current projects
- **teaching.html**: Course information and teaching philosophy
- **students.html**: Student supervision and opportunities
- **experience.html**: Academic and professional experience

### Generated Content System
- **generate_publications.py**: Python script that automatically generates individual publication pages
- **publications/**: Directory containing auto-generated pages for each publication
- **publication-template.html**: Template for individual publication pages (if present)

### Static Assets
- **styles.css**: Modern academic styling with responsive design (Bilge Mutlu inspired)
- **script.js**: JavaScript for navigation, smooth scrolling, and responsive behavior
- **Abolfazl_Zaraki.webp**: Profile photo

## Key Development Commands

### Publication Management
```bash
# Generate all individual publication pages
python3 generate_publications.py

# The script reads publication data from its internal database and creates:
# - Individual HTML pages for each publication in publications/[folder-name]/index.html
# - Proper navigation and back-links
# - BibTeX citations with copy functionality
# - Keywords and metadata display
```

### Development Workflow
```bash
# No build process required - direct file editing
# Test locally by opening index.html in browser
# GitHub Pages automatically serves from repository root

# For development testing:
python3 -m http.server 8000
# Then visit http://localhost:8000
```

## Code Architecture

### Publication Generation System
The `generate_publications.py` script contains a comprehensive database of publications structured in three categories:
- **journal_articles**: Peer-reviewed journal publications
- **book_chapters**: Book chapters and proceedings
- **conference_papers**: Conference presentations and papers

Each publication entry includes:
- Title, authors, venue, year
- Folder name for URL structure
- Keywords for categorization
- Metadata (volume, pages, location)

### Styling System
The site uses a cohesive design system with:
- **CSS Variables**: Consistent color scheme and spacing
- **Responsive Grid**: Mobile-first design approach
- **Component Classes**: Reusable UI components (cards, buttons, navigation)
- **Academic Theme**: Professional presentation suitable for academic portfolios

### Navigation & UX
- **Mobile-responsive**: Hamburger menu and adaptive layouts
- **Smooth scrolling**: Enhanced navigation experience
- **Active section highlighting**: Visual feedback for current page section
- **Error handling**: Graceful degradation for missing images

## Content Integration

### Google Scholar Integration
- Publications link to Google Scholar profile: https://scholar.google.co.uk/citations?user=ZTO-zqgAAAAJ&hl=en
- Citation metrics and h-index pulled from Scholar profile
- Individual publications can link to Scholar entries

### CV Integration
- Content derived from "CV-Abolfazl Zaraki-UH .pdf" (excluded from repository)
- Structured data maintained in Python script for consistency
- Professional formatting matching academic standards

## Development Notes

### File Organization
- Static files served directly from repository root
- Publication pages organized in subdirectories for clean URLs
- All external dependencies loaded via CDN (no local node_modules)

### Deployment
- GitHub Pages automatic deployment from main branch
- No build step required - pure static HTML/CSS/JS
- Custom domain support available through GitHub Pages settings

### Content Updates
- Publication data: Update `generate_publications.py` and regenerate pages
- General content: Direct HTML editing in respective page files
- Styling changes: Modify `styles.css` with CSS variables for consistency

### Professional Standards
- Academic presentation with clean, professional styling
- Responsive design for desktop and mobile viewing
- Accessibility considerations in navigation and content structure
- SEO-friendly structure with proper meta tags and semantic HTML