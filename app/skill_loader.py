from pathlib import Path
import yaml

class Skill:
    def __init__(self, name, description, metadata, instructions, path):
        self.name = name
        self.description = description
        self.metadata = metadata
        self.instructions = instructions
        self.path = path

class SkillLoader:
    def __init__(self, skill_directory="skills"):
        self.skill_directory = Path(skill_directory)

    def load_all(self):
        skills = {}
        for file in self.skill_directory.glob("*.md"):
            skill = self._load(file)
            skills[skill.name] = skill
        return skills

    def _load(self, file):
        content = file.read_text(encoding="utf-8")
        parts = content.split("---", 2)
        if len(parts) != 3:
            raise ValueError(f"Invalid skill file: {file}")
        metadata = yaml.safe_load(parts[1])
        return Skill(
            name=metadata["name"],
            description=metadata["description"],
            metadata=metadata,
            instructions=parts[2].strip(),
            path=str(file)
        )
