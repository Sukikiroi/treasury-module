{
    "name": "الخزينة",
    "summary": "Manage Khazina.",
    "author": "kaddour Abdelaziz",
    "category": "Services/Khazina",
    "license": "AGPL-3",
    "website": "https://github.com/Sukikiroi/treasury-module",
    "version": "15.0.1.0.0",
    "depends": ["base"],
    "application": True,
    
    "data": [
        "security/khazina_security.xml",
        "security/ir.model.access.csv",
        "views/khazina_request_loan_view.xml",
        "views/khazina_request_fund_deposit_view.xml",
        "views/khazina_testimonial_coins_conversion_veiw.xml",
        "views/khazina_coins_conversion_view.xml",
        "views/khazina_menu.xml",
    ],
    "css": ["static/src/css/test.css"],
    "assets": {
        "web.assets_backend": [
            "khazina/static/src/css/test.css",
        ],
    },
}
