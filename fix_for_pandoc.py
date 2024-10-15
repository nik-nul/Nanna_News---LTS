with open('tmp.tex', 'r') as i:
    content = i.read()

new = content.replace(
        '\\newsavebox\\colbbox', ''
    ).replace(
        '\\setbox', ''
    ).replace(
        '\\colbbox', ''
    ).replace(
        '\\vbox{', ''
    ).replace(
        '\\makeatletter', ''
    ).replace(
        '\\col@number\@ne', ''
    ).replace(
        '\\unpenalty}', ''
    ).replace(
        '}\\unvbox', ''
    ).replace(
        '\\unvbox', ''
    ).replace(
        '\\unpenalty', ''
    ).replace(
        '\\uskip', ''
    ).replace(
        '\\pagebreak', ''
    )

with open('tmp.tex', 'w') as o:
    o.write(new)