# Setting Up GitHub Repository

## Quick Setup

Run these commands to sync to GitHub:

```bash
cd /Users/jbd/Documents/Cursor/nexus-jbd/beam-next-personas

# Initialize git (if not already)
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial release: Expert Personas Framework v1.0.0"

# Add remote (if not already added)
git remote add origin https://github.com/Beam-GTM/beam-next-personas.git

# Push to GitHub
git branch -M main
git push -u origin main

# Create version tag
git tag v1.0.0
git push origin v1.0.0
```

## Installation Link

Once pushed, users can install with:

```bash
git clone https://github.com/Beam-GTM/beam-next-personas.git
cd beam-next-personas
./install-standalone.sh /path/to/their/nexus
```

Or as a one-liner:

```bash
git clone https://github.com/Beam-GTM/beam-next-personas.git && cd beam-next-personas && ./install-standalone.sh /path/to/nexus
```

## Repository URL

**Repository**: https://github.com/Beam-GTM/beam-next-personas

**Install Command**:
```bash
git clone https://github.com/Beam-GTM/beam-next-personas.git && cd beam-next-personas && ./install-standalone.sh /path/to/nexus
```
