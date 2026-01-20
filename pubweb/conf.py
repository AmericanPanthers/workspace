project = 'American Panthers'
copyright = '2026, American Panthers'
author = 'American Panthers'
html_title = 'Amercan Panthers'
lang = 'en'

heart_svg = '''
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 512 512">
    <path fill="currentColor" d="M47.6 300.4L228.3 469.1c7.5 7 17.4 10.9 27.7 10.9s20.2-3.9 27.7-10.9L464.4 300.4c30.4-28.3 47.6-68 47.6-109.5v-5.8c0-69.9-50.5-129.5-119.4-141C347 36.5 300.6 51.4 268 84L256 96 244 84c-32.6-32.6-79-47.5-124.6-39.9C50.5 55.6 0 115.2 0 185.1v5.8c0 41.5 17.2 81.2 47.6 109.5z"></path>
</svg>
'''
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.rst']
html_static_path = ['_static']
html_css_files = ['custom.css']
html_theme = 'breeze'
html_context = {
    'github_user': 'AmericanPanthers',
    'github_repo': 'workspace',
    'github_version': 'main',
    'doc_path': 'pubweb',
}
html_theme_options = {
    "external_links": [
        {
            "name": "Get Involved",
            "url": "TO-DO",
            "html": heart_svg,
        },
    ]
}

#extensions = []
