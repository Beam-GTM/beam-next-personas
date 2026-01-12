#!/usr/bin/env python3
"""
Custom Persona Generator

Generates expert personas on-the-fly based on user requirements.
Can be used during project creation or standalone.

Usage:
    python generate_persona.py --interactive  # Guided mode
    python generate_persona.py --description "Former insurance AP director..." # Natural mode
    python generate_persona.py --template  # Output empty template

Examples:
    # Interactive guided mode
    python generate_persona.py --interactive
    
    # Natural description
    python generate_persona.py --description "Someone who's implemented invoice automation at 5+ insurance companies and knows SOX compliance"
    
    # Just output template for manual filling
    python generate_persona.py --template > custom-persona.md
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional

def get_persona_template() -> str:
    """Return the base template for custom personas."""
    return """---
name: [Expert Name/Title]
slug: [auto-generated-slug]
category: custom
domain: [Specific Domain/Expertise Area]
description: [One-sentence description of expertise]
when_to_use:
  - [Situation 1]
  - [Situation 2]
  - [Situation 3]
best_for: [Key use cases, comma-separated]
is_custom: true
created_for: [Project name/id]
created_date: {date}
famous_for: [Their experience/background]
---

# [Name] Perspective

**Core Philosophy**: [What drives their thinking and approach? What do they fundamentally believe about this domain?]

## Questions They Would Ask

- [Question 1: Specific, actionable question they'd ask about the project]
- [Question 2: Challenge an assumption]
- [Question 3: Probe for hidden complexity]
- [Question 4: Ask about edge cases]
- [Question 5: Question the approach]
- [Question 6: Ask about failure modes]
- [Question 7: Challenge timeline/resources]
- [Question 8: Ask about stakeholders]
- [Question 9: Question success criteria]
- [Question 10: Ask "what could go wrong?"]

## Their Approach

1. **[Principle 1]** - [How they think about this aspect]
2. **[Principle 2]** - [Their methodology or framework]
3. **[Principle 3]** - [What they prioritize]
4. **[Principle 4]** - [How they solve problems]
5. **[Principle 5]** - [Their risk mitigation approach]
6. **[Principle 6]** - [How they measure success]
7. **[Principle 7]** - [Their long-term view]

## Red Flags They'd Spot

- **[Red Flag 1]** - [Why this is a problem]
- **[Red Flag 2]** - [What this indicates]
- **[Red Flag 3]** - [Why this fails]
- **[Red Flag 4]** - [What's missing]
- **[Red Flag 5]** - [Unrealistic expectation]
- **[Red Flag 6]** - [Common mistake]
- **[Red Flag 7]** - [Warning sign]
- **[Red Flag 8]** - [What people overlook]

## Key Insights They'd Share

- **[Insight 1]**: [Counter-intuitive or important principle]
- **[Insight 2]**: [What most people get wrong]
- **[Insight 3]**: [Critical success factor]
- **[Insight 4]**: [Risk that's often overlooked]
- **[Insight 5]**: [Optimization opportunity]
- **[Insight 6]**: [Long-term consideration]
- **[Insight 7]**: [Practical wisdom]
- **[Insight 8]**: [Scalability consideration]

## Example Application

**Project**: "[Current project name and brief description]"

**[Name] would ask:**
- [Specific question 1 for this project]
- [Specific question 2 for this project]
- [Specific question 3 for this project]
- [Specific question 4 for this project]
- [Specific question 5 for this project]

**Their likely advice:**
- [Specific recommendation 1]
- [Specific recommendation 2]
- [Specific recommendation 3]
- [Specific recommendation 4]
- [Specific recommendation 5]

## Output

- [Deliverable 1: What this persona would help produce]
- [Deliverable 2: Analysis or framework they'd provide]
- [Deliverable 3: Decision support they'd offer]
- [Deliverable 4: Risk assessment they'd create]
- [Deliverable 5: Implementation guidance]
"""

def generate_slug(name: str) -> str:
    """Generate URL-friendly slug from name."""
    return name.lower().replace(' ', '-').replace('(', '').replace(')', '').replace('/', '-')

def interactive_mode() -> Dict[str, str]:
    """Collect persona requirements interactively."""
    print("\n=== Custom Expert Persona Generator ===\n")
    print("I'll help you create a custom expert persona for your project.\n")
    
    requirements = {}
    
    # Basic info
    print("1. What's their role/title?")
    print("   Example: 'Former VP of Finance Operations at Fortune 500 Insurance'")
    requirements['role'] = input("   → ").strip()
    
    print("\n2. What's their specific domain expertise?")
    print("   Example: 'AP automation, insurance compliance, SOX controls, legacy system integration'")
    requirements['domain'] = input("   → ").strip()
    
    print("\n3. What industry/context?")
    print("   Example: 'Insurance (P&C, Life), Fortune 500'")
    requirements['industry'] = input("   → ").strip()
    
    print("\n4. What challenges should they spot?")
    print("   Example: 'Compliance gaps, integration complexity, change management risks'")
    requirements['challenges'] = input("   → ").strip()
    
    print("\n5. What's your project context?")
    print("   Example: 'Invoice automation for Zurich Insurance'")
    requirements['project'] = input("   → ").strip()
    
    print("\n6. (Optional) Any specific experience they should have?")
    print("   Example: '10+ implementations, dealt with failed audits, knows what actually breaks'")
    requirements['experience'] = input("   → ").strip()
    
    return requirements

def generate_ai_prompt(requirements: Dict[str, str]) -> str:
    """Generate prompt for AI to create full persona."""
    
    prompt = f"""STEP 1: RESEARCH REAL EXPERTS FIRST

Before creating a persona, identify 2-3 REAL experts in this domain:

REQUIREMENTS:
- Role/Title: {requirements.get('role', 'N/A')}
- Domain Expertise: {requirements.get('domain', 'N/A')}
- Industry/Context: {requirements.get('industry', 'N/A')}
- Challenges to Spot: {requirements.get('challenges', 'N/A')}
- Project Context: {requirements.get('project', 'N/A')}
- Specific Experience: {requirements.get('experience', 'N/A')}

RESEARCH SOURCES:
1. Books written on this topic (Amazon, Google Books)
2. Academic researchers (Google Scholar)
3. Industry thought leaders (LinkedIn, conference speakers)
4. Practitioners with published work (articles, blogs, talks)
5. Company founders/executives with documented frameworks

FIND: 2-3 real people who:
- Have published books/major articles on this topic
- Have documented frameworks or methodologies
- Have unique insights (not just experience)
- Are recognized experts in this specific domain
- Have talks/presentations available (YouTube, conferences)

OUTPUT FORMAT:
For each expert found:
- Name: [Real name]
- Background: [Their actual background]
- Famous for: [Their book/framework/methodology]
- Documented work: [Books, articles, talks - specific titles]
- Unique perspective: [What makes their thinking different]
- Why relevant: [How they fit the requirements]

---

STEP 2: ONCE EXPERT IS SELECTED, CREATE PERSONA

Generate a complete expert persona that follows the standard format with:

1. NAME: Create a descriptive title (e.g., "Insurance AP Automation & Compliance Specialist")
2. CORE PHILOSOPHY: 2-3 sentences capturing their worldview and approach
3. QUESTIONS (10): Specific, actionable questions they'd ask about projects in their domain
4. APPROACH (7): Principles and methodologies they follow
5. RED FLAGS (8): Specific warning signs they'd spot based on their experience
6. KEY INSIGHTS (8): Counter-intuitive or critical insights from their domain
7. EXAMPLE APPLICATION: Apply to the specific project context provided

Make it:
- Specific and actionable (not generic advice)
- Based on real-world experience in this domain
- Focused on what actually matters vs what people think matters
- Include practical wisdom from 10+ years in the field
- Highlight common mistakes and failure modes
- Provide concrete, applicable guidance

Use the exact template format provided, filling in all sections with domain-specific content."""

    return prompt

def save_persona(content: str, project_name: Optional[str] = None, permanent: bool = False) -> str:
    """Save generated persona to file."""
    
    # Determine save location
    script_path = Path(__file__).resolve()
    base_path = script_path.parent.parent.parent
    
    if permanent:
        # Save to library
        personas_dir = base_path / "00-system" / "expert-personas" / "custom"
        personas_dir.mkdir(parents=True, exist_ok=True)
    else:
        # Save to temp/project location
        if project_name:
            personas_dir = base_path / "02-projects" / project_name / "personas"
        else:
            personas_dir = Path("/tmp/nexus-custom-personas")
        personas_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate filename from content (extract slug from YAML)
    lines = content.split('\n')
    slug = None
    for line in lines:
        if line.startswith('slug:'):
            slug = line.split(':', 1)[1].strip()
            break
    
    if not slug:
        slug = f"custom-persona-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    
    filepath = personas_dir / f"{slug}.md"
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return str(filepath)

def main():
    parser = argparse.ArgumentParser(description='Generate custom expert personas')
    parser.add_argument('--interactive', '-i', action='store_true',
                        help='Interactive guided mode')
    parser.add_argument('--description', '-d', type=str,
                        help='Natural description of needed expert')
    parser.add_argument('--template', '-t', action='store_true',
                        help='Output empty template')
    parser.add_argument('--save', '-s', action='store_true',
                        help='Save to library (default: temp only)')
    parser.add_argument('--project', '-p', type=str,
                        help='Project name/context')
    
    args = parser.parse_args()
    
    # Output template
    if args.template:
        template = get_persona_template()
        print(template.format(date=datetime.now().strftime('%Y-%m-%d')))
        return
    
    # Interactive mode
    if args.interactive:
        requirements = interactive_mode()
        
        print("\n" + "="*50)
        print("REQUIREMENTS COLLECTED")
        print("="*50)
        print(json.dumps(requirements, indent=2))
        print("\n" + "="*50)
        print("\nTo generate the full persona, use an AI assistant with this prompt:\n")
        print(generate_ai_prompt(requirements))
        print("\n" + "="*50)
        print("\nCopy the generated persona and:")
        print("1. Save it to a file (e.g., custom-persona.md)")
        print("2. Move to: 00-system/mental-models/personas/custom/")
        print("3. Or use: python generate_persona.py --save < generated-persona.md")
        return
    
    # Natural description mode
    if args.description:
        requirements = {
            'description': args.description,
            'project': args.project or 'Current project'
        }
        
        print("\n" + "="*50)
        print("GENERATING PERSONA PROMPT")
        print("="*50)
        print("\nDescription:", args.description)
        print("\nTo generate the full persona, use an AI assistant with this prompt:\n")
        
        prompt = f"""Create a detailed expert persona based on this description:

"{args.description}"

Project context: {args.project or 'General use'}

Follow the standard persona template format with:
- Name/title fitting the description
- Core philosophy
- 10 specific questions they'd ask
- 7 principles they follow
- 8 red flags they'd spot
- 8 key insights they'd share
- Example application

Make it specific, actionable, and based on real-world expertise in this domain."""
        
        print(prompt)
        return
    
    # No args - show help
    parser.print_help()

if __name__ == "__main__":
    main()
