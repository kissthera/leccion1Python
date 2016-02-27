#!/usr/bin/env pythob
# -*- coding: utf-8 -*-
nomUsuario = raw_input ("nombre completo")
nacimiento = input ("ayo de nacimiento")
FActual = input ("ayo actual")
edad = FActual - nacimiento
print nomUsuario + "su edad es de" + str(edad)
if edad <= 12:
    print "ninio"
else:
    print "adolesente"
