# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Executif(models.Model):
    _name = "salaire.executif"
    _description = "Table de tous les executifs déjà entré dans le système"

    nom = fields.Char(string="Nom")
    prenom = fields.Char(string="Prenom")
    sexe = fields.Selection([("M", "Masculin"), ("F", "Feminin")], string="Sexe")
