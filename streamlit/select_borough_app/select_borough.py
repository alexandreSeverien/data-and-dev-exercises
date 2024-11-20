#imports
import streamlit as st
import pandas as pd
import seaborn as sns



#Affichage du titre de la page
prenom = "Alexandre"
st.title(f"Bienvenue sur le site web de {prenom}")


#chargement du dataset et enregistrement des arrondissements dans une liste
taxis = sns.load_dataset("taxis")

boroughs = list(taxis.pickup_borough.unique())
boroughs = [str(borough) for borough in boroughs]


#affichage du sélecteur
choice = st.multiselect("Indiquez votre arrondissement de récupération",
               boroughs,
               max_selections = 1,
               placeholder = "aucun arrondissement choisi")

#enregistrement des images
manhattan_picture = "https://images.unsplash.com/photo-1616530744217-a0f469ec719f?q=80&w=2942&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
queens_picture = "https://images.unsplash.com/photo-1678665035747-3e7596323a5c?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
nan_picture = "https://images.unsplash.com/photo-1601027847350-0285867c31f7?q=80&w=3087&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
bronx_picture = "https://images.unsplash.com/photo-1689783101576-627f2fbdb8d5?q=80&w=3087&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
brooklyn_picture = "https://images.unsplash.com/photo-1665169768935-adfbc9409aa6?q=80&w=2532&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

#stockage des images dans un dictionnaire
pictures = {
    "Manhattan" : manhattan_picture,
    "Queens" : queens_picture,
    "nan" : nan_picture,
    "Bronx" : bronx_picture,
    "Brooklyn" : brooklyn_picture
}


#affichage de l'image choisie
if choice:
    st.image(pictures[choice[0]])
