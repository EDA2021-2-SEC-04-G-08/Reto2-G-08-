﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

from DISClib.ADT import list as lt
from DISClib.ADT.indexminpq import size
import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
def initCatalog(estructuraDatos):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(estructuraDatos)
    return catalog


# Funciones para la carga de datos


def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArt(catalog)
    loadArtist(catalog)
    

def loadArt(catalog):
   
    artworksfile = cf.data_dir +  'Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworksfile , encoding='utf-8'))
    for artwork in input_file:
        model.addArt(catalog, artwork)


def loadArtist(catalog):
 
    artistsfile = cf.data_dir + 'Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    contador= 0
    for artist in input_file:
        """
        if contador>=50:
            break
        else: 
            model.addArtist(catalog, artist)
            contador+=1
        """
        model.addArtist(catalog, artist)
        contador+=1

def get_info_transporte(arte, nombre_departamento):
    return model.get_transporte(arte, nombre_departamento)


def obras_porMedio(catalog, num ,medio):
    list = model.obras_medio(catalog, medio)
    listaorganizada = model.organizar_medio(list, num)
    return listaorganizada

   
def obrasPorNacionalidadEspecifica(catalog, nac):
    model.nacionalidadPorObra(catalog)
def obrasPorNacionalidad(catalog, nac):
    return model.tamañoMapaNacionalidad(catalog, nac)

def ObrasPorNacionalidades(catalog):
    model.nacionalidadPorObra(catalog)
    lista = model.listaNacionalidad(catalog)
    return lista
    
def transportarobras(catalog, dept):
    size = model.sizelistaDepart(catalog, dept)
    precios = model.get_estimado_precio(catalog, dept)[0]
    listaobras = model.get_estimado_precio(catalog, dept)[1]
    listaorganizada = model.organizarPrecio(listaobras)
    pesoTotal = model.get_estimado_peso(catalog, dept)
    listaObrasAntiguas = model.obras_antiguas(catalog, dept)
    listaAntiguasOrganizada = model.organizarPrecio(listaObrasAntiguas)
    return size, precios, listaorganizada, pesoTotal, listaAntiguasOrganizada

def obrasPorAnio(catalog, fechai, fechaf):
    size = lt.size(catalog['Art'])
    lista_filtrada = lt.newList()
    obrasPorCompra = 0
    for pos in range(size):
        art = lt.getElement(catalog['Art'], pos)
        model.AddArtFecha(art, fechai, fechaf, lista_filtrada)
        if model.escompra(art):
            obrasPorCompra += 1
    
    lista_organizada = model.OrganizarFecha(lista_filtrada)
    sizefinal = lt.size(lista_organizada)
    r = [lista_organizada, sizefinal, obrasPorCompra]
    return r
    
    


def get_req1(artistas, inicio, final):
    return model.nacimiento_artistas(artistas, inicio, final)

def get_req3(catalog, nombre_artista):
    return model.get_obrasxtecnica(catalog, nombre_artista)

