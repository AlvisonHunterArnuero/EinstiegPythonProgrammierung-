class ProgrammerSkills:
    def __init__(self):
        self.name = 'Alvison Lucas Hunter Arnuero'
        self.languages = 'JavaScript, Python, C#, VB.NET'
        self.frameworks = 'jQuery, VueJS, AngularJS, NextJS, Flask'
        self.libraries = 'ReactJS'
        self.cssframeworks = 'BootStrap 4, Semantic UI, Chakra, TailwindCSS, Bulma'
        self.CMS = 'WordPress, Joomla, Drupal, PencilBlue'
        self.other_skills = 'Adobe Suite CC, ZBrush, 3dMax, O365, Excel VBA'
    
    def displaySkills(self):
        for attr, value in self.__dict__.items():
            print(f'{attr.upper()}: {value}')

CV = ProgrammerSkills()
CV.displaySkills()
