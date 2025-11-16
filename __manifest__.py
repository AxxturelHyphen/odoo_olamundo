{
    'name': "Odoo Ola Mundo",
    'summary': "Módulo de ejemplo Ola Mundo",
    'description': """
Módulo de prueba para crear:
- Un modelo simple
- Sus vistas y menús
- Y gestionarlo con git
    """,

    'author': "guija",
    'website': "https://github.com/AxxturelHyphen",

    'category': 'Uncategorized',
    'version': '14.0.1.0.0',

    # para que salga en “Aplicaciones”
    'application': True,

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/olamundo.xml',
        'views/menu.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}




