# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
import AthenaDocumentor

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def main(root_module):
    parser = AthenaDocumentor.Parser(root_module=root_module).parse()
    # output the desired root_module to JSON
    parser.output_to_json_file(
        "exports/documentor.json"
    )
    # output the desired root_module to Markdown
    parser.output_to_markdown_file(
        r"exports\documentor.md",
        ... # TODO ! write the file path of the obsidian reference file
    )

if __name__ == '__main__':
    main(
      root_module = ... # TODO ! import and write the module to parse  
    )
