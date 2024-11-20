from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window
Window.size=(500,500)
Window.clearcolor=(0,0,0,0)
import time
e=0
class ox(App):
        def build(self):
              g1=GridLayout(cols=3)
              b0=Button(text="Retry",background_color=(1,0,1, 1),size_hint=[1,.3],on_press=self.retry)

              self.b1=Button(text="",on_press=self.r1,background_color=(0,1,1, 1))

              self.b2=Button(text="",on_press=self.r2,background_color=(0,1,1, 1))

              self.b3=Button(text="",on_press=self.r3,background_color=(0,1,1, 1))

              self.b4=Button(text="",on_press=self.r4,background_color=(0,1,1, 1))

              self.b5=Button(text="",on_press=self.r5,background_color=(0,1,1, 1))

              self.b6=Button(text="",on_press=self.r6,background_color=(0,1,1, 1))

              self.b7=Button(text="",on_press=self.r7,background_color=(0,1,1, 1))

              self.b8=Button(text="",on_press=self.r8,background_color=(0,1,1, 1))

              self.b9=Button(text="",on_press=self.r9,background_color=(0,1,1, 1))

              self.b10=Button(text="Result",on_press=self.result,background_color=(1,1,0, 1))

              b11=Label(text="X-O GAME",font_size=25)

              g1.add_widget(self.b1)

              g1.add_widget(self.b2)

              g1.add_widget(self.b3)

              g1.add_widget(self.b4)

              g1.add_widget(self.b5)

              g1.add_widget(self.b6)

              g1.add_widget(self.b7)

              g1.add_widget(self.b8)

              g1.add_widget(self.b9)

              g1.add_widget(self.b10)

              g1.add_widget(b0)

              g1.add_widget(b11)

              return g1

        def retry(self,obj1):

              e=0

              self.b1.text=""

              self.b2.text=""

              self.b3.text=""

              self.b4.text=""

              self.b5.text=""

              self.b6.text=""

              self.b7.text=""

              self.b8.text=""

              self.b9.text=""

              self.b10.text="RESULT"

        def r1(self,obj):

          e=0

          e=self.esult(e)

          if(self.b1.text=="" and e==0):

              self.b1.text="X"

              if self.b1.text=="X" and self.b3.text=="X" and self.b2.text=="":

                self.b2.text="O"

              elif self.b1.text=="X" and self.b9.text=="X" and self.b5.text=="" :

                self.b5.text="O"

              elif self.b1.text!="" and self.b7.text!="" and self.b4.text=="":

                self.b4.text="O"

              elif self.b2.text!="" and self.b3.text=="" and self.b3.text=="":

                self.b3.text="O"

              elif self.b5.text=="" and self.b9.text!="":

                self.b5.text="O"

              elif self.b5.text!="" and self.b9.text=="":

                self.b9.text="O"

              elif self.b4.text!="" and self.b7.text=="":

                self.b7.text="O"

              elif self.b4.text=="" and self.b7.text!="":

                self.b4.text="O"

              elif self.b1.text!="" and self.b7.text!="":

                self.b4.text="O"

              elif self.b9.text=="":

                self.b9.text="O"

              elif self.b7.text=="":

                self.b7.text="O"

              elif self.b3.text=="":

                self.b3.text="O"

              elif self.b2.text=="":

                self.b2.text="O"

              elif self.b4.text=="":

                self.b4.text="O"

              elif self.b5.text=="":

                self.b5.text="O"

              elif self.b6.text=="":

                self.b6.text="O"

              elif self.b8.text=="":

                self.b8.text="O"

          self.result()

        def r2(self,obj):

          e=0

          e=self.esult(e)

          if(self.b2.text=="" and e==0):

              self.b2.text="X"

              if self.b5.text=="" and self.b8.text!="":

                self.b5.text="O"

              elif self.b3.text=="O" and self.b9.text=="O" and self.b6.text=="":

                self.b6.text="O"

              elif self.b5.text!="" and self.b8.text=="":

                self.b8.text="O"

              elif self.b1.text=="" and self.b3.text!="":

                self.b1.text="O"

              elif self.b1.text!="" and self.b3.text=="":

                self.b3.text="O"

              elif self.b5.text=="":

                self.b5.text="O"

              elif self.b1.text=="":

                self.b1.text="O"

              elif self.b3.text=="":

                self.b3.text="O"

              elif self.b6.text=="":

                self.b6.text="O"

              elif self.b4.text=="":

                self.b4.text="O"

              elif self.b9.text=="":

                self.b9.text="O"

              elif self.b7.text=="":

                self.b7.text="O"

              elif self.b8.text=="":

                self.b8.text="O"

          self.result()

        def r3(self,obj):

          e=0

          e=self.esult(e)

          if(self.b3.text=="" and e==0):

              self.b3.text="X"

              if self.b1.text=="" and self.b2.text!="":

                self.b1.text="O"

              elif self.b3.text=="X" and self.b7.text=="X" and self.b5.text=="":

                self.b5.text="O"

              elif self.b7.text=="O" and self.b9.text=="O" and self.b8.text=="":

                self.b8.text="O"

              elif self.b1.text=="X" and self.b3.text=="X" and self.b2.text=="":

                self.b2.text="O"

              elif self.b3.text=="X" and self.b9.text=="X" and self.b6.text=="":

                self.b6.text="O"

              elif self.b1.text=="O" and self.b2.text=="" and self.b2.text=="":

                self.b2.text="O"

              elif self.b3.text=="X" and self.b9.text=="X" and self.b6.text=="":

                self.b6.text="O"

              elif self.b5.text=="" and self.b7.text!="":

                self.b5.text="O"

              elif self.b5.text!="" and self.b7.text=="":

                self.b7.text="O"

              elif self.b6.text!="" and self.b9.text=="":

                self.b9.text="O"

              elif self.b6.text=="" and self.b9.text!="":

                self.b6.text="O"

              elif self.b7.text=="":

                self.b7.text="O"

              elif self.b1.text=="":

                self.b1.text="O"

              elif self.b9.text=="":

                self.b9.text="O"

              elif self.b2.text=="":

                self.b2.text="O"

              elif self.b6.text=="":

                self.b6.text="O"

              elif self.b5.text=="":

                self.b5.text="O"

              elif self.b4.text=="":

                self.b4.text="O"

              elif self.b8.text=="":

                self.b8.text="O"

          self.result()

        def r4(self,obj):

          e=0

          e=self.esult(e)

          if(self.b4.text=="" and e==0):

              self.b4.text="X"

              if self.b1.text=="" and self.b7.text!="":

                self.b1.text="O"

              elif self.b1.text!="" and self.b7.text=="":

                self.b7.text="O"

              elif self.b5.text=="" and self.b6.text!="":

                self.b5.text="O"

              elif self.b5.text!="" and self.b6.text=="":

                self.b6.text="O"

              elif self.b5.text=="":

                self.b5.text="O"

              elif self.b1.text=="":

                self.b1.text="O"

              elif self.b7.text=="":

                self.b7.text="O"

              elif self.b2.text=="":

                self.b2.text="O"

              elif self.b3.text=="":

                self.b3.text="O"

              elif self.b6.text=="":

                self.b6.text="O"

              elif self.b8.text=="":

                self.b8.text="O"

              elif self.b9.text=="":

                self.b9.text="O"

          self.result()

        def r5(self,obj):

          e=0

          e=self.esult(e)

          if(self.b5.text=="" and e==0):

              self.b5.text="X"

              if self.b1.text=="" and self.b9.text=="X":

                self.b1.text="O"

              elif self.b1.text=="O" and self.b3.text=="O" and self.b2.text=="":

                self.b2.text="O"

              elif self.b3.text=="O" and self.b9.text=="O" and self.b6.text=="":

                self.b6.text="O"

              elif self.b1.text=="O" and self.b7.text=="O" and self.b4.text=="":

                self.b4.text="O"

              elif self.b1.text!="" and self.b9.text=="":

                self.b9.text="O"

              elif self.b2.text=="" and self.b8.text!="":

                self.b2.text="O"

              elif self.b2.text!="" and self.b8.text=="":

                self.b8.text="O"

              elif self.b3.text!="" and self.b7.text=="":

                self.b7.text="O"

              elif self.b4.text=="X" and self.b5.text=="X" and self.b6.text=="":

                self.b6.text="O"

              elif self.b3.text=="" and self.b7.text!="":

                self.b3.text="O"

              elif self.b4.text=="" and self.b6.text!="":

                self.b4.text="O"

              elif self.b4.text!="" and self.b6.text=="":

                self.b6.text="O"

              elif self.b3.text=="":

                self.b3.text="O"

              elif self.b7.text=="":

                self.b7.text="O"

              elif self.b9.text=="":

                self.b9.text="O"

              elif self.b1.text=="":

                self.b1.text="O"

              elif self.b2.text=="":

                self.b2.text="O"

              elif self.b6.text=="":

                self.b6.text="O"

              elif self.b8.text=="":

                self.b8.text="O"

              elif self.b4.text=="":

                self.b4.text="O"

          self.result()

        def r6(self,obj):

          e=0

          e=self.esult(e)

          if(self.b6.text=="" and e==0):

              self.b6.text="X"

              if self.b3.text=="" and self.b9.text=="X":

                self.b3.text="O"

              elif self.b2.text=="O" and self.b5.text=="O" and self.b8.text=="":

                self.b8.text="O"

              elif self.b3.text!="" and self.b9.text=="":

                self.b9.text="O"

              elif self.b4.text=="" and self.b5.text!="":

                self.b4.text="O"

              elif self.b4.text!="" and self.b5.text=="":

                self.b5.text="O"

              elif self.b5.text=="":

                self.b5.text="O"

              elif self.b3.text=="":

                self.b3.text="O"

              elif self.b9.text=="":

                self.b9.text="O"

              elif self.b2.text=="":

                self.b2.text="O"

              elif self.b8.text=="":

                self.b8.text="O"

              elif self.b1.text=="":

                self.b1.text="O"

              elif self.b4.text=="":

                self.b4.text="O"

              elif self.b7.text=="":

                self.b7.text="O"

          self.result()

        def r7(self,obj):

          e=0

          e=self.esult(e)

          if(self.b7.text=="" and e==0):

              self.b7.text="X"

              if self.b1.text=="" and self.b4.text!="":

                self.b1.text="O"

              elif self.b3.text=="X" and self.b7.text=="X" and self.b5.text=="":

                self.b5.text="O"

              elif self.b9.text=="X" and self.b7.text=="X" and self.b8.text=="":

                self.b8.text="O"

              elif self.b1.text!="" and self.b4.text=="":

                self.b4.text="O"

              elif self.b7.text=="X" and self.b8.text=="X" and self.b5.text=="O" and self.b9.text=="":

                self.b9.text="O"

              elif self.b7.text=="X" and self.b8.text=="" and self.b9.text=="X" and self.b5.text=="":

                self.b8.text="O"

              elif self.b5.text=="" and self.b7.text=="X" and self.b9.text=="X" and self.b8.text=="":

                self.b8.text="O"

              elif self.b5.text=="" and self.b3.text!="":

                self.b5.text="O"

              elif self.b5.text!="" and self.b3.text=="":

                self.b3.text="O"

              elif self.b8.text!="" and self.b9.text=="":

                self.b9.text="O"

              elif self.b8.text=="" and self.b9.text!="":

                self.b8.text="O"

              elif self.b3.text=="":

                self.b3.text="O"

              elif self.b1.text=="":

                self.b1.text="O"

              elif self.b9.text=="":

                self.b9.text="O"

              elif self.b5.text=="":

                self.b5.text="O"

              elif self.b8.text=="":

                self.b8.text="O"

              elif self.b4.text=="":

                self.b4.text="O"

              elif self.b2.text=="":

                self.b2.text="O"

              elif self.b6.text=="":

                self.b6.text="O"

          self.result()

        def r8(self,obj):

          e=0

          e=self.esult(e)

          if(self.b8.text=="" and e==0):

              self.b8.text="X"

              if self.b3.text=="O" and self.b9.text=="O" and self.b6.text=="":

                self.b6.text="O"

              elif self.b2.text=="" and self.b5.text!="" :

                self.b2.text="O"

              elif self.b9.text!="" and self.b8.text!="" and self.b5.text=="O" and self.b7.text=="":

                self.b7.text="O"

              elif self.b7.text=="X" and self.b8.text=="X" and self.b5.text=="O" and self.b9.text=="":

                self.b9.text="O"

              elif self.b2.text!="" and self.b5.text=="":

                self.b5.text="O"

              elif self.b7.text=="" and self.b9.text!="":

                self.b7.text="O"

              elif self.b7.text!="" and self.b9.text=="":

                self.b9.text="O"

              elif self.b5.text=="":

                self.b5.text="O"

              elif self.b7.text=="":

                self.b7.text="O"

              elif self.b9.text=="":

                self.b9.text="O"

              elif self.b2.text=="":

                self.b2.text="O"

              elif self.b4.text=="":

                self.b4.text="O"

              elif self.b6.text=="":

                self.b6.text="O"

              elif self.b1.text=="":

                self.b1.text="O"

              elif self.b3.text=="":

                self.b3.text="O"

          self.result()

        def r9(self,obj):

          e=0

          e=self.esult(e)

          if(self.b9.text=="" and e==0):

              self.b9.text="X"

              if self.b9.text=="X" and self.b8.text=="X" and self.b5.text=="O" and self.b7.text=="":

                self.b7.text="O"

              elif self.b2.text=="O" and self.b5.text=="O" and self.b8.text=="":

                self.b8.text="O"

              elif self.b3.text=="X" and self.b9.text=="X" and self.b6.text=="":

                self.b6.text="O"

              elif self.b1.text=="" and self.b5.text!="":

                self.b1.text="O"

              elif self.b5.text=="" and self.b7.text=="X" and self.b9.text=="X" and self.b8.text=="":

                self.b8.text="O"

              elif self.b1.text!="" and self.b5.text=="":

                self.b5.text="O"

              elif self.b1.text=="X" and self.b9.text=="X" and self.b5.text=="":

                self.b5.text="O"

              elif self.b7.text=="" and self.b8.text!="":

                self.b7.text="O"

              elif self.b7.text=="X" and self.b9.text=="X" and self.b5.text=="" and self.b8.text=="":

                self.b8.text="O"

              elif self.b7.text!="" and self.b8.text=="":

                self.b8.text="O"

              elif self.b3.text!="" and self.b6.text=="":

                self.b6.text="O"

              elif self.b3.text=="" and self.b6.text!="":

                self.b3.text="O"

              elif self.b1.text=="":

                self.b1.text="O"

              elif self.b3.text=="":

                self.b3.text="O"

              elif self.b3.text=="":

                self.b3.text="O"

              elif self.b7.text=="":

                self.b7.text="O"

              elif self.b8.text=="":

                self.b8.text="O"

              elif self.b6.text=="":

                self.b6.text="O"

              elif self.b1.text=="":

                self.b1.text="O"

              elif self.b2.text=="":

                self.b2.text="O"

              elif self.b4.text=="":

                self.b4.text="O"

          self.result()

        def esult(self,e):

                if self.b1.text=="X" and self.b2.text=="X" and self.b3.text=="X":

                  e=e+1

                elif self.b4.text=="X" and self.b5.text=="X" and self.b6.text=="X":

                  e=e+1

                elif self.b7.text=="X" and self.b8.text=="X" and self.b9.text=="X":

                  e=e+1

                elif self.b1.text=="X" and self.b5.text=="X" and self.b9.text=="X":

                  e=e+1

                elif self.b3.text=="X" and self.b5.text=="X" and self.b7.text=="X":

                  e=e+1

                elif self.b2.text=="X" and self.b5.text=="X" and self.b8.text=="X":

                  e=e+1

                elif self.b1.text=="X" and self.b4.text=="X" and self.b7.text=="X":

                  e=e+1

                elif self.b3.text=="X" and self.b6.text=="X" and self.b9.text=="X":

                  e=e+1

                elif self.b1.text=="O" and self.b2.text=="O" and self.b3.text=="O":

                  e=e+1

                elif self.b4.text=="O" and self.b5.text=="O" and self.b6.text=="O":

                  e=e+1

                elif self.b7.text=="O" and self.b8.text=="O" and self.b9.text=="O":

                  e=e+1

                elif self.b1.text=="O" and self.b5.text=="O" and self.b9.text=="O":

                  e=e+1

                elif self.b3.text=="O" and self.b5.text=="O" and self.b7.text=="O":

                  e=e+1

                elif self.b2.text=="O" and self.b5.text=="O" and self.b8.text=="O":

                  e=e+1

                elif self.b1.text=="O" and self.b4.text=="O" and self.b7.text=="O":

                  e=e+1

                elif self.b3.text=="O" and self.b6.text=="O" and self.b9.text=="O":

                  e=e+1

                elif self.b1.text!="" and self.b2.text!="" and self.b3.text!="" and self.b4.text!="" and self.b5.text!="" and self.b6.text!="" and self.b7.text!="" and self.b8.text!="" and self.b9.text!="":

                  e=e+1

                else:

                  e=0

                return e

        def result(self):

              if self.b1.text=="X" and self.b2.text=="X" and self.b3.text=="X":

                self.b10.text="YOU WIN"

              elif self.b4.text=="X" and self.b5.text=="X" and self.b6.text=="X":

                self.b10.text="YOU WIN"

              elif self.b7.text=="X" and self.b8.text=="X" and self.b9.text=="X":

                self.b10.text="YOU WIN"

              elif self.b1.text=="X" and self.b5.text=="X" and self.b9.text=="X":

                self.b10.text="YOU WIN"

              elif self.b3.text=="X" and self.b5.text=="X" and self.b7.text=="X":

                self.b10.text="YOU WIN"

              elif self.b2.text=="X" and self.b5.text=="X" and self.b8.text=="X":

                self.b10.text="YOU WIN"

              elif self.b1.text=="X" and self.b4.text=="X" and self.b7.text=="X":

                self.b10.text="YOU WIN"

              elif self.b3.text=="X" and self.b6.text=="X" and self.b9.text=="X":

                self.b10.text="YOU WIN"

              elif self.b1.text=="O" and self.b2.text=="O" and self.b3.text=="O":

                self.b10.text="COM WIN"

              elif self.b4.text=="O" and self.b5.text=="O" and self.b6.text=="O":

                self.b10.text="COM WIN"

              elif self.b7.text=="O" and self.b8.text=="O" and self.b9.text=="O":

                self.b10.text="COM WIN"

              elif self.b1.text=="O" and self.b5.text=="O" and self.b9.text=="O":

                self.b10.text="COM WIN"

              elif self.b3.text=="O" and self.b5.text=="O" and self.b7.text=="O":

                self.b10.text="COM WIN"

              elif self.b2.text=="O" and self.b5.text=="O" and self.b8.text=="O":

                self.b10.text="COM WIN"

              elif self.b1.text=="O" and self.b4.text=="O" and self.b7.text=="O":

                self.b10.text="COM WIN"

              elif self.b3.text=="O" and self.b6.text=="O" and self.b9.text=="O":

                self.b10.text="COM WIN"   

              elif self.b1.text!="" and self.b2.text!="" and self.b3.text!="" and self.b4.text!="" and self.b5.text!="" and self.b6.text!="" and self.b7.text!="" and self.b8.text!="" and self.b9.text!="":

                self.b10.text="TIE"

              return self.b10.text

game=ox()

game.run()
