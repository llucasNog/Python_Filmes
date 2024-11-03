import pyautogui as py
import time as t
import pandas

# Abrindo o Google
py.PAUSE = 0.5
py.press("win")
py.write("Chrome")
t.sleep(1.5)
py.press("Enter")
t.sleep(1.5)
py.hotkey("win","Up")
t.sleep(1.5)
py.write("file:///C:/Users/lukas/Desktop/Automa%C3%A7%C3%A3o%20Filmes/Site_Filmes/Home.html")
py.press("Enter")
t.sleep(1)
py.press("Tab")

#colocando a lista
Filmes = pandas.read_csv("Filmes.csv")
print(Filmes)

for linha in Filmes.index:
    
    Cod = str(Filmes.loc[linha, 'Nome'])
    py.write(Cod)
    py.press("tab")

    Cod = str(Filmes.loc[linha, 'Data'])
    py.write(Cod)
    py.press("tab")

    Cod = str(Filmes.loc[linha, 'Genero'])
    py.write(Cod)
    py.press("tab")
  
    Cod = str(Filmes.loc[linha, 'Descri'])
    py.write(Cod)
    py.press("tab")

    Cod = str(Filmes.loc[linha, 'url'])
    py.write(Cod)
    py.press("tab")
    py.press("Enter")
    py.click(x=1184, y=392)
    py.press("tab")







