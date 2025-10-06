#-*- coding: utf-8 -*-
{
    "name" : "Carpooling",
    "version": "1.0",
    "description": """
                    Module to help you to organize the traject with your employees.
                    Make your life easier !
                """,
    "author": "Nalios",
    "website":"www.omias-group.com",
    "license": "LGPL-3",
    "category": "Customizations",
    "depends": ['base', 'sale'],
    "data": [
        'security/ir.model.access.csv',
        'views/carpooling_views.xml',
       
    ],
}