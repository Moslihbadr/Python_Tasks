import pytube

link = input("entrez url : ")

yt = pytube.YouTube(link)

yt.streams.first().download()

print("téléchargement terminé !")