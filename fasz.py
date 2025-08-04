import military_symbol # pyright: ignore[reportMissingTypeStubs, reportUnknownMemberType, reportAttributeAccessIssue]

if __name__ == '__main__':
    # Print symbol generated from a name to STDOUT
    #print(military_symbol.get_symbol_svg_string_from_name("enemy infantry platoon"))


    # Generate a list of symbols from names and write them as SVG files in specific
    # styles, named according to a user-defined pattern and using variant symbols where available
    examples: list[tuple[str, str]] = [
        ('Enemy armor company', 'light'),
        ("Dummy damaged neutral hospital", 'heavy'),
        ("Friendly fighter", 'dark'),
        ("Destroyed neutral artillery task force headquarters", 'unfilled'),
        ("Suspected CBRN section", 'light')
    ]
    print(military_symbol.get_symbol_svg_string_from_name(examples[0][0], style=examples[2][1]))
