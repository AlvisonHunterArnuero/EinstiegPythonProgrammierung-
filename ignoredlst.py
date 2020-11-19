class SLTeam:
  def __init__(self, coder, question):
    self.coder = coder
    self.question = question
    self.greeting = 'Hi, How are you'
    self.response = 'I will send you an email with all the details.'
    self.divider = '----------'
    self.ignoredlst =['Billi','Eleazar', 'Hector', 'Alvison']

  def coder_request(self):
      print("Hello Tio, " + self.question)
      if self.coder.title() in self.ignoredlst:
          print("chirp chirp chirp...")
      else:
          print(f"Hi {self.coder}, {self.response}")
          print('--------------------------------------------------')

request01 = SLTeam("Dan", "how much did you pay for netlify?")
request01.coder_request()

request02 = SLTeam("Billi", "how much did you pay for netlify?")
request02.coder_request()
