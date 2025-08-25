# Search interface for Jain Aagam Online Series 

Created from [tylergneill/prakrit_texts_search](https://github.com/tylergneill/prakrit_texts_search) as template.

A colleague with the full Jain Aagam Online Series (Muni Diparatnasagar ed.)
collection of .docx files requested a way to easily search through the whole thing,
preferably with IAST search input for the Devanagari content.

Served using GitHub Pages at https://tylergneill.github.io/prakrit_agama_search.

# How

First converted .docx files (`docx_source` folder) to HTML (`docs` folder) using `Pandoc`.

Then pointed Pagefind at HTML (output `docs/pagefind`).

Finally, included some transliteration and pagination sugar,
plus a little diagram of the relevant file structure.

Co-created with Gemini CLI.
